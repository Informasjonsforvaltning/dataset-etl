import json
import requests
import os

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-o', '--outputdirectory', help="the path to the directory of the output files", required=True)
args = parser.parse_args()

# data = json.loads('{"query":{"bool":{"must":[{"match_all":{}}],"must_not":[],"should":[]}},"from":0,"size":10000,"sort":[],"aggs":{}}')
host = 'http://dataset-catalogue:8080'
url = host + "/catalogs"
headers = {'Content-Type': 'application/json'}

print("Posting to the following url: ", url)
# Load the publisher by posting the data:
r = requests.post(url, headers=headers)
with open(args.outputdirectory + 'catalogs.json', 'w', encoding="utf-8") as outfile:
    json.dump(r.json(), outfile, ensure_ascii=False, indent=4)