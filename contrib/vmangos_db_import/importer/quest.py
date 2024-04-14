#!/usr/bin/python3

import constants
import database as db

#TODO

def Import():
    import_templates_vmangos()
    #remove_modern()
    
def remove_modern():
    db.tri_world.chunk_raw(
        "SELECT ID FROM quest_template WHERE Expansion > 2 AND VerifiedBuild <> 40618 LIMIT %s OFFSET %s",
        500,
        _handle_obsolete_modern_row
    )
    
def _handle_obsolete_modern_row(row):
    queries = [
        "DELETE FROM quest_objectives WHERE QuestID = %s",
        "DELETE FROM quest_objectives_locale WHERE QuestId = %s",
        "DELETE FROM quest_offer_reward WHERE ID = %s",
        "DELETE FROM quest_offer_reward_locale WHERE ID = %s",
        "DELETE FROM quest_poi WHERE QuestID = %s",
        "DELETE FROM quest_poi_points WHERE QuestID = %s",
        "DELETE FROM quest_pool_members WHERE questId = %s",
        "DELETE FROM quest_request_items WHERE ID = %s",
        "DELETE FROM quest_request_items_locale WHERE ID = %s",
        "DELETE FROM quest_reward_display_spell WHERE QuestID = %s",
        "DELETE FROM quest_template_addon WHERE ID = %s",
        "DELETE FROM quest_template_locale WHERE ID = %s",
        "DELETE FROM quest_template WHERE ID = %s"
    ]
    
    db.tri_world.execute_many_raw(queries, (row[0],))
    
    return -1
    
def import_templates_vmangos():
    db.vm_world.chunk_raw(
        ("SELECT entry, Method, QuestLevel, MinLevel, MaxLevel, "
         "Type, SuggestedPlayers, "
         "Title, Details, Objectives, EndText, "
         "PrevQuestId, NextQuestId, ExclusiveGroup, BreadcrumbForQuestId, "
         "SrcSpell, SrcItemId, SrcItemCount, "
         "RequiredClasses, RequiredSkill, RequiredSkillValue, "
         "RequiredMinRepFaction, RequiredMinRepValue, RequiredMaxRepFaction, RequiredMaxRepValue "
         "FROM quest_template LIMIT %s OFFSET %s"),
        500,
        _handle_import_template_row
    )
        
def _handle_import_template_row(row):
    dest_template_query = "SELECT ID, LogTitle FROM quest_template WHERE ID = %s"
    
    match_row = db.tri_world.get_row_raw(dest_template_query, (row[0],))
    
    if(match_row == None):
        _upsert_quest_template(row)
    else: 
        _upsert_quest_template(row, match_row)
    
    return 0

def _upsert_quest_template(vm_qt, tri_qt = None):
    if tri_qt == None:
        return #TODO handle insert
    
    #TODO quest_offer_reward
    #TODO rewards
    #TODO other tables.
    
    #TODO more fields
    update_query = ("UPDATE quest_template SET "
    "QuestType = %s, QuestLevel = %s, MinLevel = %s, "
    "QuestInfoID = %s, SuggestedGroupNum = %s, "
    "LogTitle = %s, QuestDescription = %s, LogDescription = %s, AreaDescription = %s, "
    "StartItem = %s, "
    "VerifiedBuild = 40618, Expansion = 0 "
    "WHERE ID = %s"
    )
    
    db.tri_world.execute_raw(update_query, (
        vm_qt[1], vm_qt[2], vm_qt[3], 
        vm_qt[5], vm_qt[6],
        vm_qt[7], vm_qt[8], vm_qt[9], vm_qt[10],
        vm_qt[16],
        vm_qt[0] #entry
    ,))
    
    
    existing_addon_entry = db.tri_world.get_row_raw("SELECT ID FROM quest_template_addon WHERE ID = %s", (vm_qt[0],))
    
    #TODO more fieldss
    if existing_addon_entry == None:
        # insert_query = (
            
        # )
        #TODO handle insert
        return
    else:
        update_query = (
            "UPDATE quest_template_addon SET "
            "MaxLevel = %s, "
            "PrevQuestId = %s, NextQuestId = %s, ExclusiveGroup = %s, BreadcrumbForQuestId = %s, "
            "SourceSpellID = %s, ProvidedItemCount = %s, "
            "AllowableClasses = %s, RequiredSkillID = %s, RequiredSkillPoints =%s, "
            "RequiredMinRepFaction = %s, RequiredMinRepValue = %s, RequiredMaxRepFaction = %s, RequiredMaxRepValue = %s "
            "WHERE ID = %s"
        )
        
        #TODO decide how to correctly handle column differences
        next_quest_id = vm_qt[12]
        if(next_quest_id < 0):
            next_quest_id = 0
        
        db.tri_world.execute_raw(update_query, (
            vm_qt[4],
            vm_qt[11], next_quest_id, vm_qt[13], vm_qt[14],
            vm_qt[15], vm_qt[17],
            vm_qt[18], vm_qt[19],  vm_qt[20],
            vm_qt[21], vm_qt[22], vm_qt[23], vm_qt[24],     
            vm_qt[0] #entry
        ))
        
    
    _update_quest_objectives(vm_qt[0])
    _update_quest_rewards(vm_qt[0])
    
    
