#!/usr/bin/python3

import mysql.connector

target_build = 40618

vmangos_world_con = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='vmangos_mangos'
)

trinity_world_con = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='trinity_world'
)

vm_world_cur = vmangos_world_con.cursor()
tri_world_cur = trinity_world_con.cursor()

print('Starting...')

#TODO import player race stats


def remove_obsolete_area_triggers():
    print('Area triggers...')
    query = 'DELETE FROM areatrigger WHERE SpawnId >= 4'
    tri_world_cur.execute(query)
    query2 = 'DELETE FROM areatrigger_template_actions WHERE AreaTriggerId >= 4'
    tri_world_cur.execute(query2)
    query3 = 'DELETE FROM areatrigger_tavern WHERE id >= 4753'
    tri_world_cur.execute(query3)
    trinity_world_con.commit()

    
def remove_obsolete_battleground_templates():
    print('Battlegrounds...')
    query = 'DELETE FROM battleground_template WHERE ID >= 4'
    tri_world_cur.execute(query)
    query2 = 'DELETE FROM battlemaster_entry WHERE bg_template >= 4'
    tri_world_cur.execute(query2)
    trinity_world_con.commit()

def remove_obsolete_instances():
    delete_instance = "DELETE FROM instance_template WHERE map >= 534"
    tri_world_cur.execute(delete_instance)
    trinity_world_con.commit()

def remove_obsolete_transports():
    print('Transports...')
    query = 'DELETE FROM transports WHERE guid >= 9'
    tri_world_cur.execute(query)  
    trinity_world_con.commit()

def remove_obsolete_world_safe_locs():
    print('safe locs')
    query = 'DELETE FROM world_safe_locs WHERE MapID > 533'
    tri_world_cur.execute(query)  
    trinity_world_con.commit() 

def remove_obsolete_worldstates():
    print('world states...')
    query = 'DELETE FROM world_state WHERE ID >= 2400'
    tri_world_cur.execute(query)
    trinity_world_con.commit()
    
    
# remove_obsolete_area_triggers()
# remove_obsolete_battleground_templates()
# remove_obsolete_instances()

# remove_obsolete_transports()    
# # #TODO Clean up waypoint_data, waypoint scripts
# remove_obsolete_world_safe_locs()
# remove_obsolete_worldstates()
    
def gameobject_template_check_vmangos():
    has_more = True
    src_obj_query = ("SELECT entry, type, displayId, name FROM gameobject_template LIMIT 500 OFFSET %s") 
    dest_obj_query = ("SELECT entry, type, displayId, name FROM gameobject_template "
                    "WHERE entry = %s "
                    "ORDER BY patch DESC LIMIT 1")
    
    src_find_obj_query = ("SELECT guid FROM gameobject WHERE id = %s")
    
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
    
    offset = 0
    missing = 0
    display_mismatch = 0
    name_mismatch = 0
    
    while has_more:
        tri_world_cur.execute(src_obj_query, (offset,))
        results = tri_world_cur.fetchall()
        
        for result in results:
            vm_world_cur.execute(dest_obj_query,(result[0],))
            match = vm_world_cur.fetchall()
            
            if len(match) == 0:
                
                tri_world_cur.execute(src_find_obj_query, (result[0],))
                entities = tri_world_cur.fetchall()
                
                for entity in entities:
                    for del_q in delete_src_obj_entity_queries:
                        tri_world_cur.execute(del_q, (entity[0],))
                        
                for del_q in delete_src_queries:
                    tri_world_cur.execute(del_q, (result[0],))
                    
                offset -= 1
                missing += 1
                trinity_world_con.commit()
            else: 
                if match[0][2] != result[2]:
                    display_mismatch += 1
                
                if match[0][3] != result[3]:
                    name_mismatch += 1
                
        
        offset = offset + 500  
        has_more = len(results) > 0

    print('missing')
    print(missing)
    
    print("display mismatch")
    print(display_mismatch)
    
    print("name mismatch")
    print(name_mismatch)

