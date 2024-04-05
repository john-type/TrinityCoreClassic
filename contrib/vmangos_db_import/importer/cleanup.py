#!/usr/bin/python3

import constants
import database as db

#TODO#

def Clean():
    # cleanBattlePets()
    # cleanGarrison()
    # cleanWorldStates()
    cleanDisables()

def cleanBattlePets():
    queries = [
        "DELETE FROM battle_pet_breeds",
        "DELETE FROM battle_pet_quality"
    ]
    
    db.tri_world.execute_many(queries)

    print("Cleaned battle pets")
    
def cleanGarrison():
    queries = [
        "DELETE FROM garrison_follower_class_spec_abilities",
        "DELETE FROM garrison_plot_finalize_info"
    ]
    
    db.tri_world.execute_many(queries)
        
    print("Cleaned Garrisons")
    
def cleanWorldStates():
    rows = db.tri_world.get_rows("SELECT * FROM world_state")
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
            db.tri_world.execute("DELETE FROM world_state WHERE ID = %s", (row[0], ))
        
    print("Cleaned world states")
    
def cleanDisables():    
    db.vm_world.chunk(
        "SELECT entry FROM spell_template LIMIT %s OFFSET %s",
        500,
        _handle_disable_spell
    )

    db.vm_world.chunk(
        "SELECT entry FROM quest_template LIMIT %s OFFSET %s",
        500,
        _handle_disable_quest
    )
    
    #TODO handle other disable types.
    
    #TODO delete disables from obsolete expansions.
    


def _handle_disable_spell(row):
    db.tri_world.execute("DELETE FROM disables WHERE sourceType = 0 AND entry = %s", (row[0],))
    return 0
    
def _handle_disable_quest(row):
    db.tri_world.execute("DELETE FROM disables WHERE sourceType = 1 AND entry = %s", (row[0],))
    return 0