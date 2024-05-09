#!/usr/bin/python3

import constants
import database as db


def Import():
    db.tri_world.execute_raw("DELETE FROM game_event")
    db.tri_world.execute_raw("DELETE FROM game_event_arena_seasons")
    db.tri_world.execute_raw("DELETE FROM game_event_battleground_holiday")
    db.tri_world.execute_raw("DELETE FROM game_event_condition")
    db.tri_world.execute_raw("DELETE FROM game_event_creature")
    db.tri_world.execute_raw("DELETE FROM game_event_creature_quest")
    db.tri_world.execute_raw("DELETE FROM game_event_gameobject")
    db.tri_world.execute_raw("DELETE FROM game_event_model_equip")
    db.tri_world.execute_raw("DELETE FROM game_event_npcflag")
    db.tri_world.execute_raw("DELETE FROM game_event_npc_vendor")
    db.tri_world.execute_raw("DELETE FROM game_event_pool")
    db.tri_world.execute_raw("DELETE FROM game_event_prerequisite")
    db.tri_world.execute_raw("DELETE FROM game_event_quest_condition")
    db.tri_world.execute_raw("DELETE FROM game_event_seasonal_questrelation")
    
    vm_rows = db.vm_world.select_all(
        db.SelectQuery("game_event").where(
            db.GroupCondition("AND").condition(
                'patch_max', "=", 10
            ).condition(
                'disabled', '=', 0
            )
        )
    )
    
    for vm_row in vm_rows:
        upsert = db.UpsertQuery("game_event").values({
            'eventEntry': vm_row['entry'],
            'start_time': vm_row['start_time'],
            'end_time': vm_row['end_time'],
            'occurence': vm_row['occurence'],
            'length': vm_row['length'],
            'holiday': vm_row['holiday'],
            'holidayStage': 0,  #TODO CHECK
            'description': vm_row['description'],
            'world_event': 0,
            'announce': 2
        })
        
        db.tri_world.upsert(upsert)
        
    vm_rows = db.vm_world.select_all(
        db.SelectQuery("game_event_quest")
    )
    
    for vm_row in vm_rows:
        db.tri_world.upsert(
            db.UpsertQuery("game_event_seasonal_questrelation").values({
                'questId': vm_row['quest'],
                'eventEntry': vm_row['event']
            })
        )