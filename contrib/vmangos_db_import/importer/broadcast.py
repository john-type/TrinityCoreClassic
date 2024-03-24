#!/usr/bin/python3

import constants
import database as db
import csv

def Import():
    import_broadcast_text_csv()

def import_broadcast_text_csv():
    found_header = False
    with open('BroadcastTexts1.csv') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if found_header == False:
                found_header = True
                continue
        
            existing_row = db.tri_hotfix.get_row("SELECT ID FROM broadcast_text WHERE ID = %s", (row[0],))
            
            if existing_row == None:
                db.tri_hotfix.execute((
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
                db.tri_hotfix.execute((
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
            
          
     
     