def _update_quest_objectives(quest_id):
    vm_row = db.vm_world.get_row_raw((
        "SELECT "
        "ReqItemId1, ReqItemId2, ReqItemId3, ReqItemId4, " # objective item
        "ReqItemCount1, ReqItemCount2, ReqItemCount3, ReqItemCount4, "
        "ReqSourceId1, ReqSourceId2, ReqSourceId3, ReqSourceId4, "      #provided item
        "ReqSourceCount1, ReqSourceCount2, ReqSourceCount3, ReqSourceCount4, "
        "ReqCreatureOrGOId1, ReqCreatureOrGOId2, ReqCreatureOrGOId3, ReqCreatureOrGOId4, "#objective creature / GO
        "ReqCreatureOrGOCount1, ReqCreatureOrGOCount2, ReqCreatureOrGOCount3, ReqCreatureOrGOCount4, " 
        "ReqSpellCast1, ReqSpellCast2, ReqSpellCast3, ReqSpellCast4, "  #objectives spell
        "RepObjectiveFaction, RepObjectiveValue, "  # min rep
        "RewOrReqMoney, "
        "ObjectiveText1, ObjectiveText2, ObjectiveText3, ObjectiveText4 "
        "FROM quest_template WHERE entry = %s"
        ), (quest_id,))
    

    
    if vm_row == None:
        return
    
    #TODO handle ReqSource    
    #TODO handle spellCast (trinity doesnt seem to use this, but the GO for it instead), possibly easier to manually add.
    #TODO ensure all objective types are covered.
    
    existing_objectives = db.tri_world.get_rows_raw("SELECT ID from quest_objectives WHERE QuestID = %s ORDER BY `Order` ASC", (quest_id,))
    
    #order is GO/Creature, Item, MinRep, Money
    #storage index appears to the same as order.
    #type for and above (money/currency and rep) appear to be -1 storage index.
    
    intermediate_rows = []  #type, id, amount
    
    descriptions = [
        vm_row[31], vm_row[32], vm_row[33], vm_row[34]
    ]
    
    #creatures / GO
    if vm_row[20] > 0:
        if vm_row[16] > 0:
            intermediate_rows.append([0, vm_row[16], vm_row[20]])
        else:
            intermediate_rows.append([2, vm_row[16], vm_row[20]])
    
    if vm_row[21] > 0:
        if vm_row[17] > 0:
            intermediate_rows.append([0, vm_row[17], vm_row[21]])
        else:
            intermediate_rows.append([2, vm_row[17], vm_row[21]])
            
    if vm_row[22] > 0:
        if vm_row[18] > 0:
            intermediate_rows.append([0, vm_row[18], vm_row[22]])
        else:
            intermediate_rows.append([2, vm_row[18], vm_row[22]])
            
    if vm_row[23] > 0:
        if vm_row[19] > 0:
            intermediate_rows.append([0, vm_row[19], vm_row[23]])
        else:
            intermediate_rows.append([2, vm_row[19], vm_row[23]])
    
    #items
    if vm_row[0] > 0 and vm_row[4] > 0:
        intermediate_rows.append([1, vm_row[0], vm_row[4]])
        
    if vm_row[1] > 0 and vm_row[5] > 0:
        intermediate_rows.append([1, vm_row[1], vm_row[5]])
        
    if vm_row[2] > 0 and vm_row[6] > 0:
        intermediate_rows.append([1, vm_row[2], vm_row[6]])
        
    if vm_row[3] > 0 and vm_row[7] > 0:
        intermediate_rows.append([1, vm_row[3], vm_row[7]])
        
    #rep
    if vm_row[28] > 0:
        intermediate_rows.append([6, vm_row[28], vm_row[29]])
    
    #money
    if vm_row[30] < 0:
        intermediate_rows.append([8, 0, vm_row[30]])
        
    order_index = 0
    storage_index = 0
    for intermediate in intermediate_rows:
        existing_id = 0
        
        if len(existing_objectives) > order_index:
            existing_id = existing_objectives[order_index][0]
            
            
        effective_storage_index = -1
        description = ""
        if intermediate[0] < 4:
            effective_storage_index = storage_index
            if len(descriptions) > storage_index:
                description = descriptions[storage_index]
            storage_index += 1
        
        #TODO confirm descriptions match objectives. 
        #TODO handle flags.
    
        if existing_id > 0:
            db.tri_world.execute_raw((
                "UPDATE quest_objectives SET "
                "`Type` = %s, `Order` = %s, StorageIndex = %s, "
                "ObjectID = %s, Amount = %s, "
                "Flags = 0, Flags2 = 0, ProgressBarWeight = 0, "
                "Description = %s, VerifiedBuild = 40618 "
                "WHERE ID = %s AND QuestID = %s"
            ), (
                intermediate[0], order_index, effective_storage_index,
                intermediate[1], intermediate[2],
                description,    
                existing_id, quest_id,
            ))
        else:
            next_id = db.tri_world.get_row_raw("SELECT MAX(ID) FROM quest_objectives")
            next_id = next_id[0] + 1
            
            db.tri_world.execute_raw((
                "INSERT INTO quest_objectives ("
                "ID, QuestId, `Type`, `Order`, StorageIndex, "
                "ObjectID, Amount, "
                "Flags, Flags2, ProgressBarWeight, Description, VerifiedBuild"
                ") VALUES ("
                "%s, %s, %s, %s, %s, "
                "%s, %s, "
                "0, 0, 0, %s, 40618"
                ")"
            ), (
                next_id, quest_id, intermediate[0], order_index, effective_storage_index,
                intermediate[1], intermediate[2],
                description,
            ))
            
        order_index += 1
    
    #TODO delete obsolete objectives.
    
    
