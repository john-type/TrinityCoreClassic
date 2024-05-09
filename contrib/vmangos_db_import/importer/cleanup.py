#!/usr/bin/python3

import constants
import database as db

def Clean():
    cleanBattlePets()
    cleanGarrison()
    cleanWorldStates()
    cleanVehicles()
    cleanDisables()
    cleanTeles()
    cleanAccessRequirements()
    cleanAchievements()
    cleanConversations()


def cleanBattlePets():
    queries = [
        "DELETE FROM battle_pet_breeds",
        "DELETE FROM battle_pet_quality"
    ]
    
    db.tri_world.execute_many_raw(queries)

    print("Cleaned battle pets")
    
def cleanGarrison():
    queries = [
        "DELETE FROM garrison_follower_class_spec_abilities",
        "DELETE FROM garrison_plot_finalize_info"
    ]
    
    db.tri_world.execute_many_raw(queries)
        
    print("Cleaned Garrisons")
    
def cleanWorldStates():
    rows = db.tri_world.get_rows_raw("SELECT * FROM world_state")
    for row in rows:
        map_ids = [0]
        if row[2] != None:
            map_ids = row[2].split(',')
        
        contains_valid_map = False
        for map_id in map_ids:
            if int(map_id) <= constants.MaxMapId:
                contains_valid_map = True
                break
        
        if contains_valid_map == False:
            db.tri_world.execute_raw("DELETE FROM world_state WHERE ID = %s", (row[0], ))
        
    print("Cleaned world states")
    
def cleanDisables():    
    db.vm_world.chunk_raw(
        "SELECT entry FROM spell_template LIMIT %s OFFSET %s",
        500,
        _handle_disable_spell
    )

    db.vm_world.chunk_raw(
        "SELECT entry FROM quest_template LIMIT %s OFFSET %s",
        500,
        _handle_disable_quest
    )
    
    #TODO handle other disable types.
    
    #TODO delete disables from obsolete expansions.
    


def _handle_disable_spell(row):
    db.tri_world.execute_raw("DELETE FROM disables WHERE sourceType = 0 AND entry = %s", (row[0],))
    return 0
    
def _handle_disable_quest(row):
    db.tri_world.execute_raw("DELETE FROM disables WHERE sourceType = 1 AND entry = %s", (row[0],))
    return 0

def cleanVehicles():
    db.tri_world.execute_raw("DELETE FROM vehicle_accessory")
    db.tri_world.execute_raw("DELETE FROM vehicle_seat_addon")
    db.tri_world.execute_raw("DELETE FROM vehicle_template")
    db.tri_world.execute_raw("DELETE FROM vehicle_template_accessory")
    
def cleanTeles():
    db.tri_world.delete(
        db.DeleteQuery("game_tele").where('map', '>', constants.MaxMapId)
    )
    
def cleanAccessRequirements():
    db.tri_world.delete(
        db.DeleteQuery("access_requirement").where('mapId', ">", constants.MaxMapId)
    )
    
def cleanAchievements():
    db.tri_world.execute_raw("DELETE FROM achievement_dbc")
    db.tri_world.execute_raw("DELETE FROM achievement_reward")
    db.tri_world.execute_raw("DELETE FROM achievement_reward_locale")
    db.tri_world.execute_raw("DELETE FROM achievement_scripts")
    
def cleanConversations():
    db.tri_world.execute_raw("DELETE FROM conversation_actors")
    db.tri_world.execute_raw("DELETE FROM conversation_line_template")
    db.tri_world.execute_raw("DELETE FROM conversation_template")