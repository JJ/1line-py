#!/usr/bin/env python3

import re
import sys
import glob
import json

if len(sys.argv) > 1:
    dir = sys.argv[1]
else:
    dir = "txt/"

if len(sys.argv) > 2:
    short_urls_json = sys.argv[2]
else:
    short_urls_json = "short-links.json"

with open( short_urls_json ) as data_file:
    short_urls = json.load(data_file)

dict_urls = {}

for u in short_urls:
    dict_urls[u[1]] = u[2]

ficheros = glob.glob(dir+"/*.md")
for f in ficheros:
    file_content = open(f,"r").read()
    file_content = re.sub(r'\[([^\]]+)\]\((http[^\(]+)\)',r'\1 → \2', file_content)

    for key in sorted(dict_urls,key=len,reverse=True):
        file_content = file_content.replace(key, dict_urls[key])
    f = f.replace('.md','-links.md')
    with open(f, "w") as links_file:
        links_file.write( file_content )
