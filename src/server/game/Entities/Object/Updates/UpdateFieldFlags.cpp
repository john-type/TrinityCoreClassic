/*
 * Copyright (C) 2008-2018 TrinityCore <https://www.trinitycore.org/>
 *
 * This program is free software; you can redistribute it and/or modify it
 * under the terms of the GNU General Public License as published by the
 * Free Software Foundation; either version 2 of the License, or (at your
 * option) any later version.
 *
 * This program is distributed in the hope that it will be useful, but WITHOUT
 * ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
 * FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for
 * more details.
 *
 * You should have received a copy of the GNU General Public License along
 * with this program. If not, see <http://www.gnu.org/licenses/>.
 */

#include "UpdateFieldFlags.h"

using namespace UF;

uint32 ItemUpdateFieldFlags[CONTAINER_END] = 
{
    UF_FLAG_PUBLIC,                                         // OBJECT_FIELD_GUID
    UF_FLAG_PUBLIC,                                         // OBJECT_FIELD_GUID+1
    UF_FLAG_PUBLIC,                                         // OBJECT_FIELD_GUID+2
    UF_FLAG_PUBLIC,                                         // OBJECT_FIELD_GUID+3
    UF_FLAG_DYNAMIC,                                        // OBJECT_FIELD_ENTRY
    UF_FLAG_DYNAMIC | UF_FLAG_URGENT,                       // OBJECT_DYNAMIC_FLAGS
    UF_FLAG_PUBLIC,                                         // OBJECT_FIELD_SCALE_X
    UF_FLAG_PUBLIC,                                         // ITEM_FIELD_OWNER
    UF_FLAG_PUBLIC,                                         // ITEM_FIELD_OWNER+1
    UF_FLAG_PUBLIC,                                         // ITEM_FIELD_OWNER+2
    UF_FLAG_PUBLIC,                                         // ITEM_FIELD_OWNER+3
    UF_FLAG_PUBLIC,                                         // ITEM_FIELD_CONTAINED
    UF_FLAG_PUBLIC,                                         // ITEM_FIELD_CONTAINED+1
    UF_FLAG_PUBLIC,                                         // ITEM_FIELD_CONTAINED+2
    UF_FLAG_PUBLIC,                                         // ITEM_FIELD_CONTAINED+3
    UF_FLAG_PUBLIC,                                         // ITEM_FIELD_CREATOR
    UF_FLAG_PUBLIC,                                         // ITEM_FIELD_CREATOR+1
    UF_FLAG_PUBLIC,                                         // ITEM_FIELD_CREATOR+2
    UF_FLAG_PUBLIC,                                         // ITEM_FIELD_CREATOR+3
    UF_FLAG_PUBLIC,                                         // ITEM_FIELD_GIFTCREATOR
    UF_FLAG_PUBLIC,                                         // ITEM_FIELD_GIFTCREATOR+1
    UF_FLAG_PUBLIC,                                         // ITEM_FIELD_GIFTCREATOR+2
    UF_FLAG_PUBLIC,                                         // ITEM_FIELD_GIFTCREATOR+3
    UF_FLAG_OWNER,                                          // ITEM_FIELD_STACK_COUNT
    UF_FLAG_OWNER,                                          // ITEM_FIELD_DURATION
    UF_FLAG_OWNER,                                          // ITEM_FIELD_SPELL_CHARGES
    UF_FLAG_OWNER,                                          // ITEM_FIELD_SPELL_CHARGES+1
    UF_FLAG_OWNER,                                          // ITEM_FIELD_SPELL_CHARGES+2
    UF_FLAG_OWNER,                                          // ITEM_FIELD_SPELL_CHARGES+3
    UF_FLAG_OWNER,                                          // ITEM_FIELD_SPELL_CHARGES+4
    UF_FLAG_PUBLIC,                                         // ITEM_FIELD_FLAGS
    UF_FLAG_PUBLIC,                                         // ITEM_FIELD_ENCHANTMENT
    UF_FLAG_PUBLIC,                                         // ITEM_FIELD_ENCHANTMENT+1
    UF_FLAG_PUBLIC,                                         // ITEM_FIELD_ENCHANTMENT+2
    UF_FLAG_PUBLIC,                                         // ITEM_FIELD_ENCHANTMENT+3
    UF_FLAG_PUBLIC,                                         // ITEM_FIELD_ENCHANTMENT+4
    UF_FLAG_PUBLIC,                                         // ITEM_FIELD_ENCHANTMENT+5
    UF_FLAG_PUBLIC,                                         // ITEM_FIELD_ENCHANTMENT+6
    UF_FLAG_PUBLIC,                                         // ITEM_FIELD_ENCHANTMENT+7
    UF_FLAG_PUBLIC,                                         // ITEM_FIELD_ENCHANTMENT+8
    UF_FLAG_PUBLIC,                                         // ITEM_FIELD_ENCHANTMENT+9
    UF_FLAG_PUBLIC,                                         // ITEM_FIELD_ENCHANTMENT+10
    UF_FLAG_PUBLIC,                                         // ITEM_FIELD_ENCHANTMENT+11
    UF_FLAG_PUBLIC,                                         // ITEM_FIELD_ENCHANTMENT+12
    UF_FLAG_PUBLIC,                                         // ITEM_FIELD_ENCHANTMENT+13
    UF_FLAG_PUBLIC,                                         // ITEM_FIELD_ENCHANTMENT+14
    UF_FLAG_PUBLIC,                                         // ITEM_FIELD_ENCHANTMENT+15
    UF_FLAG_PUBLIC,                                         // ITEM_FIELD_ENCHANTMENT+16
    UF_FLAG_PUBLIC,                                         // ITEM_FIELD_ENCHANTMENT+17
    UF_FLAG_PUBLIC,                                         // ITEM_FIELD_ENCHANTMENT+18
    UF_FLAG_PUBLIC,                                         // ITEM_FIELD_ENCHANTMENT+19
    UF_FLAG_PUBLIC,                                         // ITEM_FIELD_ENCHANTMENT+20
    UF_FLAG_PUBLIC,                                         // ITEM_FIELD_ENCHANTMENT+21
    UF_FLAG_PUBLIC,                                         // ITEM_FIELD_ENCHANTMENT+22
    UF_FLAG_PUBLIC,                                         // ITEM_FIELD_ENCHANTMENT+23
    UF_FLAG_PUBLIC,                                         // ITEM_FIELD_ENCHANTMENT+24
    UF_FLAG_PUBLIC,                                         // ITEM_FIELD_ENCHANTMENT+25
    UF_FLAG_PUBLIC,                                         // ITEM_FIELD_ENCHANTMENT+26
    UF_FLAG_PUBLIC,                                         // ITEM_FIELD_ENCHANTMENT+27
    UF_FLAG_PUBLIC,                                         // ITEM_FIELD_ENCHANTMENT+28
    UF_FLAG_PUBLIC,                                         // ITEM_FIELD_ENCHANTMENT+29
    UF_FLAG_PUBLIC,                                         // ITEM_FIELD_ENCHANTMENT+30
    UF_FLAG_PUBLIC,                                         // ITEM_FIELD_ENCHANTMENT+31
    UF_FLAG_PUBLIC,                                         // ITEM_FIELD_ENCHANTMENT+32
    UF_FLAG_PUBLIC,                                         // ITEM_FIELD_ENCHANTMENT+33
    UF_FLAG_PUBLIC,                                         // ITEM_FIELD_ENCHANTMENT+34
    UF_FLAG_PUBLIC,                                         // ITEM_FIELD_ENCHANTMENT+35
    UF_FLAG_PUBLIC,                                         // ITEM_FIELD_ENCHANTMENT+36
    UF_FLAG_PUBLIC,                                         // ITEM_FIELD_ENCHANTMENT+37
    UF_FLAG_PUBLIC,                                         // ITEM_FIELD_ENCHANTMENT+38
    UF_FLAG_PUBLIC,                                         // ITEM_FIELD_PROPERTY_SEED
    UF_FLAG_PUBLIC,                                         // ITEM_FIELD_RANDOM_PROPERTIES_ID
    UF_FLAG_OWNER,                                          // ITEM_FIELD_DURABILITY
    UF_FLAG_OWNER,                                          // ITEM_FIELD_MAXDURABILITY
    UF_FLAG_PUBLIC,                                         // ITEM_FIELD_CREATE_PLAYED_TIME
    UF_FLAG_OWNER,                                          // ITEM_FIELD_MODIFIERS_MASK
    UF_FLAG_PUBLIC,                                         // ITEM_FIELD_CONTEXT
    UF_FLAG_OWNER,                                          // ITEM_FIELD_ARTIFACT_XP
    UF_FLAG_OWNER,                                          // ITEM_FIELD_ARTIFACT_XP+1
    UF_FLAG_OWNER,                                          // ITEM_FIELD_APPEARANCE_MOD_ID
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+1
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+2
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+3
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+4
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+5
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+6
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+7
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+8
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+9
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+10
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+11
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+12
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+13
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+14
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+15
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+16
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+17
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+18
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+19
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+20
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+21
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+22
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+23
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+24
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+25
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+26
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+27
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+28
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+29
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+30
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+31
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+32
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+33
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+34
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+35
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+36
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+37
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+38
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+39
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+40
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+41
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+42
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+43
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+44
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+45
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+46
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+47
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+48
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+49
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+50
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+51
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+52
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+53
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+54
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+55
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+56
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+57
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+58
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+59
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+60
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+61
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+62
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+63
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+64
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+65
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+66
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+67
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+68
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+69
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+70
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+71
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+72
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+73
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+74
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+75
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+76
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+77
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+78
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+79
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+80
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+81
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+82
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+83
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+84
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+85
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+86
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+87
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+88
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+89
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+90
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+91
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+92
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+93
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+94
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+95
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+96
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+97
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+98
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+99
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+100
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+101
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+102
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+103
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+104
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+105
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+106
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+107
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+108
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+109
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+110
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+111
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+112
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+113
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+114
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+115
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+116
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+117
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+118
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+119
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+120
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+121
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+122
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+123
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+124
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+125
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+126
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+127
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+128
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+129
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+130
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+131
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+132
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+133
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+134
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+135
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+136
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+137
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+138
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+139
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+140
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+141
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+142
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_SLOT_1+143
    UF_FLAG_PUBLIC,                                         // CONTAINER_FIELD_NUM_SLOTS
};

