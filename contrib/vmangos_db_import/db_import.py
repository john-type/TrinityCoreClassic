#!/usr/bin/python3

import constants
import database as db
import mysql.connector
import importer.area
import importer.battleground
import importer.creature
import importer.gameobject
import importer.gossip
import importer.item
import importer.npc
import importer.player
import importer.quest
import importer.skill
import importer.spell
import importer.transport
import importer.cleanup

print("Starting VMangos -> Trinity DB Import...")

print("Opening DB...")
db.OpenAll()

print("Areas...")
importer.area.Import()

print("Battlegrounds...")
importer.battleground.Import()

print("Creatures...")
importer.creature.Import()

print("GameObjects...")
importer.gameobject.Import()

print("gossips...")
importer.gossip.Import()

print("Items...")
importer.item.Import()

print("NPCs...")
importer.npc.Import()

print("Players...")
importer.player.Import()

print("Quests...")
importer.quest.Import()

print("Skills...")
importer.skill.Import()

print("Spells...")
importer.spell.Import()

print("Transports...")
importer.transport.Import()

print("Cleanup...")
importer.cleanup.Clean()

print("Closing DB...")
db.CloseAll()

print("Done")


# TODO move into relevant importer files.

# print('Starting...')

# #TODO import player race stats

# def creatue_template_check_vmangos():
#     has_more = True
#     src_creature_query = ("SELECT entry, name FROM creature_template LIMIT 500 OFFSET %s") 
#     dest_creature_query = ("SELECT entry, name FROM creature_template "
#                     "WHERE entry = %s "
#                     "ORDER BY patch DESC LIMIT 1")
    
#     src_find_creature_query = ("SELECT guid FROM creature WHERE id = %s")
    
#     delete_src_creature_entity_queries = [
#         ("DELETE FROM creature_addon WHERE guid = %s"),
#         ("DELETE FROM creature_formations WHERE leaderGUID = %s"),
#         ("DELETE FROM creature_formations WHERE memberGUID = %s"),
#         ("DELETE FROM creature WHERE guid = %s"),
#     ]
    
#     delete_src_queries = [
#         ("DELETE FROM creature_equip_template WHERE CreatureID = %s"),
#         ("DELETE FROM creature_loot_template WHERE Entry = %s"),
#         ("DELETE FROM creature_onkill_reputation WHERE creature_id = %s"),
#         ("DELETE FROM creature_questender WHERE id = %s"),
#         ("DELETE FROM creature_questitem WHERE CreatureEntry = %s"),
#         ("DELETE FROM creature_queststarter WHERE id = %s"),
#         ("DELETE FROM creature_template_addon WHERE entry = %s"),
#         ("DELETE FROM creature_template_locale WHERE entry = %s"),
#         ("DELETE FROM creature_template_model WHERE CreatureID = %s"),
#         ("DELETE FROM creature_template_movement WHERE CreatureId = %s"),
#         ("DELETE FROM creature_template_resistance WHERE CreatureID = %s"),
#         ("DELETE FROM creature_template_scaling WHERE Entry = %s"),
#         ("DELETE FROM creature_template_spell WHERE CreatureID = %s"),
#         ("DELETE FROM creature_text WHERE CreatureID = %s"),
#         ("DELETE FROM creature_text_locale WHERE CreatureID = %s"),
#         ("DELETE FROM creature_template WHERE entry = %s"),
#     ]
    
#     offset = 0
#     missing = 0
#     name_mismatch = 0
    
#     while has_more:
#         tri_world_cur.execute(src_creature_query, (offset,))
#         results = tri_world_cur.fetchall()
        
#         for result in results:
#             vm_world_cur.execute(dest_creature_query,(result[0],))
#             match = vm_world_cur.fetchall()
            
#             if len(match) == 0:
                
#                 tri_world_cur.execute(src_find_creature_query, (result[0],))
#                 entities = tri_world_cur.fetchall()
                
#                 for entity in entities:
#                     for del_q in delete_src_creature_entity_queries:
#                         tri_world_cur.execute(del_q, (entity[0],))
                        
#                 for del_q in delete_src_queries:
#                     tri_world_cur.execute(del_q, (result[0],))
                    
#                 offset -= 1
#                 missing += 1
#                 trinity_world_con.commit()
#             else: 
                
#                 if match[0][1] != result[1]:
#                     name_mismatch += 1
                
        
#         offset = offset + 500  
#         has_more = len(results) > 0
        
#     print('missing')
#     print(missing)
    
#     print("name mismatch")
#     print(name_mismatch)
    
# def creature_check_vmangos():
#     has_more = True
#     src_creature_query = ("SELECT guid, id, map, position_x, position_y, position_z FROM creature LIMIT 500 OFFSET %s") 
#     dest_creature_query = ("SELECT guid, id, map, position_x, position_y, position_z FROM creature "
#                     "WHERE id = %s AND map = %s AND patch_max = 10")
    
