#!/usr/bin/python3

import sys
import os
import dbd
import json
import re

wow_db_defs_dir = 'D:/Code/WoWDBDefs/WoWDBDefs/'
target_wow_ver = "1.14.0.40618"
trinity_db2metadata_file = "D:/Code/trinity_core/src/server/game/DataStores/DB2Metadata.h"

definitions_dir = wow_db_defs_dir + 'definitions/'
defintion_files = os.listdir(definitions_dir)

extracted_data = []

def extract_table_data(name, definition, columns):
    result = {
        "file_name": name,
        "class_name": name.split('.', 2)[0] + 'Meta',
        "layout": definition.layouts[-1],
        "fields": [],
        "field_count": 0,
        "file_field_count": 0,
        "index_field": -1,
        "relation_field": -1,
    }
    noninline_count = 0
    entry_index = 0
    for entry in definition.entries:

        annotation = entry.annotation
        if isinstance(annotation, str):
            annotation = [annotation]
            
        skip_field = False
        if 'noninline' in annotation and entry.column == 'ID':
            skip_field = True    
        
        if skip_field != True:    
            match_col = None
            for col in columns:
                if(col.name == entry.column):
                    match_col = col
                    break
                
            type_str = None
            if match_col.type == 'int':
                if(entry.int_width == 8):
                    type_str = 'FT_BYTE'
                elif(entry.int_width == 16):
                    type_str = 'FT_SHORT'
                elif(entry.int_width == 32):
                    type_str = 'FT_INT'
                elif(entry.int_width == 64):
                    type_str = 'FT_LONG' 
            elif match_col.type == 'float':
                type_str = 'FT_FLOAT'
            elif match_col.type == 'string':
                type_str = 'FT_STRING_NOT_LOCALIZED'
            elif match_col.type == 'locstring':
                type_str = 'FT_STRING'
            
            is_signed = 'false' if entry.is_unsigned else 'true'
            
            if entry.column == 'ID':
                is_signed = 'false'
            
            field = "{{ {type}, {arrsize}, {issigned} }},".format(
                type = type_str,
                arrsize = entry.array_size or 1,
                issigned = is_signed
            )
            
            result["fields"].append(field)
            result["field_count"] +=1
            
            annotation = entry.annotation
            if isinstance(annotation, str):
                annotation = [annotation]
            
            if 'id' in annotation and 'noninline' not in annotation:
                result['index_field'] = entry_index
                
            if 'relation' in annotation:
                result['relation_field'] = entry_index
                
            if 'noninline' in annotation:
                 noninline_count += 1
                
            entry_index +=1
        
    result['file_field_count'] = result['field_count'] - noninline_count
        
    return result

# start loading the files.
for def_file_name in defintion_files:
    def_file_path = os.path.join(definitions_dir, def_file_name)
    
    if os.path.isfile(def_file_path):
        valid_for_build = False
        parsed = dbd.parse_dbd_file(def_file_path)
        
        for definition in parsed.definitions:           
            for build in definition.builds:
                if str(build) == target_wow_ver:
                    extracted = extract_table_data(def_file_name, definition, parsed.columns)
                
                    if extracted:
                        extracted_data.append(extracted)
                        
                    valid_for_build = True
                    break
                
            if valid_for_build:
                print("Found for build - " + def_file_name)
                break




# we now have the relevant data extracted from wow db defs
# start looking at the db2 metadata file
# only simple matching is done - expecting structs all matching the same layout

def build_struct_string(extracted, file_id = '???'):
    str = ''
    
    str += 'struct ' + extracted['class_name'] + '\n'
    str += '{\n'
    str += '    static DB2Meta const* Instance() \n'
    str += '    {\n'
    str += '        static constexpr DB2MetaField fields[{count}] =\n'.format(count = extracted['field_count'])
    str += '        {\n'
    for field in extracted['fields']:
        str += '            ' + field + '\n' 
    str += '        };\n'
    str += '        static constexpr DB2Meta instance({file_id}, {index_field}, {field_count}, {file_field_count}, 0x{layout}, fields, {relation_field});\n'.format( \
            file_id=file_id, \
            index_field=extracted['index_field'], \
            field_count=extracted['field_count'], \
            file_field_count=extracted['file_field_count'], \
            relation_field=extracted['relation_field'], \
            layout=extracted['layout'] \
        )
    str += '        return &instance;\n'
    str += '    }\n'
    str += '};\n\n'
    
    return str

meta_content = ''
with open(trinity_db2metadata_file, 'r') as file:
    meta_content = file.read()
    
meta_parts = re.split('^struct\s|^\}\;', meta_content,  flags=re.MULTILINE)

with open(trinity_db2metadata_file+'.out.h', 'w') as outfile:
    last_index = len(meta_parts) - 1
    meta_index = 0
    
    outfile.write(meta_parts[0])
    
    for meta in meta_parts:
        if len(meta.strip()) > 0 and meta_index != 0 and meta_index != last_index:
            class_name = meta.split('\n', 1)[0]
            
            match_extract = None
            for extract in extracted_data:
                if extract['class_name'] == class_name:
                    match_extract = extract
                    break
                
            if match_extract == None:
                # not found new structure, keep old to be safe
                outfile.write('struct ' + meta + '};\n\n')
            else:
                pattern = '^\\s*static constexpr DB2Meta instance\\((\\d+),'
                match = re.search(pattern, meta, flags = re.MULTILINE)
                
                file_id = '???'
                if match != None:
                    file_id = match.group(1)

                struct_str = build_struct_string(match_extract, file_id)
                outfile.write(struct_str)
                extracted_data.remove(match_extract)
        
        meta_index+= 1
        
    print('Found {len} new structures'.format(len=len(extracted_data)) )
        
    for extracted in extracted_data:
        struct_str = build_struct_string(extracted)
        outfile.write(struct_str) 
    
    outfile.write(meta_parts[last_index])



