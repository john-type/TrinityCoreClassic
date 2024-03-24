#!/usr/bin/python3

import constants
import database as db

def Import():
    vm_trainer_rows = db.vm_world.get_rows("SELECT entry, content_default FROM npc_trainer_greeting")
    
    for trainer_row in vm_trainer_rows:
        vm_creature_template = db.vm_world.get_row((
            "SELECT entry, gossip_menu_id, trainer_type, trainer_id FROM creature_template "
            "WHERE entry = %s"
        ), (trainer_row[0],))
        
        if vm_creature_template == None:
            continue
        
        tri_row = db.tri_world.get_row("SELECT Id, Type, Greeting FROM trainer WHERE Id = %s", (trainer_row[0],))
        
        if tri_row == None:
            db.tri_world.execute((
                "INSERT INTO trainer ("
                "Id, Type, Greeting, VerifiedBuild"
                ") VALUES (%s, %s, %s, 40618)"), (
                    trainer_row[0],
                    vm_creature_template[2],
                    trainer_row[1]
                ,))
        else:
            db.tri_world.execute((
                "UPDATE trainer SET "
                "Greeting = %s, Type = %s, VerifiedBuild = 40618 "
                "WHERE Id = %s"
            ),(trainer_row[1], vm_creature_template[2], trainer_row[0],))
            
            
        tri_link_row = db.tri_world.get_row("SELECT CreatureID, TrainerID, MenuID, OptionID FROM creature_trainer WHERE TrainerID = %s", (trainer_row[0],))
            
        # #TODO investigate optionID
        if tri_link_row == None:
            db.tri_world.execute((
                "INSERT INTO creature_trainer ("
                "CreatureID, TrainerID, MenuID, OptionID"
                ") VALUES (%s, %s, %s, %s)"
            ), (trainer_row[0], trainer_row[0], vm_creature_template[1], 0,))
            
        # #TODO handle link update
        
        # class spells
        vm_class_spells = db.vm_world.get_rows((
            "SELECT spell, spellcost, reqskill, reqskillvalue, reqlevel "
            "FROM npc_trainer_template WHERE entry = %s AND build_max = 5875"
        ), (vm_creature_template[3],))
        
        for vm_class_spell in vm_class_spells:
            _handle_trainer_spell(trainer_row[0], vm_class_spell)
        
        #individual spells
        vm_spells = db.vm_world.get_rows((
            "SELECT spell, spellcost, reqskill, reqskillvalue, reqlevel "
            "FROM npc_trainer WHERE entry = %s AND build_max = 5875"
            ), (trainer_row[0],))

        for vm_spell in vm_spells:
            _handle_trainer_spell(trainer_row[0], vm_spell)
        
def _handle_trainer_spell(trainer_id, vm_spell_row):
    existing_spell = db.tri_world.get_row("SELECT SpellId FROM trainer_spell WHERE TrainerId = %s AND SpellId = %s",
    (trainer_id, vm_spell_row[0],))
    
    #TODO handle req ability.
    if existing_spell == None:
        db.tri_world.execute((
            "INSERT INTO trainer_spell ("
            "TrainerId, SpellId, MoneyCost, ReqSkillLine, ReqSkillRank, "
            "ReqAbility1, ReqAbility2, ReqAbility3, ReqLevel, VerifiedBuild"
            ") VALUES (%s, %s, %s, %s, %s, 0, 0, 0, %s, 40618)"
            ), (trainer_id, vm_spell_row[0], vm_spell_row[1], vm_spell_row[2], vm_spell_row[3], vm_spell_row[4],))
    else:
        db.tri_world.execute((
            "UPDATE trainer_spell SET "
            "MoneyCost = %s, ReqSkillLine = %s, ReqSkillRank = %s, "
            "ReqAbility1 = 0, ReqAbility2 = 0, ReqAbility3 = 0, ReqLevel = %s, VerifiedBuild = 40618 "
            "WHERE TrainerId = %s AND SpellId = %s"
            ), ( vm_spell_row[1], vm_spell_row[2], vm_spell_row[3], vm_spell_row[4], trainer_id, vm_spell_row[0],))
