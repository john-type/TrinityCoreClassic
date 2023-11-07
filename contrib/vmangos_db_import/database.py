#!/usr/bin/python3

import mysql.connector

Connection = {
    "tri_world": None,
    "vm_world": None
}

Cursor = {
    "tri_world": None,
    "vm_world": None
}


def OpenAll():
    Connection["tri_world"] = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='trinity_world'
    )
        
    Connection["vm_world"] = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='vmangos_mangos'
    )
    
    Cursor["tri_world"] = Connection["tri_world"].cursor()
    Cursor["vm_world"] = Connection["vm_world"].cursor()


    
def CloseAll():
    for cur in Cursor:
        Cursor[cur].close()

    for con in Connection:
        Connection[con].close()
        

def GetRows(query, name, args = None):
    Cursor[name].execute(query, args)
    return Cursor[name].fetchall()

def Execute(query, name, args = None):
    Cursor[name].execute(query, args)
    Connection[name].commit()
    
def Insert(query, name, args = None):
    Cursor[name].execute(query, args)
    Connection[name].commit()
    return Cursor[name].lastrowid