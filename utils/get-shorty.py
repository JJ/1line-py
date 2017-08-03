#!/usr/bin/env python3

import re
import sys
import glob
import json
import requests

if len(sys.argv) > 1:
    key = sys.argv[1]

if len(sys.argv) > 2:
    urls_json = sys.argv[2]
else:
    urls_json = "all-links.json"

with open( urls_json ) as data_file:
    urls = json.load(data_file)

shortened_links = []
for u in urls:
#    print(u)
    if (re.search("amzn.to",u[1])):
        shortened_links.append( [ u[0], u[1], u[1] ] )
    else:
        payload = json.dumps({'longUrl': u[1]})
        response = requests.post( "https://www.googleapis.com/urlshortener/v1/url?key="+key,
                              data=payload,
                              headers={'Content-type': 'application/json'})
        my_id = json.loads( response.text )
#        print(my_id)
        shortened_links.append( [ u[0], u[1], my_id['id'] ] )

print(json.dumps( shortened_links ))
