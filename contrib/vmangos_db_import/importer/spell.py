#!/usr/bin/python3

import constants
import database as db

def Import():
    handle_spell_target_positions()

def handle_spell_target_positions():
    vm_rows = db.vm_world.get_rows("SELECT id, target_map, target_position_x, target_position_y, target_position_z, target_orientation FROM spell_target_position WHERE build_max = 5875")
    
    for vm_row in vm_rows:
        existing = db.tri_world.get_row("SELECT ID FROM spell_target_position WHERE ID = %s", (vm_row[0],))
        
        #TODO confirm EffectIndex usage.
        #TODO orientaion.
        
        if(existing == None):
            db.tri_world.execute((
                "INSERT INTO spell_target_position ("
                "ID, EffectIndex, MapID, PositionX, PositionY, PositionZ, VerifiedBuild"
                ") VALUES ("
                "%s, 0, %s, %s, %s, %s, 40618"
                ")"
            ), (
                vm_row[0],
                vm_row[1],
                vm_row[2],
                vm_row[3],
                vm_row[4],
            ))
        else:
            db.tri_world.execute((
                "UPDATE spell_target_position SET "
                "MapID = %s, PositionX = %s, PositionY = %s, PositionZ = %s, VerifiedBuild = 40618 "
                "WHERE ID = %s"
            ), (
                vm_row[1],
                vm_row[2],
                vm_row[3],
                vm_row[4],
                vm_row[0],
            ))
            
    #TODO delete excess.