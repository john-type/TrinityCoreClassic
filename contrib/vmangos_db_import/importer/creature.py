#!/usr/bin/python3

import constants
import database as db

def Import():
    clean_templates_check_vmangos()
    clean_entries_check_vmangos()
    import_templates_vmangos()
    import_entries_vmangos()
    update_instance_info()

def clean_templates_check_vmangos():
    has_more = True
    src_creature_query = ("SELECT entry, name FROM creature_template LIMIT 500 OFFSET %s") 
    dest_creature_query = ("SELECT entry, name FROM creature_template "
                    "WHERE entry = %s "
                    "ORDER BY patch DESC LIMIT 1")
    
    src_find_creature_query = ("SELECT guid FROM creature WHERE id = %s")
    
    delete_src_creature_entity_queries = [
        ("DELETE FROM creature_addon WHERE guid = %s"),
        ("DELETE FROM creature_formations WHERE leaderGUID = %s"),
        ("DELETE FROM creature_formations WHERE memberGUID = %s"),
        ("DELETE FROM creature WHERE guid = %s"),
    ]
    
    delete_src_queries = [
        ("DELETE FROM creature_equip_template WHERE CreatureID = %s"),
        ("DELETE FROM creature_loot_template WHERE Entry = %s"),
        ("DELETE FROM creature_onkill_reputation WHERE creature_id = %s"),
        ("DELETE FROM creature_questender WHERE id = %s"),
        ("DELETE FROM creature_questitem WHERE CreatureEntry = %s"),
        ("DELETE FROM creature_queststarter WHERE id = %s"),
        ("DELETE FROM creature_template_addon WHERE entry = %s"),
        ("DELETE FROM creature_template_locale WHERE entry = %s"),
        ("DELETE FROM creature_template_model WHERE CreatureID = %s"),
        ("DELETE FROM creature_template_movement WHERE CreatureId = %s"),
        ("DELETE FROM creature_template_resistance WHERE CreatureID = %s"),
        ("DELETE FROM creature_template_scaling WHERE Entry = %s"),
        ("DELETE FROM creature_template_spell WHERE CreatureID = %s"),
        ("DELETE FROM creature_text WHERE CreatureID = %s"),
        ("DELETE FROM creature_text_locale WHERE CreatureID = %s"),
        ("DELETE FROM creature_template WHERE entry = %s"),
    ]
    
    offset = 0
    
    while has_more:
        results = db.GetRows(src_creature_query, 'tri_world', (offset,))
        
        for result in results:
            match = db.GetRows(dest_creature_query, 'vm_world',(result[0],))
            
            if len(match) == 0:
                entities = db.GetRows(src_find_creature_query, 'tri_world', (result[0],))
                
                for entity in entities:
                    for del_q in delete_src_creature_entity_queries:
                        db.Execute(del_q, 'tri_world', (entity[0],))
                        
                for del_q in delete_src_queries:
                    db.Execute(del_q, 'tri_world', (entity[0],))
                    
                offset -= 1
                
        offset = offset + 500  
        has_more = len(results) > 0

def clean_entries_check_vmangos():
    has_more = True
    src_creature_query = ("SELECT guid, id, map, position_x, position_y, position_z FROM creature LIMIT 500 OFFSET %s") 
    dest_creature_query = ("SELECT guid, id, map, position_x, position_y, position_z FROM creature "
                    "WHERE id = %s AND map = %s AND patch_max = 10")
    
    delete_src_obj_creature_queries = [
        ("DELETE FROM creature_addon WHERE guid = %s"),
        ("DELETE FROM creature_formations WHERE leaderGUID = %s"),
        ("DELETE FROM creature_formations WHERE memberGUID = %s"),
        ("DELETE FROM creature WHERE guid = %s"),
    ]
    
    offset = 0
    while has_more:
        results = db.GetRows(src_creature_query, 'tri_world',  (offset,))
            
        for result in results:
            matches = db.GetRows(dest_creature_query, 'vm_world', (result[1],result[2]))
            matches_len = len(matches)
            
            if(matches_len == 0):
                for del_q in delete_src_obj_creature_queries:
                    db.Execute(del_q, 'tri_world', (result[0],))
                        
                offset -= 1
        
        offset += 500
        has_more = len(results) > 0
        
