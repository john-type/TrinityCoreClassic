#!/usr/bin/python3

import constants
import database as db

#TODO

def Import():
    remove_obsolete()
    add_missing()

def remove_obsolete():
    query_tri_transports = "SELECT * FROM transports"
    query_vm_transport = "SELECT * FROM transports WHERE entry = %s"
    delete_tri_transport = "DELETE FROM transports WHERE entry = %s"
    
    deleted = 0
    
    rows = db.GetRows(query_tri_transports, 'tri_world')
    for row in rows:
        vm_rows = db.GetRows(query_vm_transport, 'vm_world', (row[1],))
        if len(vm_rows) == 0:
            db.Execute(delete_tri_transport, 'tri_world', (row[1],))
            deleted += 1
            
    print("Deleted {} transports".format(deleted))  
    

def add_missing():
    query_vm_transports = "SELECT * FROM transports"
    query_tri_transport = "SELECT * FROM transports WHERE entry = %s"
    insert_tri_transport = (
        "INSERT INTO transports "
        "(entry, name, phaseUseFlags, phaseid, phasegroup, ScriptName) "
        "VALUES "
        "(%s, %s, 0, 0, 0, '')"
    )
    
    added = 0
    
    rows = db.GetRows(query_vm_transports, 'vm_world')
    for row in rows:
        tri_rows = db.GetRows(query_tri_transport, 'tri_world', (row[0],))
        if len(tri_rows) == 0:
            db.Execute(
                insert_tri_transport, 
                'tri_world',
                (
                    row[0], 
                    row[1]    
                )
                )
            added += 1
    
    print("Added {} transports".format(added)) 