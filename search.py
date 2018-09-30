#!/usr/bin/python3
#
# Searches json file for specific string
import json
import sys

with open("fa-icons.json", "r") as json_file:
	faicons = json.load(json_file)

result = None

if len(sys.argv) > 1:
    name = sys.argv[1]
else:
    name = input("Search for icon: ")

for k in faicons:
    if name in k:
        print(faicons[k])