def import_templates_vmangos():
    has_more = True
    src_ct_query = ("SELECT entry, name FROM creature_template LIMIT 1000 OFFSET %s") 
    dest_ct_query = ("SELECT entry, name FROM creature_template "
                    "WHERE entry = %s ")
    offset = 0
    while has_more:
        results = db.GetRows(src_ct_query, 'vm_world', (offset,))
            
        for result in results:
            matches = db.GetRows(dest_ct_query, 'tri_world', (result[0],)) 
            
            matches_len = len(matches)
            if(matches_len == 0):
                _upsert_creature_template(result[0])
            elif(matches_len == 1):
                _upsert_creature_template(result[0], matches[0][0])
        
        offset += 1000
        has_more = len(results) > 0

def import_entries_vmangos():
    has_more = True
    src_ct_query = ("SELECT guid, id, map, position_x, position_y, position_z FROM creature WHERE id = 15892 LIMIT 1000 OFFSET %s") 
    dest_ct_query = ("SELECT guid, id, map, position_x, position_y, position_z FROM creature "
                    "WHERE id = %s "
                    "AND position_x BETWEEN %s AND %s "
                    "AND position_y BETWEEN %s AND %s "
                    "AND map = %s")
    offset = 0
    while has_more:
        results = db.GetRows(src_ct_query, 'vm_world', (offset,))
        
        for result in results:
            diff = 5
            matches = db.GetRows(dest_ct_query, 'tri_world', (
                                    result[1],
                                    result[3] - diff,
                                    result[3] + diff,
                                    result[4] - diff,
                                    result[4] + diff,
                                    result[2],
                                   )) 
            
            matches_len = len(matches)
            if(matches_len == 0):
                _upsert_creature_entry(result[0])
            elif(matches_len == 1):
                _upsert_creature_entry(result[0], matches[0][0])
            elif(matches_len > 1):
                nearest_match = matches[0]
                nearest_abs = abs(matches[0][3] - result[3]) + abs(matches[0][4] - result[4])

                for near_match in matches:
                    next_abs = abs(near_match[3] - result[3]) + abs(near_match[4] - result[4])
                    if(next_abs < nearest_abs):
                        nearest_match = near_match
                        nearest_abs = next_abs
                
                _upsert_creature_entry(result[0], nearest_match[0])                        
        
        offset += 1000
        has_more = len(results) > 0

def update_instance_info():
    dest_update = 'UPDATE creature SET spawnDifficulties = "1,2", VerifiedBuild = 40618 WHERE map = %s'
    for instance_id in constants.DungeonMaps:
        db.Execute(dest_update, 'tri_world', (instance_id,))
    
    dest_update = 'UPDATE creature SET spawnDifficulties = "3,4,5,6,9,148", VerifiedBuild = 40618 WHERE map = %s'
    for instance_id in constants.RaidMaps:
        db.Execute(dest_update, 'tri_world', (instance_id,))

def _upsert_creature_template(vm_ct_id, tri_ct_id = None) :
    if tri_ct_id == None:
        #TODO handle inserts.
        return
    
    #TODO
    
    
def _upsert_creature_entry(vm_ce_guid, tri_ce_guid = None):
    if tri_ce_guid == None:
        #TODO handle inserts.
        return
    
    #TODO

    # check if is an event creature.
    vm_event_check = "SELECT guid, event FROM game_event_creature WHERE guid = %s"
    event_rows = db.GetRows(vm_event_check, 'vm_world', (vm_ce_guid,))
    matches_len = len(event_rows)
    
    if(matches_len > 0):
        match_row = event_rows[0]
    
        tri_event_check = "SELECT guid, eventEntry FROM game_event_creature WHERE guid = %s AND eventEntry = %s"
        tri_event_rows = db.GetRows(tri_event_check, 'tri_world', (tri_ce_guid, match_row[1],))
        
        if(len(tri_event_rows) == 0):
            #TODO ensure event id's match between tri and vm.
            tri_event_insert = "INSERT INTO game_event_creature (guid, eventEntry) VALUES (%s, %s)"
            db.Execute(tri_event_insert, 'tri_world', (tri_ce_guid, match_row[1],))
        