#!/usr/bin/python3

import constants
import database as db

def Import():
    clean_templates_check_vmangos()
    clean_entries_check_vmangos()
    import_templates_vmangos()
    import_entries_vmangos()
    
    
def clean_templates_check_vmangos():
    db.tri_world.chunk(
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
    
    match = db.vm_world.get_rows(dest_obj_query, (row[0],))
            
    if len(match) == 0:
        entities = db.tri_world.get_rows("SELECT guid FROM gameobject WHERE id = %s", (row[0],))
        for entity in entities:
            db.tri_world.execute_many(delete_src_obj_entity_queries, (entity[0],))
            
        db.tri_world.execute_many(delete_src_queries, (row[0],))
        return -1

    return 0

def clean_entries_check_vmangos():
    db.tri_world.chunk(
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
    
    matches = db.wm_world.get_rows(dest_obj_query, (row[1],row[2],))
    matches_len = len(matches)

    if(matches_len == 0):
        db.tri_world.execute_many(delete_src_obj_entity_queries, (row[0],))
        return -1
    
    return 0
        
def import_templates_vmangos():
    pass #TODO

def _handle_import_template_row(row):
    pass #TODO

def import_entries_vmangos():
    db.vm_world.chunk(
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
    matches = db.tri_world.get_rows(dest_obj_query, (
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
         

def _upsert_gameobject_template(vm_got_id, tri_got_id = None) :
    pass #TODO
    
def _upsert_gameobject_entry(vm_go_guid, tri_go_guid = None):
    if tri_go_guid == None:
        #TODO handle inserts.
        return
    
    #TODO

    # check if is an event creature.
    event_rows = db.vm_world.get_rows(
        "SELECT guid, event FROM game_event_gameobject WHERE guid = %s", 
        (vm_go_guid,)
    )
    matches_len = len(event_rows)
    
    if(matches_len > 0):
        match_row = event_rows[0]
         
        tri_event_rows = db.tri_world.get_rows(
            "SELECT guid, eventEntry FROM game_event_gameobject WHERE guid = %s AND eventEntry = %s"
            (tri_go_guid, match_row[1],)
        )
        
        if(len(tri_event_rows) == 0):
            #TODO ensure event id's match between tri and vm.
            db.tri_world.execute(
                "INSERT INTO game_event_gameobject (guid, eventEntry) VALUES (%s, %s)", 
                (tri_go_guid, match_row[1],)
            )
        
        
# def create_gameobject(vm_go_guid, tri_go_guid = None):
#     src_query = "SELECT * FROM gameobject WHERE guid = %s"
#     vm_world_cur.execute(src_query, (vm_go_guid,))
#     result = vm_world_cur.fetchone()
    
#     dest_insert = (
#         "INSERT INTO gameobject ("
#         "id, map, zoneId, areaId, spawnDifficulties, phaseUseFlags, PhaseId, PhaseGroup, terrainSwapMap, "
#         "position_x, position_y, position_z, orientation, rotation0, rotation1, rotation2, rotation3, "
#         "spawntimesecs, animprogress, state, ScriptName, VerifiedBuild"
#         ") VALUES ("
#         "%s, %s, 0, 0, 0, 0, 0, 0, -1, "
#         "%s, %s, %s, %s, %s, %s, %s, %s,"
#         "%s, %s, %s, \"\", 40618"
#         ")"
#         )
    
#     dest_update = (
#         "UPDATE gameobject SET "
#         "position_x = %s, position_y = %s, position_z=%s, orientation=%s, rotation0=%s, rotation1=%s, rotation2=%s, rotation3=%s, "
#         "spawntimesecs = %s, animprogress=%s, state = %s, VerifiedBuild = 40618 "
#         "WHERE guid = %s"
#     )
    
#     if(tri_go_guid == None):
#         tri_world_cur.execute(dest_insert, (
#             result[1], result[2], 
#             result[3], result[4], result[5], result[6], result[7], result[8], result[9], result[10],
#             result[11], result[13], result[14],
#         ))
#     else:
#          tri_world_cur.execute(dest_update, (
#             result[3], result[4], result[5], result[6], result[7], result[8], result[9], result[10],
#             result[11], result[13], result[14],
#            result[0] 
#         ))
    
#     trinity_world_con.commit()