uint32 ItemDynamicUpdateFieldFlags[CONTAINER_DYNAMIC_END] = 
{
    UF_FLAG_OWNER,                                          // ITEM_DYNAMIC_FIELD_MODIFIERS
    UF_FLAG_OWNER | UF_FLAG_0x100,                          // ITEM_DYNAMIC_FIELD_BONUSLIST_IDS
    UF_FLAG_OWNER,                                          // ITEM_DYNAMIC_FIELD_ARTIFACT_POWERS
    UF_FLAG_OWNER,                                          // ITEM_DYNAMIC_FIELD_GEMS
};

uint32 UnitUpdateFieldFlags[PLAYER_END] = 
{
    UF_FLAG_PUBLIC,                                         // OBJECT_FIELD_GUID
    UF_FLAG_PUBLIC,                                         // OBJECT_FIELD_GUID+1
    UF_FLAG_PUBLIC,                                         // OBJECT_FIELD_GUID+2
    UF_FLAG_PUBLIC,                                         // OBJECT_FIELD_GUID+3
    UF_FLAG_DYNAMIC,                                        // OBJECT_FIELD_ENTRY
    UF_FLAG_DYNAMIC | UF_FLAG_URGENT,                       // OBJECT_DYNAMIC_FLAGS
    UF_FLAG_PUBLIC,                                         // OBJECT_FIELD_SCALE_X
    UF_FLAG_PUBLIC,                                         // UNIT_FIELD_CHARM
    UF_FLAG_PUBLIC,                                         // UNIT_FIELD_CHARM+1
    UF_FLAG_PUBLIC,                                         // UNIT_FIELD_CHARM+2
    UF_FLAG_PUBLIC,                                         // UNIT_FIELD_CHARM+3
    UF_FLAG_PUBLIC,                                         // UNIT_FIELD_SUMMON
    UF_FLAG_PUBLIC,                                         // UNIT_FIELD_SUMMON+1
    UF_FLAG_PUBLIC,                                         // UNIT_FIELD_SUMMON+2
    UF_FLAG_PUBLIC,                                         // UNIT_FIELD_SUMMON+3
    UF_FLAG_PRIVATE,                                        // UNIT_FIELD_CRITTER
    UF_FLAG_PRIVATE,                                        // UNIT_FIELD_CRITTER+1
    UF_FLAG_PRIVATE,                                        // UNIT_FIELD_CRITTER+2
    UF_FLAG_PRIVATE,                                        // UNIT_FIELD_CRITTER+3
    UF_FLAG_PUBLIC,                                         // UNIT_FIELD_CHARMEDBY
    UF_FLAG_PUBLIC,                                         // UNIT_FIELD_CHARMEDBY+1
    UF_FLAG_PUBLIC,                                         // UNIT_FIELD_CHARMEDBY+2
    UF_FLAG_PUBLIC,                                         // UNIT_FIELD_CHARMEDBY+3
    UF_FLAG_PUBLIC,                                         // UNIT_FIELD_SUMMONEDBY
    UF_FLAG_PUBLIC,                                         // UNIT_FIELD_SUMMONEDBY+1
    UF_FLAG_PUBLIC,                                         // UNIT_FIELD_SUMMONEDBY+2
    UF_FLAG_PUBLIC,                                         // UNIT_FIELD_SUMMONEDBY+3
    UF_FLAG_PUBLIC,                                         // UNIT_FIELD_CREATEDBY
    UF_FLAG_PUBLIC,                                         // UNIT_FIELD_CREATEDBY+1
    UF_FLAG_PUBLIC,                                         // UNIT_FIELD_CREATEDBY+2
    UF_FLAG_PUBLIC,                                         // UNIT_FIELD_CREATEDBY+3
    UF_FLAG_PUBLIC,                                         // UNIT_FIELD_DEMON_CREATOR
    UF_FLAG_PUBLIC,                                         // UNIT_FIELD_DEMON_CREATOR+1
    UF_FLAG_PUBLIC,                                         // UNIT_FIELD_DEMON_CREATOR+2
    UF_FLAG_PUBLIC,                                         // UNIT_FIELD_DEMON_CREATOR+3
    UF_FLAG_PUBLIC,                                         // UNIT_FIELD_LOOK_AT_CONTROLLER_TARGET
    UF_FLAG_PUBLIC,                                         // UNIT_FIELD_LOOK_AT_CONTROLLER_TARGET+1
    UF_FLAG_PUBLIC,                                         // UNIT_FIELD_LOOK_AT_CONTROLLER_TARGET+2
    UF_FLAG_PUBLIC,                                         // UNIT_FIELD_LOOK_AT_CONTROLLER_TARGET+3
    UF_FLAG_PUBLIC,                                         // UNIT_FIELD_TARGET
    UF_FLAG_PUBLIC,                                         // UNIT_FIELD_TARGET+1
    UF_FLAG_PUBLIC,                                         // UNIT_FIELD_TARGET+2
    UF_FLAG_PUBLIC,                                         // UNIT_FIELD_TARGET+3
    UF_FLAG_PUBLIC,                                         // UNIT_FIELD_BATTLE_PET_COMPANION_GUID
    UF_FLAG_PUBLIC,                                         // UNIT_FIELD_BATTLE_PET_COMPANION_GUID+1
    UF_FLAG_PUBLIC,                                         // UNIT_FIELD_BATTLE_PET_COMPANION_GUID+2
    UF_FLAG_PUBLIC,                                         // UNIT_FIELD_BATTLE_PET_COMPANION_GUID+3
    UF_FLAG_PUBLIC,                                         // UNIT_FIELD_BATTLE_PET_DB_ID
    UF_FLAG_PUBLIC,                                         // UNIT_FIELD_BATTLE_PET_DB_ID+1
    UF_FLAG_PUBLIC | UF_FLAG_URGENT,                        // UNIT_FIELD_CHANNEL_DATA
    UF_FLAG_PUBLIC | UF_FLAG_URGENT,                        // UNIT_FIELD_CHANNEL_DATA+1
    UF_FLAG_PUBLIC,                                         // UNIT_FIELD_SUMMONED_BY_HOME_REALM
    UF_FLAG_PUBLIC,                                         // UNIT_FIELD_BYTES_0
    UF_FLAG_PUBLIC,                                         // UNIT_FIELD_DISPLAY_POWER
    UF_FLAG_PUBLIC,                                         // UNIT_FIELD_OVERRIDE_DISPLAY_POWER_ID
    UF_FLAG_DYNAMIC,                                        // UNIT_FIELD_HEALTH
    UF_FLAG_DYNAMIC,                                        // UNIT_FIELD_HEALTH+1
    UF_FLAG_PUBLIC | UF_FLAG_URGENT_SELF_ONLY,              // UNIT_FIELD_POWER
    UF_FLAG_PUBLIC | UF_FLAG_URGENT_SELF_ONLY,              // UNIT_FIELD_POWER+1
    UF_FLAG_PUBLIC | UF_FLAG_URGENT_SELF_ONLY,              // UNIT_FIELD_POWER+2
    UF_FLAG_PUBLIC | UF_FLAG_URGENT_SELF_ONLY,              // UNIT_FIELD_POWER+3
    UF_FLAG_PUBLIC | UF_FLAG_URGENT_SELF_ONLY,              // UNIT_FIELD_POWER+4
    UF_FLAG_PUBLIC | UF_FLAG_URGENT_SELF_ONLY,              // UNIT_FIELD_POWER+5
    UF_FLAG_DYNAMIC,                                        // UNIT_FIELD_MAXHEALTH
    UF_FLAG_DYNAMIC,                                        // UNIT_FIELD_MAXHEALTH+1
    UF_FLAG_PUBLIC,                                         // UNIT_FIELD_MAXPOWER
    UF_FLAG_PUBLIC,                                         // UNIT_FIELD_MAXPOWER+1
    UF_FLAG_PUBLIC,                                         // UNIT_FIELD_MAXPOWER+2
    UF_FLAG_PUBLIC,                                         // UNIT_FIELD_MAXPOWER+3
    UF_FLAG_PUBLIC,                                         // UNIT_FIELD_MAXPOWER+4
    UF_FLAG_PUBLIC,                                         // UNIT_FIELD_MAXPOWER+5
    UF_FLAG_PRIVATE | UF_FLAG_OWNER | UF_FLAG_UNIT_ALL,     // UNIT_FIELD_MOD_POWER_REGEN
    UF_FLAG_PRIVATE | UF_FLAG_OWNER | UF_FLAG_UNIT_ALL,     // UNIT_FIELD_MOD_POWER_REGEN+1
    UF_FLAG_PRIVATE | UF_FLAG_OWNER | UF_FLAG_UNIT_ALL,     // UNIT_FIELD_MOD_POWER_REGEN+2
    UF_FLAG_PRIVATE | UF_FLAG_OWNER | UF_FLAG_UNIT_ALL,     // UNIT_FIELD_MOD_POWER_REGEN+3
    UF_FLAG_PRIVATE | UF_FLAG_OWNER | UF_FLAG_UNIT_ALL,     // UNIT_FIELD_MOD_POWER_REGEN+4
    UF_FLAG_PRIVATE | UF_FLAG_OWNER | UF_FLAG_UNIT_ALL,     // UNIT_FIELD_MOD_POWER_REGEN+5
    UF_FLAG_PUBLIC,                                         // UNIT_FIELD_LEVEL
    UF_FLAG_PUBLIC,                                         // UNIT_FIELD_EFFECTIVE_LEVEL
    UF_FLAG_PUBLIC,                                         // UNIT_FIELD_CONTENT_TUNING_ID
    UF_FLAG_PUBLIC,                                         // UNIT_FIELD_SCALING_LEVEL_MIN
    UF_FLAG_PUBLIC,                                         // UNIT_FIELD_SCALING_LEVEL_MAX
    UF_FLAG_PUBLIC,                                         // UNIT_FIELD_SCALING_LEVEL_DELTA
    UF_FLAG_PUBLIC,                                         // UNIT_FIELD_SCALING_FACTION_GROUP
    UF_FLAG_PUBLIC,                                         // UNIT_FIELD_SCALING_HEALTH_ITEM_LEVEL_CURVE_ID
    UF_FLAG_PUBLIC,                                         // UNIT_FIELD_SCALING_DAMAGE_ITEM_LEVEL_CURVE_ID
    UF_FLAG_PUBLIC,                                         // UNIT_FIELD_FACTIONTEMPLATE
    UF_FLAG_PUBLIC,                                         // UNIT_VIRTUAL_ITEM_SLOT_ID
    UF_FLAG_PUBLIC,                                         // UNIT_VIRTUAL_ITEM_SLOT_ID+1
    UF_FLAG_PUBLIC,                                         // UNIT_VIRTUAL_ITEM_SLOT_ID+2
    UF_FLAG_PUBLIC,                                         // UNIT_VIRTUAL_ITEM_SLOT_ID+3
    UF_FLAG_PUBLIC,                                         // UNIT_VIRTUAL_ITEM_SLOT_ID+4
    UF_FLAG_PUBLIC,                                         // UNIT_VIRTUAL_ITEM_SLOT_ID+5
    UF_FLAG_PUBLIC | UF_FLAG_URGENT,                        // UNIT_FIELD_FLAGS
    UF_FLAG_PUBLIC | UF_FLAG_URGENT,                        // UNIT_FIELD_FLAGS_2
    UF_FLAG_PUBLIC | UF_FLAG_URGENT,                        // UNIT_FIELD_FLAGS_3
    UF_FLAG_PUBLIC,                                         // UNIT_FIELD_AURASTATE
    UF_FLAG_PUBLIC,                                         // UNIT_FIELD_BASEATTACKTIME
    UF_FLAG_PUBLIC,                                         // UNIT_FIELD_BASEATTACKTIME+1
    UF_FLAG_PRIVATE,                                        // UNIT_FIELD_RANGEDATTACKTIME
    UF_FLAG_PUBLIC,                                         // UNIT_FIELD_BOUNDINGRADIUS
    UF_FLAG_PUBLIC,                                         // UNIT_FIELD_COMBATREACH
    UF_FLAG_DYNAMIC | UF_FLAG_URGENT,                       // UNIT_FIELD_DISPLAYID
    UF_FLAG_DYNAMIC | UF_FLAG_URGENT,                       // UNIT_FIELD_DISPLAY_SCALE
    UF_FLAG_PUBLIC | UF_FLAG_URGENT,                        // UNIT_FIELD_NATIVEDISPLAYID
    UF_FLAG_PUBLIC | UF_FLAG_URGENT,                        // UNIT_FIELD_NATIVE_X_DISPLAY_SCALE
    UF_FLAG_PUBLIC | UF_FLAG_URGENT,                        // UNIT_FIELD_MOUNTDISPLAYID
    UF_FLAG_PRIVATE | UF_FLAG_OWNER | UF_FLAG_SPECIAL_INFO, // UNIT_FIELD_MINDAMAGE
    UF_FLAG_PRIVATE | UF_FLAG_OWNER | UF_FLAG_SPECIAL_INFO, // UNIT_FIELD_MAXDAMAGE
    UF_FLAG_PRIVATE | UF_FLAG_OWNER | UF_FLAG_SPECIAL_INFO, // UNIT_FIELD_MINOFFHANDDAMAGE
    UF_FLAG_PRIVATE | UF_FLAG_OWNER | UF_FLAG_SPECIAL_INFO, // UNIT_FIELD_MAXOFFHANDDAMAGE
    UF_FLAG_PUBLIC,                                         // UNIT_FIELD_BYTES_1
    UF_FLAG_PUBLIC,                                         // UNIT_FIELD_PETNUMBER
    UF_FLAG_PUBLIC,                                         // UNIT_FIELD_PET_NAME_TIMESTAMP
    UF_FLAG_OWNER,                                          // UNIT_FIELD_PETEXPERIENCE
    UF_FLAG_OWNER,                                          // UNIT_FIELD_PETNEXTLEVELXP
    UF_FLAG_PUBLIC,                                         // UNIT_MOD_CAST_SPEED
    UF_FLAG_PUBLIC,                                         // UNIT_MOD_CAST_HASTE
    UF_FLAG_PUBLIC,                                         // UNIT_FIELD_MOD_HASTE
    UF_FLAG_PUBLIC,                                         // UNIT_FIELD_MOD_RANGED_HASTE
    UF_FLAG_PUBLIC,                                         // UNIT_FIELD_MOD_HASTE_REGEN
    UF_FLAG_PUBLIC,                                         // UNIT_FIELD_MOD_TIME_RATE
    UF_FLAG_PUBLIC,                                         // UNIT_CREATED_BY_SPELL
    UF_FLAG_PUBLIC | UF_FLAG_DYNAMIC,                       // UNIT_NPC_FLAGS
    UF_FLAG_PUBLIC | UF_FLAG_DYNAMIC,                       // UNIT_NPC_FLAGS+1
    UF_FLAG_PUBLIC,                                         // UNIT_NPC_EMOTESTATE
    UF_FLAG_OWNER,                                          // UNIT_FIELD_TRAINING_POINTS_TOTAL
    UF_FLAG_PRIVATE | UF_FLAG_OWNER,                        // UNIT_FIELD_STAT
    UF_FLAG_PRIVATE | UF_FLAG_OWNER,                        // UNIT_FIELD_STAT+1
    UF_FLAG_PRIVATE | UF_FLAG_OWNER,                        // UNIT_FIELD_STAT+2
    UF_FLAG_PRIVATE | UF_FLAG_OWNER,                        // UNIT_FIELD_STAT+3
    UF_FLAG_PRIVATE | UF_FLAG_OWNER,                        // UNIT_FIELD_STAT+4
    UF_FLAG_PRIVATE | UF_FLAG_OWNER,                        // UNIT_FIELD_POSSTAT
    UF_FLAG_PRIVATE | UF_FLAG_OWNER,                        // UNIT_FIELD_POSSTAT+1
    UF_FLAG_PRIVATE | UF_FLAG_OWNER,                        // UNIT_FIELD_POSSTAT+2
    UF_FLAG_PRIVATE | UF_FLAG_OWNER,                        // UNIT_FIELD_POSSTAT+3
    UF_FLAG_PRIVATE | UF_FLAG_OWNER,                        // UNIT_FIELD_POSSTAT+4
    UF_FLAG_PRIVATE | UF_FLAG_OWNER,                        // UNIT_FIELD_NEGSTAT
    UF_FLAG_PRIVATE | UF_FLAG_OWNER,                        // UNIT_FIELD_NEGSTAT+1
    UF_FLAG_PRIVATE | UF_FLAG_OWNER,                        // UNIT_FIELD_NEGSTAT+2
    UF_FLAG_PRIVATE | UF_FLAG_OWNER,                        // UNIT_FIELD_NEGSTAT+3
    UF_FLAG_PRIVATE | UF_FLAG_OWNER,                        // UNIT_FIELD_NEGSTAT+4
    UF_FLAG_PRIVATE | UF_FLAG_OWNER | UF_FLAG_SPECIAL_INFO, // UNIT_FIELD_RESISTANCES
    UF_FLAG_PRIVATE | UF_FLAG_OWNER | UF_FLAG_SPECIAL_INFO, // UNIT_FIELD_RESISTANCES+1
    UF_FLAG_PRIVATE | UF_FLAG_OWNER | UF_FLAG_SPECIAL_INFO, // UNIT_FIELD_RESISTANCES+2
    UF_FLAG_PRIVATE | UF_FLAG_OWNER | UF_FLAG_SPECIAL_INFO, // UNIT_FIELD_RESISTANCES+3
    UF_FLAG_PRIVATE | UF_FLAG_OWNER | UF_FLAG_SPECIAL_INFO, // UNIT_FIELD_RESISTANCES+4
    UF_FLAG_PRIVATE | UF_FLAG_OWNER | UF_FLAG_SPECIAL_INFO, // UNIT_FIELD_RESISTANCES+5
    UF_FLAG_PRIVATE | UF_FLAG_OWNER | UF_FLAG_SPECIAL_INFO, // UNIT_FIELD_RESISTANCES+6
    UF_FLAG_PRIVATE | UF_FLAG_OWNER,                        // UNIT_FIELD_RESISTANCEBUFFMODSPOSITIVE
    UF_FLAG_PRIVATE | UF_FLAG_OWNER,                        // UNIT_FIELD_RESISTANCEBUFFMODSPOSITIVE+1
    UF_FLAG_PRIVATE | UF_FLAG_OWNER,                        // UNIT_FIELD_RESISTANCEBUFFMODSPOSITIVE+2
    UF_FLAG_PRIVATE | UF_FLAG_OWNER,                        // UNIT_FIELD_RESISTANCEBUFFMODSPOSITIVE+3
    UF_FLAG_PRIVATE | UF_FLAG_OWNER,                        // UNIT_FIELD_RESISTANCEBUFFMODSPOSITIVE+4
    UF_FLAG_PRIVATE | UF_FLAG_OWNER,                        // UNIT_FIELD_RESISTANCEBUFFMODSPOSITIVE+5
    UF_FLAG_PRIVATE | UF_FLAG_OWNER,                        // UNIT_FIELD_RESISTANCEBUFFMODSPOSITIVE+6
    UF_FLAG_PRIVATE | UF_FLAG_OWNER,                        // UNIT_FIELD_RESISTANCEBUFFMODSNEGATIVE
    UF_FLAG_PRIVATE | UF_FLAG_OWNER,                        // UNIT_FIELD_RESISTANCEBUFFMODSNEGATIVE+1
    UF_FLAG_PRIVATE | UF_FLAG_OWNER,                        // UNIT_FIELD_RESISTANCEBUFFMODSNEGATIVE+2
    UF_FLAG_PRIVATE | UF_FLAG_OWNER,                        // UNIT_FIELD_RESISTANCEBUFFMODSNEGATIVE+3
    UF_FLAG_PRIVATE | UF_FLAG_OWNER,                        // UNIT_FIELD_RESISTANCEBUFFMODSNEGATIVE+4
    UF_FLAG_PRIVATE | UF_FLAG_OWNER,                        // UNIT_FIELD_RESISTANCEBUFFMODSNEGATIVE+5
    UF_FLAG_PRIVATE | UF_FLAG_OWNER,                        // UNIT_FIELD_RESISTANCEBUFFMODSNEGATIVE+6
    UF_FLAG_PUBLIC,                                         // UNIT_FIELD_BASE_MANA
    UF_FLAG_PRIVATE | UF_FLAG_OWNER,                        // UNIT_FIELD_BASE_HEALTH
    UF_FLAG_PUBLIC,                                         // UNIT_FIELD_BYTES_2
    UF_FLAG_PRIVATE | UF_FLAG_OWNER,                        // UNIT_FIELD_ATTACK_POWER
    UF_FLAG_PRIVATE | UF_FLAG_OWNER,                        // UNIT_FIELD_ATTACK_POWER_MOD_POS
    UF_FLAG_PRIVATE | UF_FLAG_OWNER,                        // UNIT_FIELD_ATTACK_POWER_MOD_NEG
    UF_FLAG_PRIVATE | UF_FLAG_OWNER,                        // UNIT_FIELD_ATTACK_POWER_MULTIPLIER
    UF_FLAG_PRIVATE | UF_FLAG_OWNER,                        // UNIT_FIELD_RANGED_ATTACK_POWER
    UF_FLAG_PRIVATE | UF_FLAG_OWNER,                        // UNIT_FIELD_RANGED_ATTACK_POWER_MOD_POS
    UF_FLAG_PRIVATE | UF_FLAG_OWNER,                        // UNIT_FIELD_RANGED_ATTACK_POWER_MOD_NEG
    UF_FLAG_PRIVATE | UF_FLAG_OWNER,                        // UNIT_FIELD_RANGED_ATTACK_POWER_MULTIPLIER
    UF_FLAG_PRIVATE | UF_FLAG_OWNER,                        // UNIT_FIELD_ATTACK_SPEED_AURA
    UF_FLAG_PRIVATE | UF_FLAG_OWNER,                        // UNIT_FIELD_LIFESTEAL
    UF_FLAG_PRIVATE | UF_FLAG_OWNER,                        // UNIT_FIELD_MINRANGEDDAMAGE
    UF_FLAG_PRIVATE | UF_FLAG_OWNER,                        // UNIT_FIELD_MAXRANGEDDAMAGE
    UF_FLAG_PRIVATE | UF_FLAG_OWNER,                        // UNIT_FIELD_POWER_COST_MODIFIER
    UF_FLAG_PRIVATE | UF_FLAG_OWNER,                        // UNIT_FIELD_POWER_COST_MODIFIER+1
    UF_FLAG_PRIVATE | UF_FLAG_OWNER,                        // UNIT_FIELD_POWER_COST_MODIFIER+2
    UF_FLAG_PRIVATE | UF_FLAG_OWNER,                        // UNIT_FIELD_POWER_COST_MODIFIER+3
    UF_FLAG_PRIVATE | UF_FLAG_OWNER,                        // UNIT_FIELD_POWER_COST_MODIFIER+4
    UF_FLAG_PRIVATE | UF_FLAG_OWNER,                        // UNIT_FIELD_POWER_COST_MODIFIER+5
    UF_FLAG_PRIVATE | UF_FLAG_OWNER,                        // UNIT_FIELD_POWER_COST_MODIFIER+6
    UF_FLAG_PRIVATE | UF_FLAG_OWNER,                        // UNIT_FIELD_POWER_COST_MULTIPLIER
    UF_FLAG_PRIVATE | UF_FLAG_OWNER,                        // UNIT_FIELD_POWER_COST_MULTIPLIER+1
    UF_FLAG_PRIVATE | UF_FLAG_OWNER,                        // UNIT_FIELD_POWER_COST_MULTIPLIER+2
    UF_FLAG_PRIVATE | UF_FLAG_OWNER,                        // UNIT_FIELD_POWER_COST_MULTIPLIER+3
    UF_FLAG_PRIVATE | UF_FLAG_OWNER,                        // UNIT_FIELD_POWER_COST_MULTIPLIER+4
    UF_FLAG_PRIVATE | UF_FLAG_OWNER,                        // UNIT_FIELD_POWER_COST_MULTIPLIER+5
    UF_FLAG_PRIVATE | UF_FLAG_OWNER,                        // UNIT_FIELD_POWER_COST_MULTIPLIER+6
    UF_FLAG_PRIVATE | UF_FLAG_OWNER,                        // UNIT_FIELD_MAXHEALTHMODIFIER
    UF_FLAG_PUBLIC,                                         // UNIT_FIELD_HOVERHEIGHT
    UF_FLAG_PUBLIC,                                         // UNIT_FIELD_MIN_ITEM_LEVEL_CUTOFF
    UF_FLAG_PUBLIC,                                         // UNIT_FIELD_MIN_ITEM_LEVEL
    UF_FLAG_PUBLIC,                                         // UNIT_FIELD_MAXITEMLEVEL
    UF_FLAG_PUBLIC,                                         // UNIT_FIELD_WILD_BATTLEPET_LEVEL
    UF_FLAG_PUBLIC,                                         // UNIT_FIELD_BATTLEPET_COMPANION_NAME_TIMESTAMP
    UF_FLAG_PUBLIC,                                         // UNIT_FIELD_INTERACT_SPELLID
    UF_FLAG_DYNAMIC | UF_FLAG_URGENT,                       // UNIT_FIELD_STATE_SPELL_VISUAL_ID
    UF_FLAG_DYNAMIC | UF_FLAG_URGENT,                       // UNIT_FIELD_STATE_ANIM_ID
    UF_FLAG_DYNAMIC | UF_FLAG_URGENT,                       // UNIT_FIELD_STATE_ANIM_KIT_ID
    UF_FLAG_DYNAMIC | UF_FLAG_URGENT,                       // UNIT_FIELD_STATE_WORLD_EFFECT_ID
    UF_FLAG_DYNAMIC | UF_FLAG_URGENT,                       // UNIT_FIELD_STATE_WORLD_EFFECT_ID+1
    UF_FLAG_DYNAMIC | UF_FLAG_URGENT,                       // UNIT_FIELD_STATE_WORLD_EFFECT_ID+2
    UF_FLAG_DYNAMIC | UF_FLAG_URGENT,                       // UNIT_FIELD_STATE_WORLD_EFFECT_ID+3
    UF_FLAG_PUBLIC,                                         // UNIT_FIELD_SCALE_DURATION
    UF_FLAG_PUBLIC,                                         // UNIT_FIELD_LOOKS_LIKE_MOUNT_ID
    UF_FLAG_PUBLIC,                                         // UNIT_FIELD_LOOKS_LIKE_CREATURE_ID
    UF_FLAG_PUBLIC,                                         // UNIT_FIELD_LOOK_AT_CONTROLLER_ID
    UF_FLAG_PUBLIC,                                         // UNIT_FIELD_GUILD_GUID
    UF_FLAG_PUBLIC,                                         // UNIT_FIELD_GUILD_GUID+1
    UF_FLAG_PUBLIC,                                         // UNIT_FIELD_GUILD_GUID+2
    UF_FLAG_PUBLIC,                                         // UNIT_FIELD_GUILD_GUID+3
    UF_FLAG_PUBLIC,                                         // PLAYER_DUEL_ARBITER
    UF_FLAG_PUBLIC,                                         // PLAYER_DUEL_ARBITER+1
    UF_FLAG_PUBLIC,                                         // PLAYER_DUEL_ARBITER+2
    UF_FLAG_PUBLIC,                                         // PLAYER_DUEL_ARBITER+3
    UF_FLAG_PUBLIC,                                         // PLAYER_WOW_ACCOUNT
    UF_FLAG_PUBLIC,                                         // PLAYER_WOW_ACCOUNT+1
    UF_FLAG_PUBLIC,                                         // PLAYER_WOW_ACCOUNT+2
    UF_FLAG_PUBLIC,                                         // PLAYER_WOW_ACCOUNT+3
    UF_FLAG_PUBLIC,                                         // PLAYER_LOOT_TARGET_GUID
    UF_FLAG_PUBLIC,                                         // PLAYER_LOOT_TARGET_GUID+1
    UF_FLAG_PUBLIC,                                         // PLAYER_LOOT_TARGET_GUID+2
    UF_FLAG_PUBLIC,                                         // PLAYER_LOOT_TARGET_GUID+3
    UF_FLAG_PUBLIC,                                         // PLAYER_FLAGS
    UF_FLAG_PUBLIC,                                         // PLAYER_FLAGS_EX
    UF_FLAG_PUBLIC,                                         // PLAYER_GUILDRANK
    UF_FLAG_PUBLIC,                                         // PLAYER_GUILDDELETE_DATE
    UF_FLAG_PUBLIC,                                         // PLAYER_GUILDLEVEL
    UF_FLAG_PUBLIC,                                         // PLAYER_BYTES
    UF_FLAG_PUBLIC,                                         // PLAYER_BYTES_2
    UF_FLAG_PUBLIC,                                         // PLAYER_DUEL_TEAM
    UF_FLAG_PUBLIC,                                         // PLAYER_GUILD_TIMESTAMP
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+1
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+2
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+3
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+4
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+5
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+6
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+7
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+8
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+9
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+10
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+11
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+12
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+13
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+14
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+15
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+16
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+17
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+18
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+19
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+20
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+21
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+22
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+23
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+24
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+25
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+26
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+27
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+28
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+29
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+30
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+31
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+32
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+33
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+34
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+35
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+36
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+37
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+38
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+39
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+40
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+41
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+42
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+43
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+44
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+45
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+46
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+47
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+48
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+49
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+50
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+51
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+52
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+53
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+54
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+55
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+56
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+57
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+58
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+59
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+60
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+61
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+62
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+63
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+64
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+65
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+66
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+67
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+68
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+69
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+70
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+71
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+72
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+73
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+74
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+75
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+76
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+77
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+78
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+79
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+80
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+81
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+82
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+83
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+84
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+85
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+86
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+87
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+88
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+89
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+90
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+91
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+92
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+93
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+94
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+95
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+96
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+97
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+98
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+99
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+100
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+101
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+102
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+103
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+104
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+105
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+106
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+107
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+108
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+109
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+110
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+111
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+112
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+113
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+114
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+115
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+116
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+117
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+118
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+119
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+120
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+121
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+122
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+123
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+124
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+125
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+126
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+127
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+128
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+129
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+130
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+131
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+132
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+133
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+134
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+135
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+136
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+137
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+138
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+139
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+140
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+141
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+142
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+143
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+144
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+145
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+146
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+147
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+148
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+149
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+150
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+151
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+152
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+153
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+154
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+155
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+156
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+157
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+158
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+159
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+160
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+161
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+162
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+163
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+164
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+165
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+166
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+167
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+168
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+169
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+170
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+171
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+172
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+173
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+174
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+175
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+176
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+177
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+178
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+179
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+180
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+181
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+182
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+183
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+184
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+185
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+186
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+187
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+188
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+189
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+190
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+191
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+192
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+193
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+194
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+195
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+196
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+197
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+198
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+199
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+200
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+201
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+202
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+203
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+204
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+205
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+206
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+207
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+208
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+209
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+210
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+211
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+212
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+213
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+214
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+215
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+216
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+217
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+218
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+219
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+220
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+221
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+222
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+223
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+224
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+225
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+226
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+227
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+228
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+229
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+230
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+231
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+232
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+233
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+234
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+235
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+236
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+237
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+238
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+239
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+240
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+241
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+242
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+243
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+244
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+245
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+246
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+247
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+248
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+249
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+250
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+251
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+252
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+253
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+254
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+255
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+256
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+257
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+258
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+259
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+260
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+261
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+262
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+263
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+264
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+265
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+266
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+267
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+268
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+269
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+270
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+271
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+272
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+273
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+274
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+275
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+276
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+277
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+278
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+279
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+280
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+281
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+282
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+283
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+284
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+285
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+286
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+287
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+288
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+289
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+290
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+291
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+292
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+293
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+294
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+295
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+296
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+297
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+298
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+299
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+300
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+301
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+302
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+303
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+304
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+305
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+306
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+307
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+308
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+309
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+310
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+311
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+312
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+313
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+314
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+315
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+316
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+317
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+318
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+319
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+320
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+321
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+322
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+323
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+324
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+325
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+326
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+327
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+328
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+329
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+330
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+331
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+332
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+333
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+334
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+335
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+336
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+337
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+338
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+339
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+340
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+341
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+342
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+343
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+344
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+345
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+346
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+347
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+348
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+349
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+350
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+351
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+352
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+353
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+354
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+355
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+356
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+357
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+358
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+359
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+360
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+361
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+362
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+363
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+364
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+365
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+366
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+367
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+368
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+369
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+370
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+371
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+372
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+373
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+374
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+375
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+376
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+377
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+378
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+379
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+380
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+381
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+382
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+383
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+384
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+385
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+386
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+387
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+388
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+389
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+390
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+391
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+392
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+393
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+394
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+395
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+396
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+397
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+398
    UF_FLAG_GROUP_ONLY,                                     // PLAYER_QUEST_LOG+399
    UF_FLAG_PUBLIC,                                         // PLAYER_VISIBLE_ITEM
    UF_FLAG_PUBLIC,                                         // PLAYER_VISIBLE_ITEM+1
    UF_FLAG_PUBLIC,                                         // PLAYER_VISIBLE_ITEM+2
    UF_FLAG_PUBLIC,                                         // PLAYER_VISIBLE_ITEM+3
    UF_FLAG_PUBLIC,                                         // PLAYER_VISIBLE_ITEM+4
    UF_FLAG_PUBLIC,                                         // PLAYER_VISIBLE_ITEM+5
    UF_FLAG_PUBLIC,                                         // PLAYER_VISIBLE_ITEM+6
    UF_FLAG_PUBLIC,                                         // PLAYER_VISIBLE_ITEM+7
    UF_FLAG_PUBLIC,                                         // PLAYER_VISIBLE_ITEM+8
    UF_FLAG_PUBLIC,                                         // PLAYER_VISIBLE_ITEM+9
    UF_FLAG_PUBLIC,                                         // PLAYER_VISIBLE_ITEM+10
    UF_FLAG_PUBLIC,                                         // PLAYER_VISIBLE_ITEM+11
    UF_FLAG_PUBLIC,                                         // PLAYER_VISIBLE_ITEM+12
    UF_FLAG_PUBLIC,                                         // PLAYER_VISIBLE_ITEM+13
    UF_FLAG_PUBLIC,                                         // PLAYER_VISIBLE_ITEM+14
    UF_FLAG_PUBLIC,                                         // PLAYER_VISIBLE_ITEM+15
    UF_FLAG_PUBLIC,                                         // PLAYER_VISIBLE_ITEM+16
    UF_FLAG_PUBLIC,                                         // PLAYER_VISIBLE_ITEM+17
    UF_FLAG_PUBLIC,                                         // PLAYER_VISIBLE_ITEM+18
    UF_FLAG_PUBLIC,                                         // PLAYER_VISIBLE_ITEM+19
    UF_FLAG_PUBLIC,                                         // PLAYER_VISIBLE_ITEM+20
    UF_FLAG_PUBLIC,                                         // PLAYER_VISIBLE_ITEM+21
    UF_FLAG_PUBLIC,                                         // PLAYER_VISIBLE_ITEM+22
    UF_FLAG_PUBLIC,                                         // PLAYER_VISIBLE_ITEM+23
    UF_FLAG_PUBLIC,                                         // PLAYER_VISIBLE_ITEM+24
    UF_FLAG_PUBLIC,                                         // PLAYER_VISIBLE_ITEM+25
    UF_FLAG_PUBLIC,                                         // PLAYER_VISIBLE_ITEM+26
    UF_FLAG_PUBLIC,                                         // PLAYER_VISIBLE_ITEM+27
    UF_FLAG_PUBLIC,                                         // PLAYER_VISIBLE_ITEM+28
    UF_FLAG_PUBLIC,                                         // PLAYER_VISIBLE_ITEM+29
    UF_FLAG_PUBLIC,                                         // PLAYER_VISIBLE_ITEM+30
    UF_FLAG_PUBLIC,                                         // PLAYER_VISIBLE_ITEM+31
    UF_FLAG_PUBLIC,                                         // PLAYER_VISIBLE_ITEM+32
    UF_FLAG_PUBLIC,                                         // PLAYER_VISIBLE_ITEM+33
    UF_FLAG_PUBLIC,                                         // PLAYER_VISIBLE_ITEM+34
    UF_FLAG_PUBLIC,                                         // PLAYER_VISIBLE_ITEM+35
    UF_FLAG_PUBLIC,                                         // PLAYER_VISIBLE_ITEM+36
    UF_FLAG_PUBLIC,                                         // PLAYER_VISIBLE_ITEM+37
    UF_FLAG_PUBLIC,                                         // PLAYER_CHOSEN_TITLE
    UF_FLAG_PUBLIC,                                         // PLAYER_FAKE_INEBRIATION
    UF_FLAG_PUBLIC,                                         // PLAYER_FIELD_VIRTUAL_PLAYER_REALM
    UF_FLAG_PUBLIC,                                         // PLAYER_FIELD_CURRENT_SPEC_ID
    UF_FLAG_PUBLIC,                                         // PLAYER_FIELD_TAXI_MOUNT_ANIM_KIT_ID
    UF_FLAG_PUBLIC,                                         // PLAYER_FIELD_AVG_ITEM_LEVEL
    UF_FLAG_PUBLIC,                                         // PLAYER_FIELD_AVG_ITEM_LEVEL+1
    UF_FLAG_PUBLIC,                                         // PLAYER_FIELD_AVG_ITEM_LEVEL+2
    UF_FLAG_PUBLIC,                                         // PLAYER_FIELD_AVG_ITEM_LEVEL+3
    UF_FLAG_PUBLIC,                                         // PLAYER_FIELD_AVG_ITEM_LEVEL+4
    UF_FLAG_PUBLIC,                                         // PLAYER_FIELD_AVG_ITEM_LEVEL+5
    UF_FLAG_PUBLIC,                                         // PLAYER_FIELD_CURRENT_BATTLE_PET_BREED_QUALITY
    UF_FLAG_PUBLIC,                                         // PLAYER_FIELD_HONOR_LEVEL
    UF_FLAG_PUBLIC,                                         // PLAYER_FIELD_CUSTOMIZATION_CHOICES
    UF_FLAG_PUBLIC,                                         // PLAYER_FIELD_CUSTOMIZATION_CHOICES+1
    UF_FLAG_PUBLIC,                                         // PLAYER_FIELD_CUSTOMIZATION_CHOICES+2
    UF_FLAG_PUBLIC,                                         // PLAYER_FIELD_CUSTOMIZATION_CHOICES+3
    UF_FLAG_PUBLIC,                                         // PLAYER_FIELD_CUSTOMIZATION_CHOICES+4
    UF_FLAG_PUBLIC,                                         // PLAYER_FIELD_CUSTOMIZATION_CHOICES+5
    UF_FLAG_PUBLIC,                                         // PLAYER_FIELD_CUSTOMIZATION_CHOICES+6
    UF_FLAG_PUBLIC,                                         // PLAYER_FIELD_CUSTOMIZATION_CHOICES+7
    UF_FLAG_PUBLIC,                                         // PLAYER_FIELD_CUSTOMIZATION_CHOICES+8
    UF_FLAG_PUBLIC,                                         // PLAYER_FIELD_CUSTOMIZATION_CHOICES+9
    UF_FLAG_PUBLIC,                                         // PLAYER_FIELD_CUSTOMIZATION_CHOICES+10
    UF_FLAG_PUBLIC,                                         // PLAYER_FIELD_CUSTOMIZATION_CHOICES+11
    UF_FLAG_PUBLIC,                                         // PLAYER_FIELD_CUSTOMIZATION_CHOICES+12
    UF_FLAG_PUBLIC,                                         // PLAYER_FIELD_CUSTOMIZATION_CHOICES+13
    UF_FLAG_PUBLIC,                                         // PLAYER_FIELD_CUSTOMIZATION_CHOICES+14
    UF_FLAG_PUBLIC,                                         // PLAYER_FIELD_CUSTOMIZATION_CHOICES+15
    UF_FLAG_PUBLIC,                                         // PLAYER_FIELD_CUSTOMIZATION_CHOICES+16
    UF_FLAG_PUBLIC,                                         // PLAYER_FIELD_CUSTOMIZATION_CHOICES+17
    UF_FLAG_PUBLIC,                                         // PLAYER_FIELD_CUSTOMIZATION_CHOICES+18
    UF_FLAG_PUBLIC,                                         // PLAYER_FIELD_CUSTOMIZATION_CHOICES+19
    UF_FLAG_PUBLIC,                                         // PLAYER_FIELD_CUSTOMIZATION_CHOICES+20
    UF_FLAG_PUBLIC,                                         // PLAYER_FIELD_CUSTOMIZATION_CHOICES+21
    UF_FLAG_PUBLIC,                                         // PLAYER_FIELD_CUSTOMIZATION_CHOICES+22
    UF_FLAG_PUBLIC,                                         // PLAYER_FIELD_CUSTOMIZATION_CHOICES+23
    UF_FLAG_PUBLIC,                                         // PLAYER_FIELD_CUSTOMIZATION_CHOICES+24
    UF_FLAG_PUBLIC,                                         // PLAYER_FIELD_CUSTOMIZATION_CHOICES+25
    UF_FLAG_PUBLIC,                                         // PLAYER_FIELD_CUSTOMIZATION_CHOICES+26
    UF_FLAG_PUBLIC,                                         // PLAYER_FIELD_CUSTOMIZATION_CHOICES+27
    UF_FLAG_PUBLIC,                                         // PLAYER_FIELD_CUSTOMIZATION_CHOICES+28
    UF_FLAG_PUBLIC,                                         // PLAYER_FIELD_CUSTOMIZATION_CHOICES+29
    UF_FLAG_PUBLIC,                                         // PLAYER_FIELD_CUSTOMIZATION_CHOICES+30
    UF_FLAG_PUBLIC,                                         // PLAYER_FIELD_CUSTOMIZATION_CHOICES+31
    UF_FLAG_PUBLIC,                                         // PLAYER_FIELD_CUSTOMIZATION_CHOICES+32
    UF_FLAG_PUBLIC,                                         // PLAYER_FIELD_CUSTOMIZATION_CHOICES+33
    UF_FLAG_PUBLIC,                                         // PLAYER_FIELD_CUSTOMIZATION_CHOICES+34
    UF_FLAG_PUBLIC,                                         // PLAYER_FIELD_CUSTOMIZATION_CHOICES+35
    UF_FLAG_PUBLIC,                                         // PLAYER_FIELD_CUSTOMIZATION_CHOICES+36
    UF_FLAG_PUBLIC,                                         // PLAYER_FIELD_CUSTOMIZATION_CHOICES+37
    UF_FLAG_PUBLIC,                                         // PLAYER_FIELD_CUSTOMIZATION_CHOICES+38
    UF_FLAG_PUBLIC,                                         // PLAYER_FIELD_CUSTOMIZATION_CHOICES+39
    UF_FLAG_PUBLIC,                                         // PLAYER_FIELD_CUSTOMIZATION_CHOICES+40
    UF_FLAG_PUBLIC,                                         // PLAYER_FIELD_CUSTOMIZATION_CHOICES+41
    UF_FLAG_PUBLIC,                                         // PLAYER_FIELD_CUSTOMIZATION_CHOICES+42
    UF_FLAG_PUBLIC,                                         // PLAYER_FIELD_CUSTOMIZATION_CHOICES+43
    UF_FLAG_PUBLIC,                                         // PLAYER_FIELD_CUSTOMIZATION_CHOICES+44
    UF_FLAG_PUBLIC,                                         // PLAYER_FIELD_CUSTOMIZATION_CHOICES+45
    UF_FLAG_PUBLIC,                                         // PLAYER_FIELD_CUSTOMIZATION_CHOICES+46
    UF_FLAG_PUBLIC,                                         // PLAYER_FIELD_CUSTOMIZATION_CHOICES+47
    UF_FLAG_PUBLIC,                                         // PLAYER_FIELD_CUSTOMIZATION_CHOICES+48
    UF_FLAG_PUBLIC,                                         // PLAYER_FIELD_CUSTOMIZATION_CHOICES+49
    UF_FLAG_PUBLIC,                                         // PLAYER_FIELD_CUSTOMIZATION_CHOICES+50
    UF_FLAG_PUBLIC,                                         // PLAYER_FIELD_CUSTOMIZATION_CHOICES+51
    UF_FLAG_PUBLIC,                                         // PLAYER_FIELD_CUSTOMIZATION_CHOICES+52
    UF_FLAG_PUBLIC,                                         // PLAYER_FIELD_CUSTOMIZATION_CHOICES+53
    UF_FLAG_PUBLIC,                                         // PLAYER_FIELD_CUSTOMIZATION_CHOICES+54
    UF_FLAG_PUBLIC,                                         // PLAYER_FIELD_CUSTOMIZATION_CHOICES+55
    UF_FLAG_PUBLIC,                                         // PLAYER_FIELD_CUSTOMIZATION_CHOICES+56
    UF_FLAG_PUBLIC,                                         // PLAYER_FIELD_CUSTOMIZATION_CHOICES+57
    UF_FLAG_PUBLIC,                                         // PLAYER_FIELD_CUSTOMIZATION_CHOICES+58
    UF_FLAG_PUBLIC,                                         // PLAYER_FIELD_CUSTOMIZATION_CHOICES+59
    UF_FLAG_PUBLIC,                                         // PLAYER_FIELD_CUSTOMIZATION_CHOICES+60
    UF_FLAG_PUBLIC,                                         // PLAYER_FIELD_CUSTOMIZATION_CHOICES+61
    UF_FLAG_PUBLIC,                                         // PLAYER_FIELD_CUSTOMIZATION_CHOICES+62
    UF_FLAG_PUBLIC,                                         // PLAYER_FIELD_CUSTOMIZATION_CHOICES+63
    UF_FLAG_PUBLIC,                                         // PLAYER_FIELD_CUSTOMIZATION_CHOICES+64
    UF_FLAG_PUBLIC,                                         // PLAYER_FIELD_CUSTOMIZATION_CHOICES+65
    UF_FLAG_PUBLIC,                                         // PLAYER_FIELD_CUSTOMIZATION_CHOICES+66
    UF_FLAG_PUBLIC,                                         // PLAYER_FIELD_CUSTOMIZATION_CHOICES+67
    UF_FLAG_PUBLIC,                                         // PLAYER_FIELD_CUSTOMIZATION_CHOICES+68
    UF_FLAG_PUBLIC,                                         // PLAYER_FIELD_CUSTOMIZATION_CHOICES+69
    UF_FLAG_PUBLIC,                                         // PLAYER_FIELD_CUSTOMIZATION_CHOICES+70
    UF_FLAG_PUBLIC,                                         // PLAYER_FIELD_CUSTOMIZATION_CHOICES+71
};

