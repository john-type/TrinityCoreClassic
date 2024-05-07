#!/usr/bin/python3

import constants
import database as db

def uint32_to_int32(uint32_value):
    if uint32_value <= 2147483647:
        return uint32_value
    else:
        return uint32_value - 4294967296

def Import():
    # clean_templates_check_vmangos()
    # clean_entries_check_vmangos()
    import_templates_vmangos()
    # import_entries_vmangos()
    #remove_duplicate_entries()
    #update_instance_info()

    
def clean_templates_check_vmangos():
    db.tri_world.chunk_raw(
        "SELECT entry, type, displayId, name FROM gameobject_template LIMIT %s OFFSET %s",
        500,
        _handle_clean_template_row
    )

def _handle_clean_template_row(row):
    dest_obj_query = ("SELECT entry, type, displayId, name FROM gameobject_template "
                    "WHERE entry = %s "
                    "ORDER BY patch DESC LIMIT 1")
    
    delete_src_obj_entity_queries = [
        ("DELETE FROM gameobject_addon WHERE guid = %s"),
        ("DELETE FROM game_event_gameobject WHERE guid = %s"),
        ("DELETE FROM game_event_gameobject_quest WHERE id = %s"),
        ("DELETE FROM gameobject WHERE guid = %s"),
    ]
    
    delete_src_queries = [
        ("DELETE FROM gameobject_questender WHERE id = %s"),
        ("DELETE FROM gameobject_questitem WHERE GameObjectEntry = %s"),
        ("DELETE FROM gameobject_queststarter WHERE id = %s"),
        ("DELETE FROM gameobject_loot_template WHERE entry = %s"),
        ("DELETE FROM gameobject_template_locale WHERE entry = %s"),
        ("DELETE FROM gameobject_template_addon WHERE entry = %s"),
        ("DELETE FROM gameobject_template WHERE entry = %s")
    ]
    
    match = db.vm_world.get_rows_raw(dest_obj_query, (row[0],))
            
    if len(match) == 0:
        entities = db.tri_world.get_rows_raw("SELECT guid FROM gameobject WHERE id = %s", (row[0],))
        for entity in entities:
            db.tri_world.execute_many_raw(delete_src_obj_entity_queries, (entity[0],))
            
        db.tri_world.execute_many_raw(delete_src_queries, (row[0],))
        return -1

    return 0

def clean_entries_check_vmangos():
    db.tri_world.chunk_raw(
        "SELECT guid, id, map, position_x, position_y, position_z FROM gameobject LIMIT %s OFFSET %s",
        500,
        _handle_clean_entry_row
    )
    
def _handle_clean_entry_row(row):
    dest_obj_query = ("SELECT guid, id, map, position_x, position_y, position_z FROM gameobject "
                    "WHERE id = %s AND map = %s AND patch_max = 10")
    
    delete_src_obj_entity_queries = [
        ("DELETE FROM gameobject_addon WHERE guid = %s"),
        ("DELETE FROM game_event_gameobject WHERE guid = %s"),
        ("DELETE FROM game_event_gameobject_quest WHERE id = %s"),
        ("DELETE FROM gameobject WHERE guid = %s"),
    ]
    
    matches = db.wm_world.get_rows_raw(dest_obj_query, (row[1],row[2],))
    matches_len = len(matches)

    if(matches_len == 0):
        db.tri_world.execute_many_raw(delete_src_obj_entity_queries, (row[0],))
        return -1
    
    return 0
        
def import_templates_vmangos():
    vm_rows = db.vm_world.select_chunked(
        db.SelectQuery("gameobject_template").order_by("entry ASC, patch ASC"),
        250
    )
    
    for vm_row in vm_rows:
        existing_row = db.tri_world.select_one(
            db.SelectQuery("gameobject_template").select("entry, type, displayid, name").where("entry", "=", vm_row['entry'])
        )
        
        _upsert_gameobject_template(vm_row, existing_row)
    

def import_entries_vmangos():
    db.vm_world.chunk_raw(
        "SELECT guid, id, map, position_x, position_y, position_z FROM gameobject WHERE patch_max = 10 LIMIT %s OFFSET %s",
        500,
        _handle_import_entry_row
    )

