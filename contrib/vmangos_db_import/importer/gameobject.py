#!/usr/bin/python3

import constants
import database as db

def Import():
    # clean_templates_check_vmangos()
    # clean_entries_check_vmangos()
    # import_templates_vmangos()
    # import_entries_vmangos()
    remove_duplicate_entries()

    
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
    db.vm_world.chunk_raw(
        ("SELECT entry, type, displayId, name, size, "
         "data0, data1, data2, data3, data4, data5, data6, data7, data8, data9, "
         "data10, data11, data12, data13, data14, data15, data16, data17, data18, data19, "
         "data20, data21, data22, data23, faction, flags, mingold, maxgold "
         "FROM gameobject_template GROUP BY entry LIMIT %s OFFSET %s"),
        500,
        _handle_import_template_row
    )

def _handle_import_template_row(row):
    dest_template_query = "SELECT entry, type, displayid, name FROM gameobject_template WHERE entry = %s"
    
    match_row = db.tri_world.get_row_raw(dest_template_query, (row[0],))
    
    if(match_row == None):
        _upsert_gameobject_template(row)
    else: 
        _upsert_gameobject_template(row, match_row)
    
    return 0

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
    if tri_got == None:
        #TODO handle inserts
        return
    
    #confirm safe type conversions
    safe = vm_got[1] == tri_got[1] or \
        (vm_got[1] == 3 and tri_got[1] == 50)   # gather_node -> chest
    
    if safe == False:
        return 
    
    update_query = ("UPDATE gameobject_template SET "
    "type = %s, "
    "displayId = %s, "
    "name = %s, "
    "size = %s, "
    "Data0 = %s, Data1 = %s, Data2 = %s, Data3 = %s, Data4 = %s, Data5 = %s, "
    "Data6 = %s, Data7 = %s, Data8 = %s, Data9 = %s, Data10 = %s, "
    "Data11 = %s, Data12 = %s, Data13 = %s, Data14 = %s, Data15 = %s, "
    "Data16 = %s, Data17 = %s, Data18 = %s, Data19 = %s, Data20 = %s, "
    "Data21 = %s, Data22 = %s, Data23 = %s, VerifiedBuild = 40618, ContentTuningId = 0 "
    "WHERE entry = %s"
    )
    
    db.tri_world.execute_raw(update_query, (
        vm_got[1],
        vm_got[2],
        vm_got[3],
        vm_got[4], #size
        vm_got[5], vm_got[6], vm_got[7], vm_got[8], vm_got[9],
        vm_got[10], vm_got[11], vm_got[12], vm_got[13], vm_got[14],
        vm_got[15], vm_got[16], vm_got[17], vm_got[18], vm_got[19],
        vm_got[20], vm_got[21], vm_got[22], vm_got[23], vm_got[24],
        vm_got[25], vm_got[26], vm_got[27], vm_got[28],
        vm_got[0] #entry
    ,))
    
    existing_addon = db.tri_world.get_row_raw("SELECT entry, flags FROM gameobject_template_addon WHERE entry = %s", (vm_got[0],))
    # faction = vm_got[29]
        
    if existing_addon == None:
        db.tri_world.execute_raw((
            "INSERT INTO gameobject_template_addon ("
            "entry, faction, flags, mingold, maxgold, "
            "artkit0, artkit1, artkit2, artkit3, artkit4, WorldEffectID, AIAnimKitID"
            ") VALUES ("
            "%s, %s, %s, %s, %s, "
            "0, 0, 0, 0, 0, 0, 0"
            ")"
            ),(
                vm_got[0],
                vm_got[29],
                vm_got[30],
                vm_got[31],
                vm_got[32]
            ,))
    else:
        db.tri_world.execute_raw((
            "UPDATE gameobject_template_addon SET "
            "faction = %s, flags = %s, mingold = %s, maxgold = %s "
            "WHERE entry = %s"
            ),(
                vm_got[29],
                vm_got[30],
                vm_got[31],
                vm_got[32],
                vm_got[0]
            ,))
    
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