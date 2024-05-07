#!/usr/bin/python3

TargetBuild = 40618

MaxMapId = 533

NormalMaps = [
    0, 1, 25, 35, 37, 42, 369, 449, 450, 451
]

DungeonMaps = [
    13, 29, 33, 34, 36, 43, 44, 47, 48, 70, 90, 109, 129,  189, 209, 229, 230, 269, 289,  329, 349, 389, 429, 
]

Raid20Maps = [
    169, 309, 509, 531
]

Raid40Maps = [
    169, 249, 409, 469, 531, 533
]


BgMaps = [
    30, 489, 529, 
]

ClassIds = [
    1,2,3,4,5,7,8,9,11
]

RaceIds = [
    1,2,3,4,5,6,7,8,9
]

NPCFlags = {
    "UNIT_NPC_FLAG_NONE": 0x00000000,
    "UNIT_NPC_FLAG_GOSSIP": 0x00000001,     # TITLE has gossip menu DESCRIPTION 100%
    "UNIT_NPC_FLAG_QUESTGIVER": 0x00000002,     # TITLE is quest giver DESCRIPTION 100%
    "UNIT_NPC_FLAG_UNK1": 0x00000004,
    "UNIT_NPC_FLAG_UNK2": 0x00000008,
    "UNIT_NPC_FLAG_TRAINER": 0x00000010,     # TITLE is trainer DESCRIPTION 100%
    "UNIT_NPC_FLAG_TRAINER_CLASS": 0x00000020,     # TITLE is class trainer DESCRIPTION 100%
    "UNIT_NPC_FLAG_TRAINER_PROFESSION": 0x00000040,     # TITLE is profession trainer DESCRIPTION 100%
    "UNIT_NPC_FLAG_VENDOR": 0x00000080,     # TITLE is vendor (generic) DESCRIPTION 100%
    "UNIT_NPC_FLAG_VENDOR_AMMO": 0x00000100,     # TITLE is vendor (ammo) DESCRIPTION 100%, general goods vendor
    "UNIT_NPC_FLAG_VENDOR_FOOD": 0x00000200,     # TITLE is vendor (food) DESCRIPTION 100%
    "UNIT_NPC_FLAG_VENDOR_POISON": 0x00000400,     # TITLE is vendor (poison) DESCRIPTION guessed
    "UNIT_NPC_FLAG_VENDOR_REAGENT": 0x00000800,     # TITLE is vendor (reagents) DESCRIPTION 100%
    "UNIT_NPC_FLAG_REPAIR": 0x00001000,     # TITLE can repair DESCRIPTION 100%
    "UNIT_NPC_FLAG_FLIGHTMASTER": 0x00002000,     # TITLE is flight master DESCRIPTION 100%
    "UNIT_NPC_FLAG_SPIRITHEALER": 0x00004000,     # TITLE is spirit healer DESCRIPTION guessed
    "UNIT_NPC_FLAG_SPIRITGUIDE": 0x00008000,     # TITLE is spirit guide DESCRIPTION guessed
    "UNIT_NPC_FLAG_INNKEEPER": 0x00010000,     # TITLE is innkeeper
    "UNIT_NPC_FLAG_BANKER": 0x00020000,     # TITLE is banker DESCRIPTION 100%
    "UNIT_NPC_FLAG_PETITIONER": 0x00040000,  # TITLE handles guild/arena petitions DESCRIPTION 100% 0xC0000 = guild petitions, 0x40000 = arena team petitions
    "UNIT_NPC_FLAG_TABARDDESIGNER": 0x00080000,     # TITLE is guild tabard designer DESCRIPTION 100%
    "UNIT_NPC_FLAG_BATTLEMASTER": 0x00100000,     # TITLE is battlemaster DESCRIPTION 100%
    "UNIT_NPC_FLAG_AUCTIONEER": 0x00200000,     # TITLE is auctioneer DESCRIPTION 100%
    "UNIT_NPC_FLAG_STABLEMASTER": 0x00400000,     # TITLE is stable master DESCRIPTION 100%
    "UNIT_NPC_FLAG_GUILD_BANKER": 0x00800000,     # TITLE is guild banker DESCRIPTION
    "UNIT_NPC_FLAG_SPELLCLICK": 0x01000000,     # TITLE has spell click enabled
    "UNIT_NPC_FLAG_PLAYER_VEHICLE": 0x02000000,     # TITLE is player vehicle DESCRIPTION players with mounts that have vehicle data should have it set
    "UNIT_NPC_FLAG_MAILBOX": 0x04000000,     # TITLE is mailbox
    "UNIT_NPC_FLAG_ARTIFACT_POWER_RESPEC": 0x08000000,     # TITLE can reset artifact powers
    "UNIT_NPC_FLAG_TRANSMOGRIFIER": 0x10000000,     # TITLE transmogrification
    "UNIT_NPC_FLAG_VAULTKEEPER": 0x20000000,     # TITLE is void storage
    "UNIT_NPC_FLAG_WILD_BATTLE_PET": 0x40000000,     # TITLE is wild battle pet DESCRIPTION Pet that player can fight (Battle Pet)
    "UNIT_NPC_FLAG_BLACK_MARKET": 0x80000000      # TITLE is black market
}

VMangos_NPCFlags = {
"UNIT_NPC_FLAG_NONE": 0x00000000,
"UNIT_NPC_FLAG_GOSSIP": 0x00000001,       # 100%
"UNIT_NPC_FLAG_QUESTGIVER": 0x00000002,       # 100%
"UNIT_NPC_FLAG_VENDOR": 0x00000004,       # 100%
"UNIT_NPC_FLAG_FLIGHTMASTER": 0x00000008,       # 100%
"UNIT_NPC_FLAG_TRAINER": 0x00000010,       # 100%
"UNIT_NPC_FLAG_SPIRITHEALER": 0x00000020,       # guessed
"UNIT_NPC_FLAG_SPIRITGUIDE": 0x00000040,       # guessed
"UNIT_NPC_FLAG_INNKEEPER": 0x00000080,       # 100%
"UNIT_NPC_FLAG_BANKER": 0x00000100,       # 100%
"UNIT_NPC_FLAG_PETITIONER": 0x00000200,       # 100% 0xC0000 = guild petitions
"UNIT_NPC_FLAG_TABARDDESIGNER": 0x00000400,       # 100%
"UNIT_NPC_FLAG_BATTLEMASTER": 0x00000800,       # 100%
"UNIT_NPC_FLAG_AUCTIONEER": 0x00001000,       # 100%
"UNIT_NPC_FLAG_STABLEMASTER": 0x00002000,       # 100%
"UNIT_NPC_FLAG_REPAIR": 0x00004000,       # 100%
}

def ConvertNPCFlags(vmangos_flags):
    trinity_flags = 0
    
    for key, val in VMangos_NPCFlags.items():
        if vmangos_flags & val:
            trinity_flags = trinity_flags | NPCFlags[key]
    
    return trinity_flags