#     delete_src_obj_creature_queries = [
#         ("DELETE FROM creature_addon WHERE guid = %s"),
#         ("DELETE FROM creature_formations WHERE leaderGUID = %s"),
#         ("DELETE FROM creature_formations WHERE memberGUID = %s"),
#         ("DELETE FROM creature WHERE guid = %s"),
#     ]
    
#     missing = 0
#     offset = 0
#     while has_more:
#         tri_world_cur.execute(src_creature_query, (offset,))
#         results = tri_world_cur.fetchall()
            
#         for result in results:
#             vm_world_cur.execute(dest_creature_query,(result[1],result[2]))
#             matches = vm_world_cur.fetchall()
#             matches_len = len(matches)
            
#             if(matches_len == 0):
#                 for del_q in delete_src_obj_creature_queries:
#                         tri_world_cur.execute(del_q, (result[0],))
                        
#                 offset -= 1
#                 missing += 1
#                 trinity_world_con.commit()
        
#         offset += 500
#         has_more = len(results) > 0
        
#     print("missing")
#     print(missing)

# def create_creature_template(vm_ct_id, tri_ct_id = None):
#     #TODO
#     return    

# def creature_template_update_against_vmangos():
#     has_more = True
#     src_ct_query = ("SELECT entry, name FROM creature_template LIMIT 1000 OFFSET %s") 
#     dest_ct_query = ("SELECT entry, name FROM creature_template "
#                     "WHERE entry = %s ")
#     missing = 0
#     simple_match = 0
#     name_mismatch = 0
#     offset = 0
#     while has_more:
#         vm_world_cur.execute(src_ct_query, (offset,))
#         results = vm_world_cur.fetchall()
            
#         for result in results:
#             tri_world_cur.execute(dest_ct_query,(result[0],))
#             matches = tri_world_cur.fetchall()
            
#             matches_len = len(matches)
#             if(matches_len == 0):
#                 missing += 1
#                 offset -= 1
#                 create_creature_template(result[0])
#             elif(matches_len == 1):
#                 simple_match += 1
#                 create_creature_template(result[0], matches[0][0])
        
#         offset += 1000
#         print(offset)
#         has_more = len(results) > 0
        
#     print("missing")
#     print(missing)
    
#     print("simple match")
#     print(simple_match)
    
#     print("name mismatch")
#     print(name_mismatch)
    
# def creatures_update_instance_info():
#     dest_update = 'UPDATE creature SET spawnDifficulties = "1,2", VerifiedBuild = 40618 WHERE map = %s'
#     for instance_id in DungeonMaps:
#         tri_world_cur.execute(dest_update, (instance_id,))
#         trinity_world_con.commit()
    
#     dest_update = 'UPDATE creature SET spawnDifficulties = "3,4,5,6,9,148", VerifiedBuild = 40618 WHERE map = %s'
#     for instance_id in RaidMaps:
#         tri_world_cur.execute(dest_update, (instance_id,))
#         trinity_world_con.commit()
        
#     #TODO BG maps (AV)

# # creatue_template_check_vmangos()
# # creature_check_vmangos()
# # TODO - not yet ran - creature_template_update_against_vmangos()

# creatures_update_instance_info()
    
# def gameobject_template_check_vmangos():
#     has_more = True
#     src_obj_query = ("SELECT entry, type, displayId, name FROM gameobject_template LIMIT 500 OFFSET %s") 
#     dest_obj_query = ("SELECT entry, type, displayId, name FROM gameobject_template "
#                     "WHERE entry = %s "
#                     "ORDER BY patch DESC LIMIT 1")
    
#     src_find_obj_query = ("SELECT guid FROM gameobject WHERE id = %s")
    
#     delete_src_obj_entity_queries = [
#         ("DELETE FROM gameobject_addon WHERE guid = %s"),
#         ("DELETE FROM game_event_gameobject WHERE guid = %s"),
#         ("DELETE FROM game_event_gameobject_quest WHERE id = %s"),
#         ("DELETE FROM gameobject WHERE guid = %s"),
#     ]
    
#     delete_src_queries = [
#         ("DELETE FROM gameobject_questender WHERE id = %s"),
#         ("DELETE FROM gameobject_questitem WHERE GameObjectEntry = %s"),
#         ("DELETE FROM gameobject_queststarter WHERE id = %s"),
#         ("DELETE FROM gameobject_loot_template WHERE entry = %s"),
#         ("DELETE FROM gameobject_template_locale WHERE entry = %s"),
#         ("DELETE FROM gameobject_template_addon WHERE entry = %s"),
#         ("DELETE FROM gameobject_template WHERE entry = %s")
#     ]
    
