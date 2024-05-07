#!/usr/bin/python3

import constants
import database as db

def Import():
    clear_obsolete()
    
    tables = [
        'creature_loot_template',
        'disenchant_loot_template',
        'fishing_loot_template',
        'gameobject_loot_template',
        'item_loot_template',
        'mail_loot_template',
        'pickpocketing_loot_template',
        'reference_loot_template',
        'skinning_loot_template'
    ]
    
    for table in tables:
        handle_loot_table(table)

def clear_obsolete():
    db.tri_world.execute_raw("DELETE FROM milling_loot_template")
    db.tri_world.execute_raw("DELETE FROM prospecting_loot_template")
    db.tri_world.execute_raw("DELETE FROM spell_loot_template")
    
def handle_loot_table(table):
    db.tri_world.delete(
        db.DeleteQuery(table)
    )
    
    vm_rows = db.vm_world.select_chunked(
        db.SelectQuery(table).where('patch_max', "=", 10).order_by('entry ASC'),
        250
    )
    
    for vm_row in vm_rows:
        #TODO handle condition id.
        min_count = 1
        reference = 0
    
        if vm_row['mincountOrRef'] > 0:
            min_count = vm_row['mincountOrRef']
        else:
            reference = 0 - vm_row['mincountOrRef'] 
        
        insert = db.UpsertQuery(table).values({
            'Entry': vm_row['entry'],
            'Item': vm_row['item'],
            'Reference': reference,
            'Chance': abs(vm_row['ChanceOrQuestChance']),
            'QuestRequired': vm_row['ChanceOrQuestChance'] < 0, 
            'LootMode': 0x1, 
            'GroupId': vm_row['groupid'],
            'MinCount': min_count, 
            'MaxCount': vm_row['maxcount'],
            'Comment': None
        })
        
        try:
            db.tri_world.upsert(insert)
        except:
            continue    #TODO TC / VM tables have different keys.