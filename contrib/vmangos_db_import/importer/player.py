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
    db.Execute(query, 'tri_world')
    
def cleanRaceUnlockRequirements():
    query = "DELETE FROM race_unlock_requirement WHERE raceID NOT IN ({0})".format(races_str)
    db.Execute(query, 'tri_world')
    
def cleanPlayerCreateInfo():
    query = "DELETE FROM playercreateinfo WHERE class NOT IN ({0}) OR race NOT IN ({1})".format(classes_str, races_str)
    db.Execute(query, 'tri_world')
    query2 = "DELETE FROM playercreateinfo_action WHERE class NOT IN ({0}) OR race NOT IN ({1})".format(classes_str, races_str)
    db.Execute(query2, 'tri_world')
    
def handleXpForLevel():
    vm_query = "SELECT * FROM player_xp_for_level"
    tri_delete = "DELETE FROM player_xp_for_level"
    tri_insert = "INSERT INTO player_xp_for_level (Level, Experience) VALUES (%s, %s)"
    
    rows = db.GetRows(vm_query, 'vm_world')
    db.Execute(tri_delete, 'tri_world')
    
    for row in rows:
        db.Execute(tri_insert, 'tri_world', (row[0], row[1],))
        
def handleExplorationXP():
    vm_query = "SELECT * FROM exploration_basexp"
    tri_delete = "DELETE FROM exploration_basexp"
    tri_insert = "INSERT INTO exploration_basexp (level, basexp) VALUES (%s, %s)"
    
    rows = db.GetRows(vm_query, 'vm_world')
    db.Execute(tri_delete, 'tri_world')
    
    for row in rows:
        db.Execute(tri_insert, 'tri_world', (row[0], row[1],))
    