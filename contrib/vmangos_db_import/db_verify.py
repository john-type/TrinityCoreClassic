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

def main():
    print("Starting VMangos -> Trinity DB Verification...")

    print("Opening DB...")
    db.OpenAll()

    #TODO

    print("Closing DB...")
    db.CloseAll()

    print("Done")



if __name__ == '__main__':
    main()