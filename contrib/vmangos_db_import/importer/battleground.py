#!/usr/bin/python3

import constants
import database as db

def Import():
    remove_battle_fields()
    remove_battlegrounds()

def remove_battle_fields():
    db.tri_world.execute_raw('DELETE FROM battlefield_template')
    
def remove_battlegrounds():
    db.tri_world.execute_raw('DELETE FROM battleground_template WHERE ID >= 4')
    db.tri_world.execute_raw('DELETE FROM battlemaster_entry WHERE bg_template >= 4')
    
#TODO import additional battleground_template data from vmangos