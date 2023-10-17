#!/usr/bin/python3

import re
import sys

# tool for generating 'UpdateFieldFlags.cpp' based on the contents of 'UpdateFields.h'

updatefields_header = "D:/Code/trinity_core/src/server/game/Entities/Object/Updates/UpdateFields.h"
updatefieldsflags_header = "D:/Code/trinity_core/src/server/game/Entities/Object/Updates/UpdateFieldFlags.h"
updatefieldflags_source = "D:/Code/trinity_core/src/server/game/Entities/Object/Updates/UpdateFieldFlags.cpp"

out_filename = updatefieldflags_source + ".out.cpp"

updatefield_enums = []

# load in enum definitions from file
with open(updatefields_header, 'r') as file:
    current_enum_name = None
    enum_decl_prog = re.compile('^enum\s+([\w\d]*)\s*$')
    enum_start_prog = re.compile('.*{.*')
    enum_end_prog = re.compile('.*};.*')
    line_prog = re.compile('^\s*([\w\d]+)\s+=\s+([\w\d\s\+]+),(?:\s*//\s+(.*))?')
    
    state = 'SEARCH_ENUM'   # 'SEARCH_ENUM', 'HAVE_DECL', 'IN_ENUM'
    enum_decl = {
        "name": '',
        "lines": []
    }
    
    for line in file:
        if state == 'SEARCH_ENUM':
            match = enum_decl_prog.search(line)
            if match:
                state = 'HAVE_DECL'
                enum_decl['name'] = match.group(1)
                enum_decl['lines'] = []
        elif state == 'HAVE_DECL':
            match = enum_start_prog.search(line)
            if match:
                state = 'IN_ENUM'
        elif state == 'IN_ENUM':
            match = enum_end_prog.search(line)
            if match:
                state = 'SEARCH_ENUM'
                if enum_decl['name']:
                    updatefield_enums.append(enum_decl)
                enum_decl = {
                    "name": '',
                    "lines": []
                }
            else:
                match = line_prog.search(line)
                if(match):
                    enum_decl['lines'].append({'groups': match.groups()})
                else:
                    raise Exception("Unable to reliably match line: " + line)
    
# tidy comment attributes.
for enum_decl in updatefield_enums:
    for line in enum_decl['lines']:
        if(len(line['groups']) >= 3 and line['groups'][2]):
            line['attributes'] = {}
                
            parts = re.split('(\w+:)', line['groups'][2])
            parts = list(filter(len, [s.strip() for s in parts]))
            
            if((len(parts) % 2) != 0):
                raise Exception("Un-even amount of key/values for attributes.")
            
            for i in range(0, len(parts), 2):
                key = parts[i].strip(':')
                val = parts[i+1].rstrip(',')
                line['attributes'][key] = val
                
            
# we've now got the defintions
# now work out which are needed
var_decls = []
with open(updatefieldsflags_header, 'r') as file:
    var_decl_prog = re.compile('^\s+TC_GAME_API\sextern\suint32\s([\w\d]+)\[([\w\d]+)];')
    for line in file:
        match = var_decl_prog.search(line)
        if match:
            var_decls.append(match.groups())
            


def get_nested_enum_tree(end_name, current_enum_name):
    found_enum = None
    for enum_decl in updatefield_enums:
        if(enum_decl['name'] != current_enum_name):
            for line in enum_decl['lines']:
                if end_name == line['groups'][0]:
                    found_enum = (enum_decl)
        
    if found_enum:
        first_line_val = found_enum['lines'][0]['groups'][1]
        first_line_val = first_line_val.split('+')[0].strip()
        enums = get_nested_enum_tree(first_line_val, found_enum['name'])
        enums.append(found_enum)
        return enums

    return []

def rewrite_flag(org_flag):
    return 'UF_FLAG_'+(org_flag.strip())

# now start building the final type
with open(out_filename, 'w') as outfile:
    for var_decl in var_decls:
        out_def = {}
        enums_nested = get_nested_enum_tree(var_decl[1], None)
        
        for enum_decl in updatefield_enums:
            for line in enum_decl['lines']:
                if var_decl[1] == line['groups'][0]:
                    top_level_enum = enum_decl
        
        if len(enums_nested) == 0:
            raise Exception("Failed to find matching enum value: "+ var_decl[1])
        
        outfile.write("uint32 " + var_decl[0] + '[' + var_decl[1] + '] = \n')
        outfile.write('{\n')
        
        for enum_def in enums_nested:
            for line in enum_def['lines']:
                if 'attributes' in line:
                    size_str = line['attributes']['Size'] if 'Size' in line['attributes'] else 1
                    flags_str = ' | '.join(map(rewrite_flag, line['attributes']['Flags'].split(',')))
                    
                    prefix = '    ' + flags_str + ','
                    start_line = prefix.ljust(60)
                    
                    
                    for i in range(0, int(size_str)):
                        label = line['groups'][0]
                        if i > 0:
                            label += '+' + str(i)
                            
                        
                            
                        outfile.write(start_line + '// ' + label + '\n')        
        
        outfile.write('};\n\n')
        