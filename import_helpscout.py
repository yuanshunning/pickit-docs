#!/usr/bin/env python
# Quick and dirty script to convert helpscout documentation to .rst files.
import requests
import pypandoc
import os
import sys
from requests.auth import HTTPBasicAuth

apikey = sys.argv[1]
auth = HTTPBasicAuth(apikey, 'X')

collections = requests.get('https://docsapi.helpscout.net/v1/collections', auth=auth).json()
keepcharacters = (' ','_')


for k in collections["collections"]["items"]:
  print("Importing collection '{0}'...".format(k["name"]))

  dirname = k["name"].lower()
  dirname = "".join(c for c in dirname if c.isalnum() or c in keepcharacters).rstrip().replace(' ','_')

  directory = os.path.join("docs", dirname)

  if not os.path.exists(directory):
    os.makedirs(directory)

  collection = requests.get('https://docsapi.helpscout.net/v1/collections/{0}/articles'.format(k["id"]), auth=auth).json()
  for article in collection["articles"]["items"]:
    print(" - Importing article '{0}'...".format(article["name"]))

    artcl = requests.get('https://docsapi.helpscout.net/v1/articles/{0}'.format(article["id"]), auth=auth).json()

    # Add title to each article
    text = "<h1>{0}</h1>{1}".format(article["name"], artcl["article"]["text"].encode('utf8'))

    output = pypandoc.convert_text(text, 'rst', format='html')

    filename = article["name"].lower()
    filename = "".join(c for c in filename if c.isalnum() or c in keepcharacters).rstrip().replace(' ','_')
    filepath = os.path.join(directory, "{0}.rst".format(filename))
    with open(filepath, "w") as text_file:
      text_file.write(output.encode('utf8'))
