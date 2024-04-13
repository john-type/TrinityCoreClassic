#!/usr/bin/python3

import constants
import database as db

#TODO

TRINITY_POOL_TYPE_CREATURE = 0
TRINITY_POOL_TYPE_GAMEOJECT = 1
TRINITY_POOL_TYPE_POOL = 2 

def Import():
    handle_pool_templates()
    handle_pool_members()
    
#TODO delete obsolete data
    
def handle_pool_templates():
    
    vm_rows = db.vm_world.get_rows("SELECT entry, max_limit, description FROM pool_template WHERE patch_max = 10")
    
    for vm_row in vm_rows:
       existing = db.tri_world.get_row("SELECT entry FROM pool_template WHERE entry = %s", (vm_row[0],))
       
       if existing == None:
            db.tri_world.execute((
            "INSERT INTO pool_template (entry, max_limit, description) "
            "VALUES (%s, %s, %s)"
            ), (vm_row[0], vm_row[1], vm_row[2],))
       else: 
           db.tri_world.execute(
               "UPDATE pool_template SET max_limit = %s, description=%s WHERE entry = %s",
               (vm_row[1], vm_row[2], vm_row[0],)
           )
           

    
def handle_pool_members():
    vm_member_pools = db.vm_world.get_rows("SELECT pool_id, mother_pool, chance, description FROM pool_pool")
    
    for vm_mp in vm_member_pools:
        _upsert_pool_member(TRINITY_POOL_TYPE_POOL, vm_mp[0], vm_mp[1], vm_mp[2], vm_mp[3])
        
        
    #TODO handle creatures
    #TODO handle game objects
    
            
def _upsert_pool_member(type, spawn_id, pool_spawn_id, chance, desc):
        existing = db.tri_world.get_row(
            "SELECT type FROM pool_members WHERE type = %s AND spawnId = %s AND poolSpawnId = %s", 
            (type, spawn_id, pool_spawn_id,)
            )
        
        if existing == None:
            db.tri_world.execute("INSERT INTO pool_members (type, spawnId, poolSpawnId, chance, description )",
                                 (type, spawn_id, pool_spawn_id, chance, desc,))
        else:
            db.tri_world.execute("UPDATE pool_members SET chance = %s, description = %s WHERE type = %s AND spawnId = %s AND poolSpawnId = %s",
                                 (chance, desc, type, spawn_id, pool_spawn_id,))
    