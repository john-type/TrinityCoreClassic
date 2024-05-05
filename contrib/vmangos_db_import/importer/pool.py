#!/usr/bin/python3

import constants
import database as db

TRINITY_POOL_TYPE_CREATURE = 0
TRINITY_POOL_TYPE_GAMEOJECT = 1
TRINITY_POOL_TYPE_POOL = 2 

def Import():
    handle_pool_templates()
    handle_pool_members()
    
#TODO delete obsolete data
    
def handle_pool_templates():
    
    vm_rows = db.vm_world.get_rows_raw("SELECT entry, max_limit, description FROM pool_template WHERE patch_max = 10")
    
    for vm_row in vm_rows:
       existing = db.tri_world.get_row_raw("SELECT entry FROM pool_template WHERE entry = %s", (vm_row[0],))
       
       if existing == None:
            db.tri_world.execute_raw((
            "INSERT INTO pool_template (entry, max_limit, description) "
            "VALUES (%s, %s, %s)"
            ), (vm_row[0], vm_row[1], vm_row[2],))
       else: 
           db.tri_world.execute_raw(
               "UPDATE pool_template SET max_limit = %s, description=%s WHERE entry = %s",
               (vm_row[1], vm_row[2], vm_row[0],)
           )
           

    
def handle_pool_members():
    vm_member_pools = db.vm_world.select_all(
        db.SelectQuery("pool_pool")
    )
    
    for vm_mp in vm_member_pools:
        _upsert_pool_member(TRINITY_POOL_TYPE_POOL, vm_mp['pool_id'], vm_mp['mother_pool'], vm_mp['chance'], vm_mp['description'])
    
    
    #TODO handle creature template and GO template pools.
    
    vm_creature_pools = db.vm_world.select_chunked(
        db.SelectQuery("pool_creature").order_by("guid ASC, pool_entry ASC"),
        250
    )
    
    for vm_cp in vm_creature_pools:
        _upsert_pool_member(TRINITY_POOL_TYPE_CREATURE, vm_cp['guid'], vm_cp['pool_entry'], vm_cp['chance'], vm_cp['description'])
    
    vm_go_pools = db.vm_world.select_chunked(
        db.SelectQuery("pool_gameobject").order_by("guid ASC, pool_entry ASC"),
        250
    )
    
    for vm_gp in vm_go_pools:
        _upsert_pool_member(TRINITY_POOL_TYPE_GAMEOJECT, vm_gp['guid'], vm_gp['pool_entry'], vm_gp['chance'], vm_gp['description'])

    
            
def _upsert_pool_member(type, spawn_id, pool_spawn_id, chance, desc):   
    existing = db.tri_world.get_row_raw(
        "SELECT type FROM pool_members WHERE type = %s AND spawnId = %s", 
        (type, spawn_id,)
        )
    
    if existing == None:
        db.tri_world.upsert(
            db.UpsertQuery("pool_members").values({
                'type': type,
                'spawnId': spawn_id,
                'poolSpawnId': pool_spawn_id,
                'chance': chance,
                'description': desc
            })
        )
    else:
        db.tri_world.upsert(
            db.UpsertQuery("pool_members").values({
                'chance': chance,
                'description': desc,
                'poolSpawnId': pool_spawn_id
            }).where(
                db.GroupCondition("AND")
                    .condition("type", "=", type)
                    .condition("spawnId", "=", spawn_id)
            )
        )

    