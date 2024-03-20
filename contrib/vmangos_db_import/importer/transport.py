#!/usr/bin/python3

import constants
import database as db

def Import():
    remove_obsolete()
    add_missing()
    update_gameobject_templates()

def remove_obsolete():
    deleted = 0
    
    rows = db.tri_world.get_rows("SELECT guid, entry FROM transports")
    for row in rows:
        vm_rows = db.vm_world.get_rows("SELECT entry, name FROM transports WHERE entry = %s", (row[1],))
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
    
    rows = db.vm_world.get_rows("SELECT entry, name FROM transports")
    for row in rows:
        tri_rows = db.tri_world.get_rows("SELECT entry, name FROM transports WHERE entry = %s", (row[0],))
        if len(tri_rows) == 0:
            db.tri_world.Execute(insert_tri_transport, (row[0], row[1],))
            added += 1
    
    print("Added {} transports".format(added)) 
    
def update_gameobject_templates():
    rows = db.tri_world.get_rows("SELECT entry FROM transports")
    for row in rows:
        tri_go_template_row = db.tri_world.get_row("SELECT entry FROM gameobject_template WHERE entry = %s", (row[0],))
        vm_go_template_row = db.vm_world.get_row(
            "SELECT entry, type, displayId, size, data0, data1, data2, data3, data4, data5, data6 FROM gameobject_template WHERE entry = %s",
            (row[0],)
        )
        
        if(vm_go_template_row == None):
            continue
        
        if(tri_go_template_row == None):
            continue #TODO handle insert.
        
        #TODO handle gameobject.flags.
        
        go_taxi_id_update = ("UPDATE gameobject_template SET " 
        "type = %s, "
        "displayId = %s,"
        "size = %s,"
        "Data0 = %s, "
        "Data1 = %s, "
        "Data2 = %s, "
        "Data3 = %s, "
        "Data4 = %s, "
        "Data5 = %s, "
        "Data6 = %s "
        "WHERE entry = %s")
        
        db.tri_world.execute(go_taxi_id_update, (
            vm_go_template_row[1],
            vm_go_template_row[2],
            vm_go_template_row[3],
            vm_go_template_row[4],
            vm_go_template_row[5],
            vm_go_template_row[6],
            vm_go_template_row[7],
            vm_go_template_row[8],
            vm_go_template_row[9],
            vm_go_template_row[10],
            tri_go_template_row[0]
            ,))
        
        
        
        

