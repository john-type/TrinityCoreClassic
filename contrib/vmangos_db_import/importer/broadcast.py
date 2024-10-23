#!/usr/bin/python3

import constants
import database as db
import csv

def Import():
    import_broadcast_text_vmangos()
    import_broadcast_text_csv()

def import_broadcast_text_vmangos(): 
    vm_text = db.vm_world.select_chunked(
        db.SelectQuery("broadcast_text"),
        250
    )
    
    for row in vm_text:
        existing = db.tri_hotfix.select_one(
            db.SelectQuery("broadcast_text").where("ID", "=", row['entry'])
        )
        
        if existing != None:
            continue
        
        upsert = db.UpsertQuery("broadcast_text").values({
            'Text': row['male_text'],
            'Text1': row['female_text'],
            'ID': row['entry'],
            'LanguageID': row['language_id'],
            'ConditionID': 0,
            'EmotesID': 0,
            'Flags': 0,
            'ChatBubbleDurationMs': 0,
            'VoiceOverPriorityID': 0,
            'SoundKitID1': row['sound_id'],
            'SoundKitID2': 0,
            'EmoteID1': row['emote_id1'],
            'EmoteID2': row['emote_id2'],
            'EmoteID3': row['emote_id3'],
            'EmoteDelay1': row['emote_delay1'],
            'EmoteDelay2': row['emote_delay2'],
            'EmoteDelay3': row['emote_delay3'],
            'VerifiedBuild': constants.TargetBuild
        })
        
        db.tri_hotfix.upsert(upsert)
        
        

def import_broadcast_text_csv():
    # include the CSV file from hermes proxy.
    found_header = False
    with open('BroadcastTexts1.csv') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if found_header == False:
                found_header = True
                continue
        
            existing_row = db.tri_hotfix.get_row_raw("SELECT ID FROM broadcast_text WHERE ID = %s", (row[0],))
            
            if existing_row == None:
                db.tri_hotfix.execute_raw((
                    "INSERT INTO broadcast_text ("
                    "Text, Text1, ID, LanguageID, ConditionID, EmotesID, Flags, ChatBubbleDurationMs, VoiceOverPriorityID, "
                    "SoundKitID1, SoundKitID2, "
                    "EmoteID1, EmoteID2, EmoteID3, "
                    "EmoteDelay1, EmoteDelay2, EmoteDelay3, "
                    "VerifiedBuild"
                    ") VALUES (%s, %s, %s, %s, 0, 0, 0, 0, 0, 0, 0, %s, %s, %s, %s, %s, %s, 40618)"
                ), (
                    row[1], row[2], row[0], row[3],
                    row[4], row[5], row[6],
                    row[7], row[8], row[9]
                ,))
            else:
                db.tri_hotfix.execute_raw((
                    "UPDATE broadcast_text SET "
                    "Text = %s, Text1 = %s, "
                    "LanguageID = %s, "
                    "EmoteID1 = %s, EmoteID2 = %s, EmoteID3 = %s, "
                    "EmoteDelay1 = %s, EmoteDelay2 = %s, EmoteDelay3 = %s, "
                    "VerifiedBuild = 40618 "
                    "WHERE ID = %s"
                ), (
                    row[1], row[2],
                    row[3],
                    row[4], row[5], row[6],
                    row[7], row[8],row[9],
                    row[0]
                ,))
            
          
     
     