def _handle_import_entry_row(row):
    dest_obj_query = ("SELECT guid, id, map, position_x, position_y, position_z FROM gameobject "
                    "WHERE id = %s "
                    "AND position_x BETWEEN %s AND %s "
                    "AND position_y BETWEEN %s AND %s "
                    "AND map = %s")
    
    diff = 5
    matches = db.tri_world.get_rows_raw(dest_obj_query, (
                            row[1],
                            row[3] - diff,
                            row[3] + diff,
                            row[4] - diff,
                            row[4] + diff,
                            row[2],
                            )) 
    
    matches_len = len(matches)
    if(matches_len == 0):
        _upsert_gameobject_entry(row[0])
    elif(matches_len == 1):
        _upsert_gameobject_entry(row[0], matches[0][0])
    else:
        nearest_match = matches[0]
        nearest_abs = abs(matches[0][3] - row[3]) + abs(matches[0][4] - row[4])

        for near_match in matches:
            next_abs = abs(near_match[3] - row[3]) + abs(near_match[4] - row[4])
            if(next_abs < nearest_abs):
                nearest_match = near_match
                nearest_abs = next_abs
        
        _upsert_gameobject_entry(row[0], nearest_match[0])    
    
    return 0   

def _upsert_gameobject_template(vm_got, tri_got = None) :  
        
    if tri_got != None:
        #confirm safe type conversions
        safe = vm_got['type'] == tri_got['type'] or \
            (vm_got['type'] == 3 and tri_got['type'] == 50)   # gather_node -> chest
        
        if safe == False:
            return  #TODO when importer is fully implemented this can be removed.
        
    
    go_upsert = db.UpsertQuery("gameobject_template").values({
        'type': vm_got['type'],
        'displayId': vm_got['displayId'],
        'name': vm_got['name'],
        'size': vm_got['size'],
        'ContentTuningId': 0,
        'VerifiedBuild': constants.TargetBuild
    })
    
    # manually fixing data attributes!
    #ensure max >+ min.
    if vm_got['type'] == 3: # chest
        vm_got['data5'] = max(vm_got['data4'], vm_got['data5']) 
    elif vm_got['type'] == 25: # fishing hole
        vm_got['data3'] =  max(vm_got['data2'], vm_got['data3'])  
    
    for i in range(0, 23 + 1):
        go_upsert.values({
            'Data'+str(i): uint32_to_int32(vm_got['data'+str(i)])
        })
    
    #TODO handle additional data fields.
    
    if tri_got == None:
        go_upsert.values({
            'entry': vm_got['entry']
        })
    else:
        go_upsert.where('entry', "=", vm_got['entry'])
    
    db.tri_world.upsert(go_upsert)
        
    existing_addon = db.tri_world.select_one(
        db.SelectQuery("gameobject_template_addon").where("entry", "=", vm_got['entry'])
    )
    
    addon_upsert = db.UpsertQuery("gameobject_template_addon").values({
        'faction': vm_got['faction'],
        'flags': vm_got['flags'],
        'mingold': vm_got['mingold'],
        'maxgold': vm_got['maxgold'],
        #artkits?
    })
    
    if existing_addon == None:
        addon_upsert.values({
            'entry': vm_got['entry']
        })
    else:
        addon_upsert.where('entry', "=", vm_got['entry'])
        
    db.tri_world.upsert(addon_upsert)
    

    
