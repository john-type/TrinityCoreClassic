#!/usr/bin/python3

import constants
import database as db

#TODO#

def Clean():
    cleanBattlePets()
    cleanGarrison()
    cleanWorldStates()

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