def gameobject_check_vmangos():
    has_more = True
    src_obj_query = ("SELECT guid, id, map, position_x, position_y, position_z FROM gameobject LIMIT 500 OFFSET %s") 
    dest_obj_query = ("SELECT guid, id, map, position_x, position_y, position_z FROM gameobject "
                    "WHERE id = %s AND map = %s AND patch_max = 10")
    
    delete_src_obj_entity_queries = [
        ("DELETE FROM gameobject_addon WHERE guid = %s"),
        ("DELETE FROM game_event_gameobject WHERE guid = %s"),
        ("DELETE FROM game_event_gameobject_quest WHERE id = %s"),
        ("DELETE FROM gameobject WHERE guid = %s"),
    ]
    
    #TODO gameobject_loot_template
    
    missing = 0
    offset = 0
    while has_more:
        tri_world_cur.execute(src_obj_query, (offset,))
        results = tri_world_cur.fetchall()
            
        for result in results:
            vm_world_cur.execute(dest_obj_query,(result[1],result[2]))
            matches = vm_world_cur.fetchall()
            
            matches_len = len(matches)
            
            if(matches_len == 0):
                for del_q in delete_src_obj_entity_queries:
                        tri_world_cur.execute(del_q, (result[0],))
                        
                offset -= 1
                missing += 1
                trinity_world_con.commit()
        
        offset += 500
        has_more = len(results) > 0
        
    print("missing")
    print(missing)
    
def create_gameobject(vm_go_guid, tri_go_guid = None):
    src_query = "SELECT * FROM gameobject WHERE guid = %s"
    vm_world_cur.execute(src_query, (vm_go_guid,))
    result = vm_world_cur.fetchone()
    
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
    
    if(tri_go_guid == None):
        tri_world_cur.execute(dest_insert, (
            result[1], result[2], 
            result[3], result[4], result[5], result[6], result[7], result[8], result[9], result[10],
            result[11], result[13], result[14],
        ))
    else:
         tri_world_cur.execute(dest_update, (
            result[3], result[4], result[5], result[6], result[7], result[8], result[9], result[10],
            result[11], result[13], result[14],
           result[0] 
        ))
    
    trinity_world_con.commit()
    
def gameobject_update_against_vmangos():
    has_more = True
    src_obj_query = ("SELECT guid, id, map, position_x, position_y, position_z FROM gameobject WHERE patch_max = 10 LIMIT 1000 OFFSET %s") 
    dest_obj_query = ("SELECT guid, id, map, position_x, position_y, position_z FROM gameobject "
                    "WHERE id = %s "
                    "AND position_x BETWEEN %s AND %s "
                    "AND position_y BETWEEN %s AND %s "
                    "AND map = %s")
    missing = 0
    simple_match = 0
    offset = 0
    while has_more:
        vm_world_cur.execute(src_obj_query, (offset,))
        results = vm_world_cur.fetchall()
            
        for result in results:
            #TODO currently this requires to be ran multiple times, changing diff each time
            diff = 5
            tri_world_cur.execute(dest_obj_query,(
                                    result[1],
                                    result[3] - diff,
                                    result[3] + diff,
                                    result[4] - diff,
                                    result[4] + diff,
                                    result[2],
                                   ))
            matches = tri_world_cur.fetchall()
            
            matches_len = len(matches)
            if(matches_len == 0):
                missing += 1
                offset -= 1
                create_gameobject(result[0])
            elif(matches_len == 1):
                simple_match += 1
                create_gameobject(result[0], matches[0][0])
            else:
                continue
                # TODO handle multiple cases in a single zone.
         
        
        offset += 1000
        print(offset)
        has_more = len(results) > 0
        
    print("missing")
    print(missing)
    
    print("simple match")
    print(simple_match)
    
    
# gameobject_template_check_vmangos()
# gameobject_check_vmangos()
# gameobject_update_against_vmangos()
    
vm_world_cur.close()
tri_world_cur.close()

vmangos_world_con.close()
trinity_world_con.close()

print('done')