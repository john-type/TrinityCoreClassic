#!/usr/bin/python3

import constants
import database as db

#TODO

def Import():
    import_templates_vmangos()
    
def import_templates_vmangos():
        db.vm_world.chunk(
        ("SELECT entry, Method, QuestLevel, MinLevel, MaxLevel, "
         "Type, SuggestedPlayers, "
         "Title, Details, Objectives, EndText, "
         "PrevQuestId, NextQuestId, ExclusiveGroup, BreadcrumbForQuestId "
         "FROM quest_template LIMIT %s OFFSET %s"),
        500,
        _handle_import_template_row
    )
        
def _handle_import_template_row(row):
    dest_template_query = "SELECT ID, LogTitle FROM quest_template WHERE ID = %s"
    
    match_row = db.tri_world.get_row(dest_template_query, (row[0],))
    
    if(match_row == None):
        _upsert_quest_template(row)
    else: 
        _upsert_quest_template(row, match_row)
    
    return 0

def _upsert_quest_template(vm_qt, tri_qt = None):
    if tri_qt == None:
        return #TODO handle insert
    
    #TODO quest_offer_reward
    #TODO other tables.
    
    #TODO more fields
    update_query = ("UPDATE quest_template SET "
    "QuestType = %s, QuestLevel = %s, MinLevel = %s, "
    "QuestInfoID = %s, SuggestedGroupNum = %s, "
    "LogTitle = %s, QuestDescription = %s, LogDescription = %s, AreaDescription = %s, "
    "VerifiedBuild = 40618, Expansion = 0 "
    "WHERE ID = %s"
    )
    
    db.tri_world.execute(update_query, (
        vm_qt[1], vm_qt[2], vm_qt[3], 
        vm_qt[5], vm_qt[6],
        vm_qt[7], vm_qt[8], vm_qt[9], vm_qt[10],
        vm_qt[0] #entry
    ,))
    
    
    existing_addon_entry = db.tri_world.get_row("SELECT ID FROM quest_template_addon WHERE ID = %s", (vm_qt[0],))
    
    #TODO more fieldss
    if existing_addon_entry == None:
        # insert_query = (
            
        # )
        #TODO handle insert
        pass
    else:
        update_query = (
            "UPDATE quest_template_addon SET "
            "MaxLevel = %s, "
            "PrevQuestId = %s, NextQuestId = %s, ExclusiveGroup = %s, BreadcrumbForQuestId = %s "
            "WHERE ID = %s"
        )
        
        #TODO decide how to correctly handle column differences
        next_quest_id = vm_qt[12]
        if(next_quest_id < 0):
            next_quest_id = 0
        
        db.tri_world.execute(update_query, (
            vm_qt[4],
            vm_qt[11], next_quest_id, vm_qt[13], vm_qt[14],
            vm_qt[0] #entry
        ))
        
    
    