def _update_quest_rewards(quest_id):
    vm_row = db.vm_world.get_row_raw((
        "SELECT "
        "RewChoiceItemId1, RewChoiceItemId2, RewChoiceItemId3, RewChoiceItemId4, RewChoiceItemId5, RewChoiceItemId6,"
        "RewChoiceItemCount1, RewChoiceItemCount2, RewChoiceItemCount3, RewChoiceItemCount4, RewChoiceItemCount5, RewChoiceItemCount6, "
        "RewItemId1, RewItemId2, RewItemId3, RewItemId4, "
        "RewItemCount1, RewItemCount2, RewItemCount3, RewItemCount4, "
        "RewRepFaction1, RewRepFaction2, RewRepFaction3, RewRepFaction4, RewRepFaction5, "
        "RewRepValue1, RewRepValue2, RewRepValue3, RewRepValue4, RewRepValue5, "
        "RewXP, RewOrReqMoney, RewMoneyMaxLevel, "  #TODO implement in update
        "RewSpell, RewSpellCast, RewMailTemplateId, RewMailDelaySecs, RewMailMoney " #TODO implement in update
        "FROM quest_template WHERE entry = %s"
    ), (quest_id,))
    
    if vm_row == None:
        return
    
    update_query = (
     "UPDATE quest_template SET "
     "RewardChoiceItemID1 = %s, RewardChoiceItemID2 = %s, RewardChoiceItemID3 = %s, "
     "RewardChoiceItemID4 = %s, RewardChoiceItemID5 = %s, RewardChoiceItemID6 = %s, "
     "RewardChoiceItemQuantity1 = %s, RewardChoiceItemQuantity2 = %s, RewardChoiceItemQuantity3 = %s, "
     "RewardChoiceItemQuantity4 = %s, RewardChoiceItemQuantity5 = %s, RewardChoiceItemQuantity6 = %s, "
     "RewardItem1 = %s, RewardItem2 = %s, RewardItem3 = %s, RewardItem4 = %s, "
     "RewardAmount1 = %s, RewardAmount2 = %s, RewardAmount3 = %s, RewardAmount4 = %s, "
     "RewardFactionID1 = %s, RewardFactionID2 = %s, RewardFactionID3 = %s,RewardFactionID4 = %s, RewardFactionID5 = %s,"
     "RewardFactionValue1 = %s, RewardFactionValue2 = %s, RewardFactionValue3 = %s,RewardFactionValue4 = %s, RewardFactionValue5 = %s "
     "WHERE ID = %s"   
    )
    
    db.tri_world.execute_raw(update_query, (
            vm_row[0], vm_row[1], vm_row[2], #choice
            vm_row[3], vm_row[4], vm_row[5], #choice
            vm_row[6], vm_row[7], vm_row[8], #choice
            vm_row[9], vm_row[10], vm_row[11], #choice
            vm_row[12], vm_row[13], vm_row[14], vm_row[15], #item
            vm_row[16], vm_row[17], vm_row[18], vm_row[19], #item
            vm_row[20], vm_row[21], vm_row[22], vm_row[23], vm_row[24], #faction
            vm_row[25], vm_row[26], vm_row[27], vm_row[28], vm_row[29], #faction        
            quest_id
        ))