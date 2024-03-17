#!/usr/bin/python3

import constants
import database as db

def Import():
    remove_battle_fields()
    remove_battlegrounds()

def remove_battle_fields():
    query = 'DELETE FROM battlefield_template'
    db.Execute(query, 'tri_world')
    
def remove_battlegrounds():
    query = 'DELETE FROM battleground_template WHERE ID >= 4'
    query2 = 'DELETE FROM battlemaster_entry WHERE bg_template >= 4'
    db.Execute(query, 'tri_world')
    db.Execute(query2, 'tri_world')
    
#TODO import additional battleground_template data from vmangos