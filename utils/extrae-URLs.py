#!/usr/bin/env python3

import re
import sys
import glob
import json

if len(sys.argv) > 1:
    dir = sys.argv[1]
else:
    dir = "txt/"

ficheros = glob.glob(dir+"/*.md")

all_links = []
for f in ficheros:
    file_content = open(f,"r").read()
    links = re.findall('\[([^\]]+)\]\((http[^\(]+)\)',file_content)
    for text,link in links:
        all_links.append( [ text, link] )
        
print(json.dumps( all_links ) )
                         
    
