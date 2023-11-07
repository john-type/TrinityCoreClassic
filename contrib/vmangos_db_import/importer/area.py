#!/usr/bin/python3

import constants
import database as db

def Import():
    handle_taverns()
    handle_teleports()
    handle_access_requirements()
    handle_areatriggers()
    handle_areatrigger_templates()


def handle_taverns():
    # remove taverns that dont exist in VMangos
    query_tri_taverns = "SELECT * FROM areatrigger_tavern"
    query_vm_taverns = "SELECT * FROM areatrigger_tavern WHERE id = %s"
    query_tri_taverns_delete = "DELETE FROM areatrigger_tavern WHERE id = %s"
     
    taverns_deleted = 0
     
    rows = db.GetRows(query_tri_taverns, 'tri_world') 
    for row in rows:
        vm_rows = db.GetRows(query_vm_taverns, 'vm_world', (row[0], ))
        if len(vm_rows) == 0:
            db.Execute(query_tri_taverns_delete, 'tri_world', (row[0],))
            taverns_deleted += 1
            
    print("Deleted {} areatrigger_tavern's".format(taverns_deleted))
        

def handle_teleports(): 
    query_tri_teleports = (
        "SELECT * FROM areatrigger_teleport AS at "
        "LEFT JOIN world_safe_locs AS wsl ON at.PortLocID = wsl.ID"
    )
    query_vm_teleports = "SELECT * FROM areatrigger_teleport WHERE ID = %s ORDER BY patch DESC LIMIT 1"
    query_tri_teleports_delete = "DELETE FROM areatrigger_teleport WHERE ID = %s"
    
    query_tri_update_safe_loc = (
        "UPDATE world_safe_locs "
        "SET MapID = %s, LocX = %s, LocY = %s, LocZ = %s, Facing = %s "
        "WHERE ID = %s"
    )
    
    teleports = {
        "deleted": 0,
        "updated": 0,
        "added": 0
    }
    
    #TODO update labels/names/comments
    
    #remove or update teleports from vmangos
    rows = db.GetRows(query_tri_teleports, 'tri_world')
    for row in rows:
        vm_rows = db.GetRows(query_vm_teleports, 'vm_world', (row[0],))
        if len(vm_rows) == 0:
            db.Execute(query_tri_teleports_delete, 'tri_world', (row[0],))
            teleports['deleted'] += 1
            #TODO - should world_safe_locs be deleted too?
        else:
            vm_row = vm_rows[0]
            db.Execute(
                query_tri_update_safe_loc, 
                'tri_world',
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
     
            
    query_vm_teleports = "SELECT * FROM areatrigger_teleport"
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
    rows = db.GetRows(query_vm_teleports, 'vm_world')
    for row in rows:
        tri_rows = db.GetRows(query_tri_teleports, 'tri_world', (row[0],))
        if len(tri_rows) == 0:
            # teleport is missing in trinity, add it.
            world_safe_loc_id = db.Insert(
                insert_tri_safe_loc, 
                'tri_world', 
                (
                    row[6],
                    row[7],
                    row[8],
                    row[9],
                    row[10],
                    row[2],
                )
                )
            
            db.Insert(
                insert_tri_teleport,
                'tri_world',
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
    
    
def handle_access_requirements():
    pass
    # TODO
    
def handle_areatriggers():
    # these tables are quite small, hard coding for now.
    query = 'DELETE FROM areatrigger WHERE SpawnId >= 4'
    query2 = 'DELETE FROM areatrigger_template_actions WHERE AreaTriggerId >= 4'

    db.Execute(query, 'tri_world')
    db.Execute(query2, 'tri_world')
    
def handle_areatrigger_templates():
    pass
    #TODO