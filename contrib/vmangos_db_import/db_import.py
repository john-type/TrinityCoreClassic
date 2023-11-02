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
    
    
remove_obsolete_area_triggers()
remove_obsolete_battleground_templates()
remove_obsolete_instances()

remove_obsolete_transports()    
# #TODO Clean up waypoint_data, waypoint scripts
remove_obsolete_world_safe_locs()
remove_obsolete_worldstates()
    
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
                    print(match[0][3])
                    print(result[3])
                    print('----')
                
        
        offset = offset + 500  
        has_more = len(results) > 0

    
    print('missing')
    print(missing)
    
    print("display mismatch")
    print(display_mismatch)
    
    print("name mismatch")
    print(name_mismatch)

    
gameobject_template_check_vmangos()
    
    
vm_world_cur.close()
tri_world_cur.close()

vmangos_world_con.close()
trinity_world_con.close()

print('done')