uint32 UnitDynamicUpdateFieldFlags[PLAYER_DYNAMIC_END] = 
{
    UF_FLAG_PUBLIC | UF_FLAG_URGENT,                        // UNIT_DYNAMIC_FIELD_PASSIVE_SPELLS
    UF_FLAG_PUBLIC | UF_FLAG_URGENT,                        // UNIT_DYNAMIC_FIELD_WORLD_EFFECTS
    UF_FLAG_PUBLIC | UF_FLAG_URGENT,                        // UNIT_DYNAMIC_FIELD_CHANNEL_OBJECTS
    UF_FLAG_PUBLIC,                                         // PLAYER_DYNAMIC_FIELD_ARENA_COOLDOWNS
};

uint32 GameObjectUpdateFieldFlags[GAMEOBJECT_END] = 
{
    UF_FLAG_PUBLIC,                                         // OBJECT_FIELD_GUID
    UF_FLAG_PUBLIC,                                         // OBJECT_FIELD_GUID+1
    UF_FLAG_PUBLIC,                                         // OBJECT_FIELD_GUID+2
    UF_FLAG_PUBLIC,                                         // OBJECT_FIELD_GUID+3
    UF_FLAG_DYNAMIC,                                        // OBJECT_FIELD_ENTRY
    UF_FLAG_DYNAMIC | UF_FLAG_URGENT,                       // OBJECT_DYNAMIC_FLAGS
    UF_FLAG_PUBLIC,                                         // OBJECT_FIELD_SCALE_X
    UF_FLAG_PUBLIC,                                         // GAMEOBJECT_FIELD_CREATED_BY
    UF_FLAG_PUBLIC,                                         // GAMEOBJECT_FIELD_CREATED_BY+1
    UF_FLAG_PUBLIC,                                         // GAMEOBJECT_FIELD_CREATED_BY+2
    UF_FLAG_PUBLIC,                                         // GAMEOBJECT_FIELD_CREATED_BY+3
    UF_FLAG_PUBLIC,                                         // GAMEOBJECT_FIELD_GUILD_GUID
    UF_FLAG_PUBLIC,                                         // GAMEOBJECT_FIELD_GUILD_GUID+1
    UF_FLAG_PUBLIC,                                         // GAMEOBJECT_FIELD_GUILD_GUID+2
    UF_FLAG_PUBLIC,                                         // GAMEOBJECT_FIELD_GUILD_GUID+3
    UF_FLAG_DYNAMIC | UF_FLAG_URGENT,                       // GAMEOBJECT_DISPLAYID
    UF_FLAG_PUBLIC | UF_FLAG_URGENT,                        // GAMEOBJECT_FLAGS
    UF_FLAG_PUBLIC,                                         // GAMEOBJECT_PARENTROTATION
    UF_FLAG_PUBLIC,                                         // GAMEOBJECT_PARENTROTATION+1
    UF_FLAG_PUBLIC,                                         // GAMEOBJECT_PARENTROTATION+2
    UF_FLAG_PUBLIC,                                         // GAMEOBJECT_PARENTROTATION+3
    UF_FLAG_PUBLIC,                                         // GAMEOBJECT_FACTION
    UF_FLAG_PUBLIC,                                         // GAMEOBJECT_LEVEL
    UF_FLAG_PUBLIC | UF_FLAG_URGENT,                        // GAMEOBJECT_BYTES_1
    UF_FLAG_PUBLIC | UF_FLAG_DYNAMIC | UF_FLAG_URGENT,      // GAMEOBJECT_SPELL_VISUAL_ID
    UF_FLAG_DYNAMIC | UF_FLAG_URGENT,                       // GAMEOBJECT_STATE_SPELL_VISUAL_ID
    UF_FLAG_DYNAMIC | UF_FLAG_URGENT,                       // GAMEOBJECT_STATE_ANIM_ID
    UF_FLAG_DYNAMIC | UF_FLAG_URGENT,                       // GAMEOBJECT_STATE_ANIM_KIT_ID
    UF_FLAG_DYNAMIC | UF_FLAG_URGENT,                       // GAMEOBJECT_STATE_WORLD_EFFECT_ID
    UF_FLAG_DYNAMIC | UF_FLAG_URGENT,                       // GAMEOBJECT_STATE_WORLD_EFFECT_ID+1
    UF_FLAG_DYNAMIC | UF_FLAG_URGENT,                       // GAMEOBJECT_STATE_WORLD_EFFECT_ID+2
    UF_FLAG_DYNAMIC | UF_FLAG_URGENT,                       // GAMEOBJECT_STATE_WORLD_EFFECT_ID+3
    UF_FLAG_PUBLIC | UF_FLAG_URGENT,                        // GAMEOBJECT_FIELD_CUSTOM_PARAM
};

