# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 18:32:32 2021

@author: icinsight
"""
from urllib.request import urlopen
import json
import requests
from jsonschema import validate

# https://pynative.com/python-json-validation/

# load the validation schema
url = 'https://uniswap.org/tokenlist.schema.json'
#url = 'https://raw.githubusercontent.com/Uniswap/token-lists/main/src/tokenlist.schema.json'
response = urlopen(url)
schema = json.loads(response.read())

# load a list to validate
url = "https://raw.githubusercontent.com/BlockTimeWorld/SwapMatic/master/swapmatic.tokenlist.json" # no duplicates
#url = "https://raw.githubusercontent.com/BlockTimeWorld/SwapMatic/master/beta.tokenlist.json" # has a duplicate

response = urlopen(url)
instance = json.loads(response.read())
validate(instance=instance, schema=schema)

# IF NO OUTPUT, LIST VALIDATION IS OK!

# finally, check if there are duplicates that will break the list
listdata = requests.get(url) #, headers=agent)
json_tree = json.loads(listdata.text)
resp = json_tree["tokens"]

address_collect_list = []
symbol_collect_list = []

for r in resp:
    
    address = r['address']
    symbol = r['symbol']
    
    print(address, symbol)
    
    if address.lower() in address_collect_list:
        print()
        print("################## Duplicate address", address)
        print()
        
    if symbol.upper() in symbol_collect_list:
        print()
        print("################## Duplicate symbol", symbol)
        print()
        
    address_collect_list.append(address.lower())
    symbol_collect_list.append(symbol.upper())
    
