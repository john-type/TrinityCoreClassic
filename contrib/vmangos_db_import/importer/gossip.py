#!/usr/bin/python3

import constants
import database as db

#TODO

def Import():
    import_gossip_menus()
    #TODO check gossip_menu_addon
    #TODO gossip_menu_option
    

def import_gossip_menus():
    db.vm_world.chunk(
        "SELECT entry, text_id, script_id, condition_id FROM gossip_menu LIMIT %s OFFSET %s",
        500,
        _handle_gossip_menu_row
    )

def _handle_gossip_menu_row(row):
    existing_row = db.tri_world.get_row("SELECT MenuID, TextID FROM gossip_menu WHERE MenuID = %s", (row[0],))
    
    if existing_row == None:
        db.tri_world.execute("INSERT INTO gossip_menu (MenuID, TextID, VerifiedBuild) VALUES (%s, %s, 40618)", (row[0], row[1],))
    else:
        if (existing_row[0] == row[0] and existing_row[1] == row[1]):
            db.tri_world.execute("UPDATE gossip_menu SET VerifiedBuild = 40618 WHERE MenuID = %s", (row[0],))
            #TODO handle changing textid.
            
            
    return 0