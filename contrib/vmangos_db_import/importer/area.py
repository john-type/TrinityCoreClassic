#!/usr/bin/python3

import constants
import database as db

def Import():
    handle_taverns()
    handle_teleports()
    remove_instances()


def handle_taverns():
    # remove taverns that dont exist in VMangos
    taverns_deleted = 0   
    rows = db.tri_world.select_all(
        db.SelectQuery("areatrigger_tavern")
    )
    
    for row in rows:
        vm_rows = db.vm_world.select_all(
                db.SelectQuery("areatrigger_tavern").where(
                    db.Condition("id", "=", row['id'])
                ) 
            )
        
        if len(vm_rows) == 0:
            db.tri_world.delete(
                db.DeleteQuery("areatrigger_tavern").where(
                    db.Condition("id", "=", row['id'])
                )
            )
            taverns_deleted += 1
            
    print("Deleted {} areatrigger_tavern's".format(taverns_deleted))
        

def handle_teleports():    
   
    teleports = {
        "deleted": 0,
        "updated": 0,
        "added": 0
    }
    
    #TODO update labels/names/comments
    
    #remove or update teleports from vmangos
    rows = db.tri_world.get_rows_raw((
        "SELECT * FROM areatrigger_teleport AS at "
        "LEFT JOIN world_safe_locs AS wsl ON at.PortLocID = wsl.ID"
    ))
    for row in rows:
        vm_row = db.vm_world.get_row_raw(
            "SELECT * FROM areatrigger_teleport WHERE ID = %s ORDER BY patch DESC LIMIT 1", 
            (row[0],)
        )
        if vm_row != None:
            db.tri_world.execute_raw("DELETE FROM areatrigger_teleport WHERE ID = %s", (row[0],))
            teleports['deleted'] += 1
        else:
            db.tri_world.execute_raw(
                ("UPDATE world_safe_locs "
                "SET MapID = %s, LocX = %s, LocY = %s, LocZ = %s, Facing = %s "
                "WHERE ID = %s"),
                (
                    vm_row[6], # map
                    vm_row[7], # x
                    vm_row[8], # y
                    vm_row[9], # z
                    vm_row[10], # facing
                    row[1], #id
                )
                )
            teleports['updated'] += 1
     
            
    query_tri_teleports = (
        "SELECT * FROM areatrigger_teleport AS at "
        "LEFT JOIN world_safe_locs AS wsl ON at.PortLocID = wsl.ID "
        "WHERE at.ID = %s"
    )
    
    insert_tri_safe_loc = (
        "INSERT INTO world_safe_locs "
        "(MapID, LocX, LocY, LocZ, Facing, Comment) "
        "VALUES "
        "(%s, %s, %s, %s, %s, %s)"
    )
    
    insert_tri_teleport = (
        "INSERT INTO areatrigger_teleport "
        "(ID, PortLocID, Name) "
        "VALUES "
        "(%s, %s, %s) "
    )
    
    #add teleports that exist in vmangos
    rows = db.vm_world.get_rows_raw("SELECT * FROM areatrigger_teleport")
    for row in rows:
        tri_rows = db.tri_world.get_rows_raw(query_tri_teleports, (row[0],))
        if len(tri_rows) == 0:
            # teleport is missing in trinity, add it.
            world_safe_loc_id = db.tri_world.insert_raw(
                insert_tri_safe_loc, 
                (
                    row[6],
                    row[7],
                    row[8],
                    row[9],
                    row[10],
                    row[2],
                )
                )
            
            db.tri_world.insert_raw(
                insert_tri_teleport,
                (
                    row[0],
                    world_safe_loc_id,
                    row[2]
                )
            )
            
            teleports['added'] += 1
           
    
    print("Changes to areatrigger_teleport's")
    for tele in teleports:
        print("{0} {1}".format(tele, teleports[tele]))    
    

def remove_instances():
    db.tri_world.delete(
        db.DeleteQuery("instance_template") \
            .where(db.Condition('map', '>', constants.MaxMapId))
    )
