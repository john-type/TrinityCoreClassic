#!/usr/bin/python3

import constants
import database as db

#TODO 

#TODO import player race stats

classes_str = ','.join(map(str, constants.ClassIds))
races_str = ','.join(map(str, constants.RaceIds))

def Import():
    cleanClassExpansionRequirements()
    cleanRaceUnlockRequirements()
    cleanPlayerCreateInfo()
    handleXpForLevel()
    handleExplorationXP()


def cleanClassExpansionRequirements():
    query = "DELETE FROM class_expansion_requirement WHERE ClassID NOT IN ({0}) OR RaceID NOT IN ({1})".format(classes_str, races_str)
    db.tri_world.execute(query)
    
def cleanRaceUnlockRequirements():
    query = "DELETE FROM race_unlock_requirement WHERE raceID NOT IN ({0})".format(races_str)
    db.tri_world.execute(query)
    
def cleanPlayerCreateInfo():
    query = "DELETE FROM playercreateinfo WHERE class NOT IN ({0}) OR race NOT IN ({1})".format(classes_str, races_str)
    db.tri_world.execute(query)
    query2 = "DELETE FROM playercreateinfo_action WHERE class NOT IN ({0}) OR race NOT IN ({1})".format(classes_str, races_str)
    db.tri_world.execute(query2)
    
def handleXpForLevel():
    rows = db.vm_world.get_rows("SELECT * FROM player_xp_for_level")
    db.tri_world.execute("DELETE FROM player_xp_for_level")
    
    for row in rows:
        db.tri_world.execute(
            "INSERT INTO player_xp_for_level (Level, Experience) VALUES (%s, %s)",
            (row[0], row[1],)
        )
        
def handleExplorationXP():
    rows = db.vm_world.get_rows("SELECT * FROM exploration_basexp")
    db.tri_world.execute("DELETE FROM exploration_basexp")
    
    for row in rows:
        db.tri_world.execute(
            "INSERT INTO exploration_basexp (level, basexp) VALUES (%s, %s)",
            (row[0], row[1],)
        )
    