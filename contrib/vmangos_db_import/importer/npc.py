#!/usr/bin/python3

import constants
import database as db

#TODO

def Import():
    import_npc_text()
    
    
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