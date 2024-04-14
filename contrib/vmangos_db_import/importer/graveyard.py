#!/usr/bin/python3

import constants
import database as db
import json

#TODO

def Import():
    f = open('WorldSafeLocs.json')
    # data doesnt exist in client any more 
    # get a data from a JSON export from the old DBC
    world_safe_locs = json.load(f)
    
    # update safe locs
    
    for wsl in world_safe_locs:
        if wsl['Continent'] <= constants.MaxMapId:
            existing_row = db.tri_world.select_one(
                    db.SelectQuery("world_safe_locs").where("ID", "=", wsl['ID'])
                )

            upsert_query = db.UpsertQuery("world_safe_locs").values({
                "MapID": wsl['Continent'],
                "LocX": wsl['LocX'],
                "LocY": wsl['LocY'],
                "LocZ": wsl['LocZ'],
                "Comment": wsl['AreaName_Lang_enUS']
            })
            
            if existing_row == None:
                upsert_query.values({
                    "ID": wsl['ID'],
                    "Facing": 0 
                })
            else:
                upsert_query.where("ID", "=", wsl['ID'])
            
            db.tri_world.upsert(upsert_query)
    
    # update graveyards
    
    vm_graveyards = db.vm_world.select_all(
        db.SelectQuery("game_graveyard_zone").where("patch_max", "=", 10)
    )
    
    for vm_gy in vm_graveyards:
        match_wsl = None
        for wsl in world_safe_locs:
            if wsl['ID'] == vm_gy['id']:
                match_wsl = wsl
                break

        if match_wsl != None and match_wsl['Continent'] <= constants.MaxMapId:
            
            match_condition = db.GroupCondition("AND").condition("ID", "=", vm_gy['id']).condition("GhostZone", "=", vm_gy['ghost_zone'])
            existing_record = db.tri_world.select_one(
                db.SelectQuery("graveyard_zone").where(match_condition)
            )
            
            upsert_query = db.UpsertQuery("graveyard_zone").values({
                'Faction': vm_gy['faction'],
                'Comment': match_wsl['AreaName_Lang_enUS']
            })
            
            if existing_record == None:
                upsert_query.values({
                    'ID': vm_gy['id'],
                    'GhostZone': vm_gy['ghost_zone']
                })
            else:
                upsert_query.where(match_condition)
                
            db.tri_world.upsert(upsert_query)
    

    f.close()
    
    cleanup_obsolete_graveyards()
    
def cleanup_obsolete_graveyards():
    
    trinity_gys = db.tri_world.select_all(
        db.SelectQuery("graveyard_zone")
    )
    
    for trinity_gy in trinity_gys:
        vm_gy = db.vm_world.select_one(
            db.SelectQuery("game_graveyard_zone").where(
                db.GroupCondition("AND").condition("patch_max", "=", 10).condition("id", "=", trinity_gy['ID'])
            )
        )
        
        if vm_gy == None:
            db.tri_world.delete(
                db.DeleteQuery("graveyard_zone").where("ID", "=", trinity_gy["ID"])
            )