#!/usr/bin/python3

import constants
import database as db

def Import():
    import_pages()
    import_weather()
    import_points_of_interest()


def import_pages():
    vm_rows = db.vm_world.select_chunked(
        db.SelectQuery("page_text").order_by("entry ASC"), 
        500
    )
    
    for vm_row in vm_rows:
        existing = db.tri_world.select_one(
            db.SelectQuery("page_text").where("ID", "=", vm_row['entry'])
        )
        
        if existing == None:
            db.tri_world.upsert(
                db.UpsertQuery("page_text").values({
                    'ID': vm_row['entry'],
                    'Text': vm_row['text'],
                    'NextPageID': vm_row['next_page'],
                    'PlayerConditionID': 0,
                    'Flags': 0,
                    'VerifiedBuild': constants.TargetBuild
                })
            )
        else:
            db.tri_world.upsert(
                db.UpsertQuery("page_text").values({
                    'Text': vm_row['text'],
                    'NextPageID': vm_row['next_page'],
                    'VerifiedBuild': constants.TargetBuild
                }).where("ID", "=", vm_row['entry'])
            )
            
def import_weather():
    vm_rows = db.vm_world.select_all(
        db.SelectQuery("game_weather")
    )
    
    for vm_row in vm_rows:
        existing = db.tri_world.select_one(
            db.SelectQuery("game_weather").where("zone", "=", vm_row['zone'])
        )
        
        upsert = db.UpsertQuery("game_weather").values({
            'spring_rain_chance': vm_row['spring_rain_chance'],
            'spring_snow_chance': vm_row['spring_snow_chance'],
            'spring_storm_chance': vm_row['spring_storm_chance'],
            'summer_rain_chance': vm_row['summer_rain_chance'],
            'summer_snow_chance': vm_row['summer_snow_chance'],
            'summer_storm_chance': vm_row['summer_storm_chance'],
            'fall_rain_chance': vm_row['fall_rain_chance'],
            'fall_snow_chance': vm_row['fall_snow_chance'],
            'fall_storm_chance': vm_row['fall_storm_chance'],
            'winter_rain_chance': vm_row['winter_rain_chance'],
            'winter_snow_chance': vm_row['winter_snow_chance'],
            'winter_storm_chance': vm_row['winter_storm_chance'],
            'ScriptName': ''
        })
        
        if existing == None:
            upsert.values({'zone': vm_row['zone']})
        else:
            upsert.where("zone", "=", vm_row['zone'])
            
def import_points_of_interest():
    vm_rows = db.vm_world.select_all(
        db.SelectQuery("points_of_interest")
    )
    
    for vm_row in vm_rows:
        existing = db.tri_world.select_one(
            db.SelectQuery("points_of_interest").where("ID", "=", vm_row['entry'])
        )
        
        upsert = db.UpsertQuery("points_of_interest").values({
            'PositionX': vm_row['x'],
            'PositionY': vm_row['y'],
            'PositionZ': 0,
            'Icon': vm_row['icon'],
            'Flags': vm_row['flags'],
            'Importance': vm_row['data'],
            'Name': vm_row['icon_name'],
            'VerifiedBuild': constants.TargetBuild
        })
        
        if existing == None:
            upsert.values({
                'ID': vm_row['entry']
            })
        else:
            upsert.where("ID", "=", vm_row['entry'])
            
            
        db.tri_world.upsert(upsert)