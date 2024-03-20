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
            existing_rows = db.tri_world.get_rows(
                'SELECT ID FROM world_safe_locs WHERE ID = %s',
                (wsl['ID'],)
            )
            
            if len(existing_rows) == 0:
                db.tri_world.execute(
                    ("INSERT INTO world_safe_locs (ID, MapID, LocX, LocY, LocZ, Facing, Comment) "
                    "VALUES (%s, %s, %s, %s, %s, %s, %s)"),
                    (wsl['ID'],
                    wsl['Continent'],
                    wsl['LocX'],
                    wsl['LocY'],
                    wsl['LocZ'],
                    0,
                    wsl['AreaName_Lang_enUS'],)
                )
            else:
                db.tri_world.execute(
                    ("UPDATE world_safe_locs SET "
                    "MapID = %s, LocX = %s, LocY = %s, LocZ = %s, Comment = %s "
                    "WHERE ID = %s"),
                    (wsl['Continent'],
                    wsl['LocX'],
                    wsl['LocY'],
                    wsl['LocZ'],
                    wsl['AreaName_Lang_enUS'],
                    wsl['ID'],)
                )
        
    
    # update graveyards
    
    vm_graveyards = db.vm_world.get_rows(
        'SELECT id, ghost_zone, faction FROM game_graveyard_zone WHERE patch_max = 10'
    )
    
    for vm_gy in vm_graveyards:
        match_wsl = None
        for wsl in world_safe_locs:
            if wsl['ID'] == vm_gy[0]:
                match_wsl = wsl
                break

        if match_wsl != None and match_wsl['Continent'] <= constants.MaxMapId:
            existing_records = db.tri_world.get_rows(
                ("SELECT ID, GhostZone, Faction, Comment FROM graveyard_zone "
                "WHERE ID = %s "
                "AND GhostZone = %s"),
                (vm_gy[0], vm_gy[1],)
            )
            
            if len(existing_records) == 0:
                db.tri_world.execute(
                    ("INSERT INTO graveyard_zone (ID, GhostZone, Faction, Comment) "
                    "VALUES (%s, %s, %s, %s)"),
                    (vm_gy[0], vm_gy[1], vm_gy[2], match_wsl['AreaName_Lang_enUS'],)
                )
            else:
                db.tri_world.execute(
                    ("UPDATE graveyard_zone SET "
                    "Faction = %s, Comment = %s "
                    "WHERE ID = %s AND GhostZone = %s"),
                    (vm_gy[2], match_wsl['AreaName_Lang_enUS'], vm_gy[0], vm_gy[1],)
                )
    

    f.close()