uint32 GameObjectDynamicUpdateFieldFlags[GAMEOBJECT_DYNAMIC_END] = 
{
    UF_FLAG_PUBLIC,                                         // GAMEOBJECT_DYNAMIC_ENABLE_DOODAD_SETS
};

uint32 DynamicObjectUpdateFieldFlags[DYNAMICOBJECT_END] = 
{
    UF_FLAG_PUBLIC,                                         // OBJECT_FIELD_GUID
    UF_FLAG_PUBLIC,                                         // OBJECT_FIELD_GUID+1
    UF_FLAG_PUBLIC,                                         // OBJECT_FIELD_GUID+2
    UF_FLAG_PUBLIC,                                         // OBJECT_FIELD_GUID+3
    UF_FLAG_DYNAMIC,                                        // OBJECT_FIELD_ENTRY
    UF_FLAG_DYNAMIC | UF_FLAG_URGENT,                       // OBJECT_DYNAMIC_FLAGS
    UF_FLAG_PUBLIC,                                         // OBJECT_FIELD_SCALE_X
    UF_FLAG_PUBLIC,                                         // DYNAMICOBJECT_CASTER
    UF_FLAG_PUBLIC,                                         // DYNAMICOBJECT_CASTER+1
    UF_FLAG_PUBLIC,                                         // DYNAMICOBJECT_CASTER+2
    UF_FLAG_PUBLIC,                                         // DYNAMICOBJECT_CASTER+3
    UF_FLAG_PUBLIC,                                         // DYNAMICOBJECT_TYPE
    UF_FLAG_PUBLIC,                                         // DYNAMICOBJECT_SPELL_X_SPELL_VISUAL_ID
    UF_FLAG_PUBLIC,                                         // DYNAMICOBJECT_SPELLID
    UF_FLAG_PUBLIC,                                         // DYNAMICOBJECT_RADIUS
    UF_FLAG_PUBLIC,                                         // DYNAMICOBJECT_CASTTIME
};

