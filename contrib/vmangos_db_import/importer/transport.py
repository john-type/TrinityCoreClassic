#!/usr/bin/python3

import constants
import database as db

def Import():
    db.tri_world.execute_raw("DELETE FROM transports")
    
    vm_transports = db.vm_world.select_chunked(
        db.SelectQuery("transports"),
        250
    )
    
    guid = 1
    for row in vm_transports:
        upsert = db.UpsertQuery("transports").values({
            'guid': guid,
            'entry': row['entry'],
            'name': row['name'],
            'phaseUseFlags': 0,
            'phaseid': 0,
            'phasegroup': 0,
            'ScriptName': ''
        })

        db.tri_world.upsert(upsert)
        guid = guid + 1
        
        vm_go = db.vm_world.select_one(
            db.SelectQuery("gameobject_template").where('entry', '=', row['entry'])
        )
        
        if vm_go == None:
            print("Unknown vmangos transport entry {}".format(row['entry']))
            continue
        
        tri_go = db.tri_world.select_one(
            db.SelectQuery("gameobject_template").where('entry', '=', row['entry'])
        )
        
        if tri_go == None:
            print("Unknown TC transport entry {}".format(row['entry']))
            continue
        
        db.tri_world.upsert(
            db.UpsertQuery("gameobject_template").values({
                'type': vm_go['type'],
                'displayId': vm_go['displayId'],
                'size': vm_go['size'],
                'Data0': vm_go['data0'],
                'Data1': vm_go['data1'],
                'Data2': vm_go['data2'],
                'Data3': vm_go['data3'],
                'Data4': vm_go['data4'],
                'Data5': vm_go['data5'],
                'Data6': vm_go['data6'],
            }).where('entry', '=', row['entry'])
        )
