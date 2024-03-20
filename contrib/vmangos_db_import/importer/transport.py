#!/usr/bin/python3

import constants
import database as db

def Import():
    remove_obsolete()
    add_missing()

def remove_obsolete():
    deleted = 0
    
    rows = db.tri_world.get_rows("SELECT * FROM transports")
    for row in rows:
        vm_rows = db.vm_world.get_rows("SELECT * FROM transports WHERE entry = %s", (row[1],))
        if len(vm_rows) == 0:
            db.tri_world.execute("DELETE FROM transports WHERE entry = %s" (row[1],))
            deleted += 1
            
    print("Deleted {} transports".format(deleted))  
    

def add_missing():
    insert_tri_transport = (
        "INSERT INTO transports "
        "(entry, name, phaseUseFlags, phaseid, phasegroup, ScriptName) "
        "VALUES "
        "(%s, %s, 0, 0, 0, '')"
    )
    
    added = 0
    
    rows = db.vm_world.get_rows("SELECT * FROM transports")
    for row in rows:
        tri_rows = db.tri_world.get_rows("SELECT * FROM transports WHERE entry = %s", (row[0],))
        if len(tri_rows) == 0:
            db.tri_world.Execute(insert_tri_transport, (row[0], row[1],))
            added += 1
    
    print("Added {} transports".format(added)) 