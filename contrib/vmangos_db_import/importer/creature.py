#!/usr/bin/python3

import constants
import database as db

next_entry_guid = 333000

imported_entry_guids = []

def Import():
    global next_entry_guid
    next_creature_row = db.tri_world.get_row_raw("SELECT MAX(guid) FROM creature")
    next_entry_guid = next_creature_row[0] + 1
    
    # clean_templates_check_vmangos()
    # clean_entries_check_vmangos()
    import_templates_vmangos()
    #import_entries_vmangos()
    #update_instance_info()

def clean_templates_check_vmangos():
    db.tri_world.chunk_raw(
        "SELECT entry, name FROM creature_template LIMIT %s OFFSET %s",
        500,
        _handle_clean_template_row
    )

def _handle_clean_template_row(row):
    
    dest_creature_query = ("SELECT entry, name FROM creature_template "
                    "WHERE entry = %s "
                    "ORDER BY patch DESC LIMIT 1")
    
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
    
    match = db.vm_world.get_rows_raw(dest_creature_query, (row[0],))
    
    if len(match) == 0:
        entities = db.tri_world.get_rows_raw("SELECT guid FROM creature WHERE id = %s", (row[0],))
        
        for entity in entities:
            db.tri_world.execute_many_raw(delete_src_creature_entity_queries, (entity[0],))      
                
        db.tri_world.execute_many_raw(delete_src_queries, (entity[0],))
            
        return -1
    
    return 0

def clean_entries_check_vmangos(): 
    db.tri_world.chunk_raw(
        "SELECT guid, id, map, position_x, position_y, position_z FROM creature LIMIT %s OFFSET %s",
        500,
        _handle_clean_entry_row
    )    
   
def _handle_clean_entry_row(row):
    dest_creature_query = ("SELECT guid, id, map, position_x, position_y, position_z FROM creature "
                    "WHERE id = %s AND map = %s AND patch_max = 10")
    
    delete_src_obj_creature_queries = [
        ("DELETE FROM creature_addon WHERE guid = %s"),
        ("DELETE FROM creature_formations WHERE leaderGUID = %s"),
        ("DELETE FROM creature_formations WHERE memberGUID = %s"),
        ("DELETE FROM creature WHERE guid = %s"),
    ]
    
    matches = db.vm_world.get_rows_raw(dest_creature_query, (row[1], row[2]))
    matches_len = len(matches)
    
    if(matches_len == 0):
        db.tri_world.execute_many_raw(delete_src_obj_creature_queries, (row[0],))                
        return -1
    
    return 0
     
def import_templates_vmangos():
    db.vm_world.chunk_raw(
        "SELECT entry, name FROM creature_template ORDER BY patch ASC LIMIT %s OFFSET %s",
        500,
        _handle_import_template_row
    )
    
def _handle_import_template_row(row):
    matches = db.tri_world.get_rows_raw(
        "SELECT entry, name FROM creature_template WHERE entry = %s ", 
        (row[0],)
    ) 
            
    matches_len = len(matches)
    if(matches_len == 0):
        _upsert_creature_template(row[0])
    elif(matches_len == 1):
        _upsert_creature_template(row[0], matches[0][0])

    return 0
                    

def import_entries_vmangos():
    db.vm_world.chunk_raw(
        "SELECT guid, id, map, position_x, position_y, position_z FROM creature WHERE patch_max = 10 LIMIT %s OFFSET %s",
        500,
        _handle_import_entry_row
    )

def _handle_import_entry_row(row):
    global imported_entry_guids
    
    exact_match = db.tri_world.get_row_raw("SELECT guid, id FROM creature WHERE guid = %s AND id = %s", (row[0], row[1],))
    if exact_match != None:
        _upsert_creature_entry(row[0], exact_match[0])
        return 0
    
    diff_sizes = [5, 10, 15, 20, 35, 50, 100]
    for diff in diff_sizes:  
        dest_ct_query = ("SELECT guid, id, map, position_x, position_y, position_z FROM creature "
                        "WHERE id = %s "
                        "AND position_x BETWEEN %s AND %s "
                        "AND position_y BETWEEN %s AND %s "
                        "AND map = %s")
        
        matches = db.tri_world.get_rows_raw(dest_ct_query, (
                                row[1],
                                row[3] - diff,
                                row[3] + diff,
                                row[4] - diff,
                                row[4] + diff,
                                row[2],
                                )) 
        
        for match in matches:
            if match[0] in imported_entry_guids:
                matches.remove(match)
        
        matches_len = len(matches)
        if(matches_len == 1):
            _upsert_creature_entry(row[0], matches[0][0])
            return 0
        elif(matches_len > 1):
            nearest_match = matches[0]
            nearest_abs = abs(matches[0][3] - row[3]) + abs(matches[0][4] - row[4])

            for near_match in matches:
                next_abs = abs(near_match[3] - row[3]) + abs(near_match[4] - row[4])
                if(next_abs < nearest_abs):
                    nearest_match = near_match
                    nearest_abs = next_abs
            
            _upsert_creature_entry(row[0], nearest_match[0])  
            return 0
        
    guid_missing = db.tri_world.get_row_raw("SELECT guid, id FROM creature WHERE guid = %s", (row[0],))
    if guid_missing == None:
        _upsert_creature_entry(row[0], 0 - row[0])
        return 0
    
    _upsert_creature_entry(row[0])
    return 0

def update_instance_info():
    dest_update = 'UPDATE creature SET spawnDifficulties = "1,2", VerifiedBuild = 40618 WHERE map = %s'
    for instance_id in constants.DungeonMaps:
        db.tri_world.execute_raw(dest_update, (instance_id,))
    
    dest_update = 'UPDATE creature SET spawnDifficulties = "3,4,5,6,9,148", VerifiedBuild = 40618 WHERE map = %s'
    for instance_id in constants.RaidMaps:
        db.tri_world.execute_raw(dest_update, (instance_id,))