uint32 CorpseUpdateFieldFlags[CORPSE_END] = 
{
    UF_FLAG_PUBLIC,                                         // OBJECT_FIELD_GUID
    UF_FLAG_PUBLIC,                                         // OBJECT_FIELD_GUID+1
    UF_FLAG_PUBLIC,                                         // OBJECT_FIELD_GUID+2
    UF_FLAG_PUBLIC,                                         // OBJECT_FIELD_GUID+3
    UF_FLAG_DYNAMIC,                                        // OBJECT_FIELD_ENTRY
    UF_FLAG_DYNAMIC | UF_FLAG_URGENT,                       // OBJECT_DYNAMIC_FLAGS
    UF_FLAG_PUBLIC,                                         // OBJECT_FIELD_SCALE_X
    UF_FLAG_PUBLIC,                                         // CORPSE_FIELD_OWNER
    UF_FLAG_PUBLIC,                                         // CORPSE_FIELD_OWNER+1
    UF_FLAG_PUBLIC,                                         // CORPSE_FIELD_OWNER+2
    UF_FLAG_PUBLIC,                                         // CORPSE_FIELD_OWNER+3
    UF_FLAG_PUBLIC,                                         // CORPSE_FIELD_PARTY_GUID
    UF_FLAG_PUBLIC,                                         // CORPSE_FIELD_PARTY_GUID+1
    UF_FLAG_PUBLIC,                                         // CORPSE_FIELD_PARTY_GUID+2
    UF_FLAG_PUBLIC,                                         // CORPSE_FIELD_PARTY_GUID+3
    UF_FLAG_PUBLIC,                                         // CORPSE_FIELD_GUILD_GUID
    UF_FLAG_PUBLIC,                                         // CORPSE_FIELD_GUILD_GUID+1
    UF_FLAG_PUBLIC,                                         // CORPSE_FIELD_GUILD_GUID+2
    UF_FLAG_PUBLIC,                                         // CORPSE_FIELD_GUILD_GUID+3
    UF_FLAG_PUBLIC,                                         // CORPSE_FIELD_DISPLAY_ID
    UF_FLAG_PUBLIC,                                         // CORPSE_FIELD_ITEMS
    UF_FLAG_PUBLIC,                                         // CORPSE_FIELD_ITEMS+1
    UF_FLAG_PUBLIC,                                         // CORPSE_FIELD_ITEMS+2
    UF_FLAG_PUBLIC,                                         // CORPSE_FIELD_ITEMS+3
    UF_FLAG_PUBLIC,                                         // CORPSE_FIELD_ITEMS+4
    UF_FLAG_PUBLIC,                                         // CORPSE_FIELD_ITEMS+5
    UF_FLAG_PUBLIC,                                         // CORPSE_FIELD_ITEMS+6
    UF_FLAG_PUBLIC,                                         // CORPSE_FIELD_ITEMS+7
    UF_FLAG_PUBLIC,                                         // CORPSE_FIELD_ITEMS+8
    UF_FLAG_PUBLIC,                                         // CORPSE_FIELD_ITEMS+9
    UF_FLAG_PUBLIC,                                         // CORPSE_FIELD_ITEMS+10
    UF_FLAG_PUBLIC,                                         // CORPSE_FIELD_ITEMS+11
    UF_FLAG_PUBLIC,                                         // CORPSE_FIELD_ITEMS+12
    UF_FLAG_PUBLIC,                                         // CORPSE_FIELD_ITEMS+13
    UF_FLAG_PUBLIC,                                         // CORPSE_FIELD_ITEMS+14
    UF_FLAG_PUBLIC,                                         // CORPSE_FIELD_ITEMS+15
    UF_FLAG_PUBLIC,                                         // CORPSE_FIELD_ITEMS+16
    UF_FLAG_PUBLIC,                                         // CORPSE_FIELD_ITEMS+17
    UF_FLAG_PUBLIC,                                         // CORPSE_FIELD_ITEMS+18
    UF_FLAG_PUBLIC,                                         // CORPSE_FIELD_BYTES_1
    UF_FLAG_PUBLIC,                                         // CORPSE_FIELD_FLAGS
    UF_FLAG_DYNAMIC,                                        // CORPSE_FIELD_DYNAMIC_FLAGS
    UF_FLAG_PUBLIC,                                         // CORPSE_FIELD_FACTION_TEMPLATE
    UF_FLAG_PUBLIC,                                         // CORPSE_FIELD_CUSTOMIZATION_CHOICES
    UF_FLAG_PUBLIC,                                         // CORPSE_FIELD_CUSTOMIZATION_CHOICES+1
    UF_FLAG_PUBLIC,                                         // CORPSE_FIELD_CUSTOMIZATION_CHOICES+2
    UF_FLAG_PUBLIC,                                         // CORPSE_FIELD_CUSTOMIZATION_CHOICES+3
    UF_FLAG_PUBLIC,                                         // CORPSE_FIELD_CUSTOMIZATION_CHOICES+4
    UF_FLAG_PUBLIC,                                         // CORPSE_FIELD_CUSTOMIZATION_CHOICES+5
    UF_FLAG_PUBLIC,                                         // CORPSE_FIELD_CUSTOMIZATION_CHOICES+6
    UF_FLAG_PUBLIC,                                         // CORPSE_FIELD_CUSTOMIZATION_CHOICES+7
    UF_FLAG_PUBLIC,                                         // CORPSE_FIELD_CUSTOMIZATION_CHOICES+8
    UF_FLAG_PUBLIC,                                         // CORPSE_FIELD_CUSTOMIZATION_CHOICES+9
    UF_FLAG_PUBLIC,                                         // CORPSE_FIELD_CUSTOMIZATION_CHOICES+10
    UF_FLAG_PUBLIC,                                         // CORPSE_FIELD_CUSTOMIZATION_CHOICES+11
    UF_FLAG_PUBLIC,                                         // CORPSE_FIELD_CUSTOMIZATION_CHOICES+12
    UF_FLAG_PUBLIC,                                         // CORPSE_FIELD_CUSTOMIZATION_CHOICES+13
    UF_FLAG_PUBLIC,                                         // CORPSE_FIELD_CUSTOMIZATION_CHOICES+14
    UF_FLAG_PUBLIC,                                         // CORPSE_FIELD_CUSTOMIZATION_CHOICES+15
    UF_FLAG_PUBLIC,                                         // CORPSE_FIELD_CUSTOMIZATION_CHOICES+16
    UF_FLAG_PUBLIC,                                         // CORPSE_FIELD_CUSTOMIZATION_CHOICES+17
    UF_FLAG_PUBLIC,                                         // CORPSE_FIELD_CUSTOMIZATION_CHOICES+18
    UF_FLAG_PUBLIC,                                         // CORPSE_FIELD_CUSTOMIZATION_CHOICES+19
    UF_FLAG_PUBLIC,                                         // CORPSE_FIELD_CUSTOMIZATION_CHOICES+20
    UF_FLAG_PUBLIC,                                         // CORPSE_FIELD_CUSTOMIZATION_CHOICES+21
    UF_FLAG_PUBLIC,                                         // CORPSE_FIELD_CUSTOMIZATION_CHOICES+22
    UF_FLAG_PUBLIC,                                         // CORPSE_FIELD_CUSTOMIZATION_CHOICES+23
    UF_FLAG_PUBLIC,                                         // CORPSE_FIELD_CUSTOMIZATION_CHOICES+24
    UF_FLAG_PUBLIC,                                         // CORPSE_FIELD_CUSTOMIZATION_CHOICES+25
    UF_FLAG_PUBLIC,                                         // CORPSE_FIELD_CUSTOMIZATION_CHOICES+26
    UF_FLAG_PUBLIC,                                         // CORPSE_FIELD_CUSTOMIZATION_CHOICES+27
    UF_FLAG_PUBLIC,                                         // CORPSE_FIELD_CUSTOMIZATION_CHOICES+28
    UF_FLAG_PUBLIC,                                         // CORPSE_FIELD_CUSTOMIZATION_CHOICES+29
    UF_FLAG_PUBLIC,                                         // CORPSE_FIELD_CUSTOMIZATION_CHOICES+30
    UF_FLAG_PUBLIC,                                         // CORPSE_FIELD_CUSTOMIZATION_CHOICES+31
    UF_FLAG_PUBLIC,                                         // CORPSE_FIELD_CUSTOMIZATION_CHOICES+32
    UF_FLAG_PUBLIC,                                         // CORPSE_FIELD_CUSTOMIZATION_CHOICES+33
    UF_FLAG_PUBLIC,                                         // CORPSE_FIELD_CUSTOMIZATION_CHOICES+34
    UF_FLAG_PUBLIC,                                         // CORPSE_FIELD_CUSTOMIZATION_CHOICES+35
    UF_FLAG_PUBLIC,                                         // CORPSE_FIELD_CUSTOMIZATION_CHOICES+36
    UF_FLAG_PUBLIC,                                         // CORPSE_FIELD_CUSTOMIZATION_CHOICES+37
    UF_FLAG_PUBLIC,                                         // CORPSE_FIELD_CUSTOMIZATION_CHOICES+38
    UF_FLAG_PUBLIC,                                         // CORPSE_FIELD_CUSTOMIZATION_CHOICES+39
    UF_FLAG_PUBLIC,                                         // CORPSE_FIELD_CUSTOMIZATION_CHOICES+40
    UF_FLAG_PUBLIC,                                         // CORPSE_FIELD_CUSTOMIZATION_CHOICES+41
    UF_FLAG_PUBLIC,                                         // CORPSE_FIELD_CUSTOMIZATION_CHOICES+42
    UF_FLAG_PUBLIC,                                         // CORPSE_FIELD_CUSTOMIZATION_CHOICES+43
    UF_FLAG_PUBLIC,                                         // CORPSE_FIELD_CUSTOMIZATION_CHOICES+44
    UF_FLAG_PUBLIC,                                         // CORPSE_FIELD_CUSTOMIZATION_CHOICES+45
    UF_FLAG_PUBLIC,                                         // CORPSE_FIELD_CUSTOMIZATION_CHOICES+46
    UF_FLAG_PUBLIC,                                         // CORPSE_FIELD_CUSTOMIZATION_CHOICES+47
    UF_FLAG_PUBLIC,                                         // CORPSE_FIELD_CUSTOMIZATION_CHOICES+48
    UF_FLAG_PUBLIC,                                         // CORPSE_FIELD_CUSTOMIZATION_CHOICES+49
    UF_FLAG_PUBLIC,                                         // CORPSE_FIELD_CUSTOMIZATION_CHOICES+50
    UF_FLAG_PUBLIC,                                         // CORPSE_FIELD_CUSTOMIZATION_CHOICES+51
    UF_FLAG_PUBLIC,                                         // CORPSE_FIELD_CUSTOMIZATION_CHOICES+52
    UF_FLAG_PUBLIC,                                         // CORPSE_FIELD_CUSTOMIZATION_CHOICES+53
    UF_FLAG_PUBLIC,                                         // CORPSE_FIELD_CUSTOMIZATION_CHOICES+54
    UF_FLAG_PUBLIC,                                         // CORPSE_FIELD_CUSTOMIZATION_CHOICES+55
    UF_FLAG_PUBLIC,                                         // CORPSE_FIELD_CUSTOMIZATION_CHOICES+56
    UF_FLAG_PUBLIC,                                         // CORPSE_FIELD_CUSTOMIZATION_CHOICES+57
    UF_FLAG_PUBLIC,                                         // CORPSE_FIELD_CUSTOMIZATION_CHOICES+58
    UF_FLAG_PUBLIC,                                         // CORPSE_FIELD_CUSTOMIZATION_CHOICES+59
    UF_FLAG_PUBLIC,                                         // CORPSE_FIELD_CUSTOMIZATION_CHOICES+60
    UF_FLAG_PUBLIC,                                         // CORPSE_FIELD_CUSTOMIZATION_CHOICES+61
    UF_FLAG_PUBLIC,                                         // CORPSE_FIELD_CUSTOMIZATION_CHOICES+62
    UF_FLAG_PUBLIC,                                         // CORPSE_FIELD_CUSTOMIZATION_CHOICES+63
    UF_FLAG_PUBLIC,                                         // CORPSE_FIELD_CUSTOMIZATION_CHOICES+64
    UF_FLAG_PUBLIC,                                         // CORPSE_FIELD_CUSTOMIZATION_CHOICES+65
    UF_FLAG_PUBLIC,                                         // CORPSE_FIELD_CUSTOMIZATION_CHOICES+66
    UF_FLAG_PUBLIC,                                         // CORPSE_FIELD_CUSTOMIZATION_CHOICES+67
    UF_FLAG_PUBLIC,                                         // CORPSE_FIELD_CUSTOMIZATION_CHOICES+68
    UF_FLAG_PUBLIC,                                         // CORPSE_FIELD_CUSTOMIZATION_CHOICES+69
    UF_FLAG_PUBLIC,                                         // CORPSE_FIELD_CUSTOMIZATION_CHOICES+70
    UF_FLAG_PUBLIC,                                         // CORPSE_FIELD_CUSTOMIZATION_CHOICES+71
};

