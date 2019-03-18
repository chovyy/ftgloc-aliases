#!/usr/bin/python

'''
@author: Christian Hovy
'''

from __future__ import print_function
import argparse
import json

def main():
    argParser = argparse.ArgumentParser(description='Searches in for ftg:loc doublettes in Serialbox2 meta data files.');
    args = parseArguments(argParser)
    jsonData = open(args.file).read()
    jsonDict = json.loads(jsonData)
    fieldMap = jsonDict['field_map']
    doublettes = findDoublettes(fieldMap)
    for loc, fields in doublettes.items():
        print(loc + ':')
        for field in fields:
            print('    ' + field) 
        
def parseArguments(argParser):
    argParser.add_argument('file', help="MetaData-*.json file");
    return argParser.parse_args();    
    
def findDoublettes(fieldMap):
    locs = dict()
    for field, meta in fieldMap.items():
        metaInfo = meta['meta_info']
        if 'ftg:loc' in metaInfo:
            loc = metaInfo['ftg:loc']['value']
            if not loc in locs:
                locs[loc] = []
            locs[loc].append(field)
    
    return {loc: fields for loc, fields in locs.items() if len(fields) > 1} 

if __name__ == "__main__":
    main()
