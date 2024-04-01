#!/usr/bin/python3

import constants
import database as db
import mysql.connector
import importer.area
import importer.battleground
import importer.creature
import importer.gameobject
import importer.gossip
import importer.item
import importer.npc
import importer.player
import importer.quest
import importer.skill
import importer.spell
import importer.transport
import importer.cleanup

missing_creature_templates = []
missing_creatures = []
missing_gameobject_templates = []
missing_gameobjects = []

def main():
    print("Starting VMangos -> Trinity DB Verification...")

    print("Opening DB...")
    db.OpenAll()

    verify_creature_templates()

    print("---")
    
    verify_creatures()
    
    print("---")
    
    verify_gameobject_templates()

    print("---")
    
    verify_gameobjects()

    print("---")

    print("Closing DB...")
    db.CloseAll()

    print("Done")
    
    
    
def verify_creature_templates():
    vm_count_row = db.vm_world.get_row("SELECT COUNT(*) FROM creature_template")
    tri_count_row = db.tri_world.get_row("SELECT COUNT(*) FROM creature_template")
    
    print("Vmangos Creature Template count: {}".format(vm_count_row[0]))
    print("Trinity Creature Template count: {}".format(tri_count_row[0]))
    
    db.vm_world.chunk(
        ("SELECT entry FROM creature_template GROUP BY entry LIMIT %s OFFSET %s"),
        500,
        _handle_verify_creature_template_row
    )
    
    print("Missing Creature Template count: {}".format(len(missing_creature_templates)))
    if(len(missing_creature_templates) < 10):
        print(missing_creature_templates)
    
def _handle_verify_creature_template_row(row):
    existing_row = db.tri_world.get_row(
        "SELECT entry FROM creature_template WHERE entry = %s", 
        (row[0],)
    )
    
    if existing_row == None:
        missing_creature_templates.append(row[0])
        
    return 0

def verify_creatures():
    vm_count_row = db.vm_world.get_row("SELECT COUNT(*) FROM creature")
    tri_count_row = db.tri_world.get_row("SELECT COUNT(*) FROM creature")
    
    print("Vmangos Creature count: {}".format(vm_count_row[0]))
    print("Trinity Creature count: {}".format(tri_count_row[0]))
    
def verify_gameobject_templates():
    vm_count_row = db.vm_world.get_row("SELECT COUNT(*) FROM gameobject_template")
    tri_count_row = db.tri_world.get_row("SELECT COUNT(*) FROM gameobject_template")
    
    print("Vmangos GO Template count: {}".format(vm_count_row[0]))
    print("Trinity GO Template count: {}".format(tri_count_row[0]))
    
    db.vm_world.chunk(
        ("SELECT entry FROM gameobject_template GROUP BY entry LIMIT %s OFFSET %s"),
        500,
        _handle_verify_gameobject_template_row
    )
    
    print("Missing GO Template count: {}".format(len(missing_gameobject_templates)))
    if(len(missing_gameobject_templates) < 10):
        print(missing_gameobject_templates)
    
def _handle_verify_gameobject_template_row(row):
    existing_row = db.tri_world.get_row(
        "SELECT entry FROM gameobject_template WHERE entry = %s", 
        (row[0],)
    )
    
    if existing_row == None:
        missing_gameobject_templates.append(row[0])
        
    return 0

def verify_gameobjects():
    
    vm_count_row = db.vm_world.get_row("SELECT COUNT(*) FROM gameobject")
    tri_count_row = db.tri_world.get_row("SELECT COUNT(*) FROM gameobject")
    
    print("Vmangos GO count: {}".format(vm_count_row[0]))
    print("Trinity GO count: {}".format(tri_count_row[0]))
    

if __name__ == '__main__':
    main()