uint32 AreaTriggerUpdateFieldFlags[AREATRIGGER_END] = 
{
    UF_FLAG_PUBLIC,                                         // OBJECT_FIELD_GUID
    UF_FLAG_PUBLIC,                                         // OBJECT_FIELD_GUID+1
    UF_FLAG_PUBLIC,                                         // OBJECT_FIELD_GUID+2
    UF_FLAG_PUBLIC,                                         // OBJECT_FIELD_GUID+3
    UF_FLAG_DYNAMIC,                                        // OBJECT_FIELD_ENTRY
    UF_FLAG_DYNAMIC | UF_FLAG_URGENT,                       // OBJECT_DYNAMIC_FLAGS
    UF_FLAG_PUBLIC,                                         // OBJECT_FIELD_SCALE_X
    UF_FLAG_PUBLIC | UF_FLAG_URGENT,                        // AREATRIGGER_OVERRIDE_SCALE_CURVE
    UF_FLAG_PUBLIC | UF_FLAG_URGENT,                        // AREATRIGGER_OVERRIDE_SCALE_CURVE+1
    UF_FLAG_PUBLIC | UF_FLAG_URGENT,                        // AREATRIGGER_OVERRIDE_SCALE_CURVE+2
    UF_FLAG_PUBLIC | UF_FLAG_URGENT,                        // AREATRIGGER_OVERRIDE_SCALE_CURVE+3
    UF_FLAG_PUBLIC | UF_FLAG_URGENT,                        // AREATRIGGER_OVERRIDE_SCALE_CURVE+4
    UF_FLAG_PUBLIC | UF_FLAG_URGENT,                        // AREATRIGGER_OVERRIDE_SCALE_CURVE+5
    UF_FLAG_PUBLIC | UF_FLAG_URGENT,                        // AREATRIGGER_OVERRIDE_SCALE_CURVE+6
    UF_FLAG_PUBLIC | UF_FLAG_URGENT,                        // AREATRIGGER_EXTRA_SCALE_CURVE
    UF_FLAG_PUBLIC | UF_FLAG_URGENT,                        // AREATRIGGER_EXTRA_SCALE_CURVE+1
    UF_FLAG_PUBLIC | UF_FLAG_URGENT,                        // AREATRIGGER_EXTRA_SCALE_CURVE+2
    UF_FLAG_PUBLIC | UF_FLAG_URGENT,                        // AREATRIGGER_EXTRA_SCALE_CURVE+3
    UF_FLAG_PUBLIC | UF_FLAG_URGENT,                        // AREATRIGGER_EXTRA_SCALE_CURVE+4
    UF_FLAG_PUBLIC | UF_FLAG_URGENT,                        // AREATRIGGER_EXTRA_SCALE_CURVE+5
    UF_FLAG_PUBLIC | UF_FLAG_URGENT,                        // AREATRIGGER_EXTRA_SCALE_CURVE+6
    UF_FLAG_PUBLIC,                                         // AREATRIGGER_CASTER
    UF_FLAG_PUBLIC,                                         // AREATRIGGER_CASTER+1
    UF_FLAG_PUBLIC,                                         // AREATRIGGER_CASTER+2
    UF_FLAG_PUBLIC,                                         // AREATRIGGER_CASTER+3
    UF_FLAG_PUBLIC,                                         // AREATRIGGER_DURATION
    UF_FLAG_PUBLIC | UF_FLAG_URGENT,                        // AREATRIGGER_TIME_TO_TARGET
    UF_FLAG_PUBLIC | UF_FLAG_URGENT,                        // AREATRIGGER_TIME_TO_TARGET_SCALE
    UF_FLAG_PUBLIC | UF_FLAG_URGENT,                        // AREATRIGGER_TIME_TO_TARGET_EXTRA_SCALE
    UF_FLAG_PUBLIC,                                         // AREATRIGGER_SPELLID
    UF_FLAG_PUBLIC,                                         // AREATRIGGER_SPELL_FOR_VISUALS
    UF_FLAG_PUBLIC,                                         // AREATRIGGER_SPELL_X_SPELL_VISUAL_ID
    UF_FLAG_DYNAMIC | UF_FLAG_URGENT,                       // AREATRIGGER_BOUNDS_RADIUS_2D
    UF_FLAG_PUBLIC,                                         // AREATRIGGER_DECAL_PROPERTIES_ID
    UF_FLAG_PUBLIC,                                         // AREATRIGGER_CREATING_EFFECT_GUID
    UF_FLAG_PUBLIC,                                         // AREATRIGGER_CREATING_EFFECT_GUID+1
    UF_FLAG_PUBLIC,                                         // AREATRIGGER_CREATING_EFFECT_GUID+2
    UF_FLAG_PUBLIC,                                         // AREATRIGGER_CREATING_EFFECT_GUID+3
};