def _upsert_gameobject_entry(vm_go_guid, tri_go_guid = None):

    
    src_obj = db.vm_world.get_row_raw((
        "SELECT id, map, position_x, position_y, position_z, orientation,"
        "rotation0, rotation1, rotation2, rotation3, spawntimesecsmin, animprogress, state "
        "FROM gameobject WHERE guid = %s"
        ), (vm_go_guid,))
    
    if src_obj == None:
        return
    
    dest_insert = (
        "INSERT INTO gameobject ("
        "id, map, zoneId, areaId, spawnDifficulties, phaseUseFlags, PhaseId, PhaseGroup, terrainSwapMap, "
        "position_x, position_y, position_z, orientation, rotation0, rotation1, rotation2, rotation3, "
        "spawntimesecs, animprogress, state, ScriptName, VerifiedBuild"
        ") VALUES ("
        "%s, %s, 0, 0, 0, 0, 0, 0, -1, "
        "%s, %s, %s, %s, %s, %s, %s, %s,"
        "%s, %s, %s, \"\", 40618"
        ")"
        )
    
    dest_update = (
        "UPDATE gameobject SET "
        "position_x = %s, position_y = %s, position_z=%s, orientation=%s, rotation0=%s, rotation1=%s, rotation2=%s, rotation3=%s, "
        "spawntimesecs = %s, animprogress=%s, state = %s, VerifiedBuild = 40618 "
        "WHERE guid = %s"
    )
    
    if tri_go_guid == None:
        pass #TODO handle insert
    else:
        db.tri_world.execute_raw(dest_update, (
            src_obj[2], src_obj[3], src_obj[4], src_obj[5], src_obj[6],  src_obj[7],  src_obj[8],  src_obj[9],  
            src_obj[10], src_obj[11], src_obj[12], tri_go_guid
        ,))
    
    if tri_go_guid == None:
        return


    # check if is an event creature.
    # event_rows = db.vm_world.get_rows_raw(
    #     "SELECT guid, event FROM game_event_gameobject WHERE guid = %s", 
    #     (vm_go_guid,)
    # )
    # matches_len = len(event_rows)
    
    # if(matches_len > 0):
    #     match_row = event_rows[0]
         
    #     tri_event_rows = db.tri_world.get_rows_raw(
    #         "SELECT guid, eventEntry FROM game_event_gameobject WHERE guid = %s AND eventEntry = %s"
    #         (tri_go_guid, match_row[1],)
    #     )
        
    #     if(len(tri_event_rows) == 0):
    #         #TODO ensure event id's match between tri and vm.
    #         db.tri_world.execute_raw(
    #             "INSERT INTO game_event_gameobject (guid, eventEntry) VALUES (%s, %s)", 
    #             (tri_go_guid, match_row[1],)
    #         )
        
def remove_duplicate_entries():    
    # duplicates got in at some point :(
    db.tri_world.chunk_raw(
        "SELECT guid, id, map, position_x, position_y, position_z, phaseId FROM gameobject WHERE id IN (174626) LIMIT %s OFFSET %s",
        500,
        _handle_clean_duplicate_entry_row
    )

def _handle_clean_duplicate_entry_row(row):    
    duplicates = db.tri_world.get_rows_raw((
        "SELECT guid, id, map, position_x, position_y, position_z FROM gameobject "
        "WHERE id = %s AND map = %s AND abs(position_x - %s) < 0.001 AND abs(position_y - %s) < 0.001 AND abs(position_z - %s) < 0.001 AND PhaseId = %s ORDER BY guid DESC"
        ),
        (row[1], row[2], row[3], row[4], row[5], row[6],)) 
    
    vm_matches = db.vm_world.get_rows_raw((
        "SELECT guid, id, map, position_x, position_y, position_z FROM gameobject "
        "WHERE id = %s AND map = %s AND abs(position_x - %s) < 0.001 AND abs(position_y - %s) < 0.001 AND abs(position_z - %s) < 0.001"
        ),
        (row[1], row[2], row[3], row[4], row[5],))
    
    vm_guids = []
    for vm in vm_matches:
        vm_guids.append(vm[0])
    
    to_remove_dups = []
    while(len(duplicates) > len(vm_matches)):
        for dup in duplicates:
            if dup[0] not in vm_guids:
                to_remove_dups.append(duplicates.pop(0)[0])
                continue    
    
    for dup_guid in to_remove_dups:
        db.tri_world.execute_raw("DELETE FROM gameobject WHERE guid = %s", (dup_guid,))
                
    return 0 - len(to_remove_dups)

def update_instance_info():
    for instance_id in constants.NormalMaps:
        db.tri_world.upsert(
            db.UpsertQuery("gameobject").values({
                'spawnDifficulties': "0",
                "VerifiedBuild": constants.TargetBuild
            }).where("map", "=", instance_id)
        )
        
    for instance_id in constants.DungeonMaps:
        db.tri_world.upsert(
            db.UpsertQuery("gameobject").values({
                'spawnDifficulties': "1",
                "VerifiedBuild": constants.TargetBuild
            }).where("map", "=", instance_id)
        )

    for instance_id in constants.Raid20Maps:
        db.tri_world.upsert(
            db.UpsertQuery("gameobject").values({
                'spawnDifficulties': "148",
                "VerifiedBuild": constants.TargetBuild
            }).where("map", "=", instance_id)
        )
        
    for instance_id in constants.Raid40Maps:
        db.tri_world.upsert(
            db.UpsertQuery("gameobject").values({
                'spawnDifficulties': "9",
                "VerifiedBuild": constants.TargetBuild
            }).where("map", "=", instance_id)
        )