#     offset = 0
#     missing = 0
#     display_mismatch = 0
#     name_mismatch = 0
    
#     while has_more:
#         tri_world_cur.execute(src_obj_query, (offset,))
#         results = tri_world_cur.fetchall()
        
#         for result in results:
#             vm_world_cur.execute(dest_obj_query,(result[0],))
#             match = vm_world_cur.fetchall()
            
#             if len(match) == 0:
                
#                 tri_world_cur.execute(src_find_obj_query, (result[0],))
#                 entities = tri_world_cur.fetchall()
                
#                 for entity in entities:
#                     for del_q in delete_src_obj_entity_queries:
#                         tri_world_cur.execute(del_q, (entity[0],))
                        
#                 for del_q in delete_src_queries:
#                     tri_world_cur.execute(del_q, (result[0],))
                    
#                 offset -= 1
#                 missing += 1
#                 trinity_world_con.commit()
#             else: 
#                 if match[0][2] != result[2]:
#                     display_mismatch += 1
                
#                 if match[0][3] != result[3]:
#                     name_mismatch += 1
                
        
#         offset = offset + 500  
#         has_more = len(results) > 0

#     print('missing')
#     print(missing)
    
#     print("display mismatch")
#     print(display_mismatch)
    
#     print("name mismatch")
#     print(name_mismatch)

# def gameobject_check_vmangos():
#     has_more = True
#     src_obj_query = ("SELECT guid, id, map, position_x, position_y, position_z FROM gameobject LIMIT 500 OFFSET %s") 
#     dest_obj_query = ("SELECT guid, id, map, position_x, position_y, position_z FROM gameobject "
#                     "WHERE id = %s AND map = %s AND patch_max = 10")
    
#     delete_src_obj_entity_queries = [
#         ("DELETE FROM gameobject_addon WHERE guid = %s"),
#         ("DELETE FROM game_event_gameobject WHERE guid = %s"),
#         ("DELETE FROM game_event_gameobject_quest WHERE id = %s"),
#         ("DELETE FROM gameobject WHERE guid = %s"),
#     ]
    
#     #TODO gameobject_loot_template
    
#     missing = 0
#     offset = 0
#     while has_more:
#         tri_world_cur.execute(src_obj_query, (offset,))
#         results = tri_world_cur.fetchall()
            
#         for result in results:
#             vm_world_cur.execute(dest_obj_query,(result[1],result[2]))
#             matches = vm_world_cur.fetchall()
            
#             matches_len = len(matches)
            
#             if(matches_len == 0):
#                 for del_q in delete_src_obj_entity_queries:
#                         tri_world_cur.execute(del_q, (result[0],))
                        
#                 offset -= 1
#                 missing += 1
#                 trinity_world_con.commit()
        
#         offset += 500
#         has_more = len(results) > 0
        
#     print("missing")
#     print(missing)
    
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
    
# def gameobject_update_against_vmangos():
#     has_more = True
#     src_obj_query = ("SELECT guid, id, map, position_x, position_y, position_z FROM gameobject WHERE patch_max = 10 LIMIT 1000 OFFSET %s") 
#     dest_obj_query = ("SELECT guid, id, map, position_x, position_y, position_z FROM gameobject "
#                     "WHERE id = %s "
#                     "AND position_x BETWEEN %s AND %s "
#                     "AND position_y BETWEEN %s AND %s "
#                     "AND map = %s")
#     missing = 0
#     simple_match = 0
#     offset = 0
#     while has_more:
#         vm_world_cur.execute(src_obj_query, (offset,))
#         results = vm_world_cur.fetchall()
            
#         for result in results:
#             #TODO currently this requires to be ran multiple times, changing diff each time
#             diff = 5
#             tri_world_cur.execute(dest_obj_query,(
#                                     result[1],
#                                     result[3] - diff,
#                                     result[3] + diff,
#                                     result[4] - diff,
#                                     result[4] + diff,
#                                     result[2],
#                                    ))
#             matches = tri_world_cur.fetchall()
            
#             matches_len = len(matches)
#             if(matches_len == 0):
#                 missing += 1
#                 offset -= 1
#                 create_gameobject(result[0])
#             elif(matches_len == 1):
#                 simple_match += 1
#                 create_gameobject(result[0], matches[0][0])
#             else:
#                 continue
#                 # TODO handle multiple cases in a single zone.
         
        
#         offset += 1000
#         print(offset)
#         has_more = len(results) > 0
        
#     print("missing")
#     print(missing)
    
#     print("simple match")
#     print(simple_match)
    
    
# # gameobject_template_check_vmangos()
# # gameobject_check_vmangos()
# # gameobject_update_against_vmangos()
    