uint32 SceneObjectUpdateFieldFlags[SCENEOBJECT_END] = 
{
    UF_FLAG_PUBLIC,                                         // OBJECT_FIELD_GUID
    UF_FLAG_PUBLIC,                                         // OBJECT_FIELD_GUID+1
    UF_FLAG_PUBLIC,                                         // OBJECT_FIELD_GUID+2
    UF_FLAG_PUBLIC,                                         // OBJECT_FIELD_GUID+3
    UF_FLAG_DYNAMIC,                                        // OBJECT_FIELD_ENTRY
    UF_FLAG_DYNAMIC | UF_FLAG_URGENT,                       // OBJECT_DYNAMIC_FLAGS
    UF_FLAG_PUBLIC,                                         // OBJECT_FIELD_SCALE_X
    UF_FLAG_PUBLIC,                                         // SCENEOBJECT_FIELD_SCRIPT_PACKAGE_ID
    UF_FLAG_PUBLIC,                                         // SCENEOBJECT_FIELD_RND_SEED_VAL
    UF_FLAG_PUBLIC,                                         // SCENEOBJECT_FIELD_CREATEDBY
    UF_FLAG_PUBLIC,                                         // SCENEOBJECT_FIELD_CREATEDBY+1
    UF_FLAG_PUBLIC,                                         // SCENEOBJECT_FIELD_CREATEDBY+2
    UF_FLAG_PUBLIC,                                         // SCENEOBJECT_FIELD_CREATEDBY+3
    UF_FLAG_PUBLIC,                                         // SCENEOBJECT_FIELD_SCENE_TYPE
};

uint32 ConversationUpdateFieldFlags[CONVERSATION_END] = 
{
    UF_FLAG_PUBLIC,                                         // OBJECT_FIELD_GUID
    UF_FLAG_PUBLIC,                                         // OBJECT_FIELD_GUID+1
    UF_FLAG_PUBLIC,                                         // OBJECT_FIELD_GUID+2
    UF_FLAG_PUBLIC,                                         // OBJECT_FIELD_GUID+3
    UF_FLAG_DYNAMIC,                                        // OBJECT_FIELD_ENTRY
    UF_FLAG_DYNAMIC | UF_FLAG_URGENT,                       // OBJECT_DYNAMIC_FLAGS
    UF_FLAG_PUBLIC,                                         // OBJECT_FIELD_SCALE_X
    UF_FLAG_DYNAMIC,                                        // CONVERSATION_LAST_LINE_END_TIME
};

uint32 ConversationDynamicUpdateFieldFlags[CONVERSATION_DYNAMIC_END] = 
{
    UF_FLAG_PUBLIC,                                         // CONVERSATION_DYNAMIC_FIELD_ACTORS
    UF_FLAG_0x100,                                          // CONVERSATION_DYNAMIC_FIELD_LINES
};

