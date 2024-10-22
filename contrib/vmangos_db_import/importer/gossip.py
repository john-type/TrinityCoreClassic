#!/usr/bin/python3

import constants
import database as db

def Import():
    import_gossip_menus()
    db.tri_world.execute_raw("DELETE FROM gossip_menu_addon")
    import_gossip_menu_options()
    

def import_gossip_menus():
    db.tri_world.execute_raw("DELETE FROM gossip_menu")
    db.vm_world.chunk_raw(
        "SELECT entry, text_id, script_id, condition_id FROM gossip_menu LIMIT %s OFFSET %s",
        500,
        _handle_gossip_menu_row
    )

def _handle_gossip_menu_row(row):
    db.tri_world.execute_raw("INSERT INTO gossip_menu (MenuID, TextID, VerifiedBuild) VALUES (%s, %s, 40618)", (row[0], row[1],))
    return 0

def import_gossip_menu_options():
    db.tri_world.execute_raw("DELETE FROM gossip_menu_option")
    
    vm_options = db.vm_world.select_chunked(
        db.SelectQuery("gossip_menu_option"),
        250
    )
    
    for row in vm_options:
        if row['option_text'].startswith("GOSSIP_OPTION_"):
            continue
        
        upsert = db.UpsertQuery("gossip_menu_option").values({
            'MenuID': row['menu_id'],
            'OptionID': row['id'],
            'OptionNpc': row['option_icon'],
            'OptionText': row['option_text'],
            'OptionBroadcastTextID': row['option_broadcast_text'],
            'OptionNpcFlag': constants.ConvertNPCFlags(row['npc_option_npcflag']),
            'Language': 0,
            'ActionMenuID': max(0, row['action_menu_id']),
            'ActionPoiID': row['action_poi_id'],
            'BoxCoded': row['box_coded'],
            'BoxMoney': row['box_money'],
            'BoxText': row['box_text'],
            'BoxBroadcastTextID': row['box_broadcast_text'],
            'VerifiedBuild': constants.TargetBuild
        })

        db.tri_world.upsert(upsert)
    
