#!/usr/bin/python3
#
# Converts fontawesome css to json file for easier parsing
# Can be grabbed from https://use.fontawesome.com/releases/v5.3.1/css/all.css
import json

cssfile = open("fa-all.css", "r").readlines()[4]
css = cssfile.split('}')

names = {}

for rule in css:
    if ".fa-" in rule:
        name = rule.split(':')[0].replace('.fa-', '')
        if "{" not in name and name != "":
            names[name] = rule.split(':')[0]

with open("fa-icons.json", "w") as json_file:
	json.dump(names, json_file, indent=4)
