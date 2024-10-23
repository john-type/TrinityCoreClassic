#!/usr/bin/python3

import constants
import database as db


def Import():
    handle_enchants()

def handle_enchants():
    db.tri_world.execute_raw("DELETE FROM item_enchantment_template")
    
    vm_rows = db.vm_world.select_chunked(
        db.SelectQuery("item_enchantment_template").where('patch_max',"=", 10).order_by("entry ASC"),
        500
    )
    
    for vm_row in vm_rows:
        db.tri_world.upsert(
            db.UpsertQuery("item_enchantment_template").values({
                'entry': vm_row['entry'],
                'type': 0,  #TODO confirm.
                'ench': vm_row['ench'],
                'chance': vm_row['chance']
            })
        )