def _upsert_creature_template(vm_ct_id, tri_ct_id = None) :
    vm_ct_row = db.vm_world.get_row_raw((
        "SELECT entry, level_min, level_max, faction, gold_min, gold_max, rank, "
        "display_id1, display_id2, display_id3, display_id4, "
        "display_scale1, display_scale2, display_scale3, display_scale4, "
        "display_probability1, display_probability2, display_probability3, display_probability4, "
        "name, subname, gossip_menu_id, npc_flags, speed_walk, speed_run, type, type_flags  "
        "FROM creature_template "
        "WHERE entry = %s "
        "ORDER BY patch DESC LIMIT 1"),
        (vm_ct_id,))
    
    if vm_ct_row == None:
        return
    
    if tri_ct_id == None:
        db.tri_world.execute_raw("INSERT INTO creature_template (entry) VALUES (%s)", (vm_ct_id,))
   
    update_template_query = ("UPDATE creature_template SET "
                                "minLevel = %s, maxLevel = %s, faction = %s, minGold = %s, maxGold = %s, rank = %s, VerifiedBuild = 40618,  "
                                "name = %s, subname = %s, gossip_menu_id = %s, npcflag = %s, speed_walk = %s, speed_run = %s, type = %s, type_flags = %s "
                                "WHERE entry = %s"
                                )
        
    type_flags = vm_ct_row[26]
    if vm_ct_row[21] > 0: #has gossip
        type_flags = type_flags | 0x08000000 #force gossip
        #TODO handle other trinity type flags.
    
    db.tri_world.execute_raw(update_template_query, (
            vm_ct_row[1],
            vm_ct_row[2],
            vm_ct_row[3],
            vm_ct_row[4],
            vm_ct_row[5],
            vm_ct_row[6],
            vm_ct_row[19],
            vm_ct_row[20],
            vm_ct_row[21],
            constants.ConvertNPCFlags(vm_ct_row[22]),
            vm_ct_row[23],
            vm_ct_row[24],
            vm_ct_row[25],
            type_flags,
            vm_ct_id,
        ))
    
    
    db.tri_world.execute_raw("DELETE FROM creature_template_model WHERE CreatureID = %s", (vm_ct_id,))
    
    displays = []
    
    if vm_ct_row[7] > 0:
        displays.append([vm_ct_row[7], vm_ct_row[11], vm_ct_row[15]])
        
    if vm_ct_row[8] > 0:
        displays.append([vm_ct_row[8], vm_ct_row[12], vm_ct_row[16]])
        
    if vm_ct_row[9] > 0:
        displays.append([vm_ct_row[9], vm_ct_row[13], vm_ct_row[17]])
            
    if vm_ct_row[10] > 0:
        displays.append([vm_ct_row[10], vm_ct_row[14], vm_ct_row[18]])
        
    display_index = 0
    for display in displays:
        db.tri_world.execute_raw("INSERT INTO creature_template_model ("
                             "CreatureID, Idx, CreatureDisplayID, DisplayScale, Probability, VerifiedBuild"
                             ") VALUES ("
                             "%s, %s, %s, %s, %s, 40618"
                             ")", (vm_ct_id, display_index, display[0], display[1], display[2],))
        display_index += 1
    
def _upsert_creature_entry(vm_ce_guid, tri_ce_guid = None):
    global next_entry_guid
    vm_row = db.vm_world.get_row_raw((
        "SELECT guid, id, "
        "map, position_x, position_y, position_z, orientation, "
        "spawntimesecsmin, wander_distance, movement_type  FROM creature WHERE guid = %s"
        ), (vm_ce_guid,))
    
    if vm_row == None:
        return
    
    if tri_ce_guid == None:
        tri_ce_guid = next_entry_guid
        next_entry_guid += 1
        db.tri_world.execute_raw("INSERT INTO creature (guid, id) VALUES (%s, %s)", (tri_ce_guid, vm_row[1],))
    elif tri_ce_guid < 0:
        tri_ce_guid = abs(tri_ce_guid)
        db.tri_world.execute_raw("INSERT INTO creature (guid, id) VALUES (%s, %s)", (tri_ce_guid, vm_row[1],))

    #TODO health / power / flags
    db.tri_world.execute_raw((
        "UPDATE creature SET "
        "map = %s, position_x = %s, position_y = %s, position_z = %s, orientation = %s, "
        "spawntimesecs = %s, wander_distance = %s, MovementType = %s, VerifiedBuild = 40618 "
        "WHERE guid = %s"
    ), (
        vm_row[2], vm_row[3], vm_row[4], vm_row[5], vm_row[6],
        vm_row[7], vm_row[8], vm_row[9],
        tri_ce_guid,
    )
    )
    
    global imported_entry_guids
    imported_entry_guids.append(tri_ce_guid)

    # check if is an event creature.
    event_rows = db.vm_world.get_rows_raw("SELECT guid, event FROM game_event_creature WHERE guid = %s", (vm_ce_guid,))
    matches_len = len(event_rows)
    
    if(matches_len > 0):
        match_row = event_rows[0]
        
        tri_event_rows = db.tri_world.get_rows_raw(
            "SELECT guid, eventEntry FROM game_event_creature WHERE guid = %s AND eventEntry = %s", 
            (tri_ce_guid, match_row[1],)
        )
        
        if(len(tri_event_rows) == 0):
            #TODO ensure event id's match between tri and vm.
            db.tri_world.execute_raw("INSERT INTO game_event_creature (guid, eventEntry) VALUES (%s, %s)", (tri_ce_guid, match_row[1],))
        
        