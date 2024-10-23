#!/usr/bin/python3

import constants
import database as db

def Import():
    import_npc_text()
    import_vendors()
    
    
def import_npc_text():
    db.tri_world.execute_raw("DELETE FROM npc_text")
    
    vm_rows = db.vm_world.select_chunked(
        db.SelectQuery("npc_text").order_by("ID ASC"),
        500
    )
    
    for vm_row in vm_rows:
        vm_row['VerifiedBuild'] = constants.TargetBuild
        db.tri_world.upsert(
            db.UpsertQuery("npc_text").values(vm_row)
        )
        
def import_vendors():
    db.tri_world.execute_raw("DELETE FROM npc_vendor")
    
    _handle_vendor_templates()
    _handle_vendor_entries()
    
def _handle_vendor_templates():
    vm_vendor_entries = db.vm_world.select_all(
        db.SelectQuery("npc_vendor_template").select("entry").group_by("entry")
        )
    
    for vm_vendor_entry in vm_vendor_entries:
        vm_vendor_items = db.vm_world.select_all(
            db.SelectQuery("npc_vendor_template").where("entry", "=", vm_vendor_entry['entry'])
        )
        
        vm_creature_templates = db.vm_world.select_all(
            db.SelectQuery("creature_template").select("entry").where('vendor_id',"=", vm_vendor_entry['entry'])
        )     
        
        for vm_creature in vm_creature_templates:
            for vm_vendor_item in vm_vendor_items:
                _upsert_vendor_item(vm_creature['entry'], vm_vendor_item)
            

def _handle_vendor_entries():
    vm_rows = db.vm_world.select_chunked(
        db.SelectQuery("npc_vendor"),
        500
    )
    
    for vm_row in vm_rows:
        _upsert_vendor_item(vm_row['entry'], vm_row)
    
    
def _upsert_vendor_item(creature_id, vm_vendor_row):
    
    upsert = db.UpsertQuery("npc_vendor").values({
            'slot': vm_vendor_row['slot'],
            'maxcount': vm_vendor_row['maxcount'],
            'incrtime': vm_vendor_row['incrtime'],
            'ExtendedCost': 0,
            'type': 1, 
            'BonusListIDs': None,
            'PlayerConditionID': 0, #TODO
            'IgnoreFiltering': 1,
            'VerifiedBuild': constants.TargetBuild
        })
    #TODO vmangos itemflags
    
    match_existing = db.GroupCondition("AND").condition(
        'entry', "=", creature_id
    ).condition(
        'item', "=", vm_vendor_row['item']
    )
    
    existing = db.tri_world.select_one(
        db.SelectQuery("npc_vendor").where(match_existing)
    )
    
    if existing == None:
        upsert.values({
            'entry': creature_id,
            'item': vm_vendor_row['item'],
        })
    else:
        upsert.where(match_existing)
    
    
    db.tri_world.upsert(upsert)