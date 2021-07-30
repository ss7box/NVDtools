#!/usr/bin/python

# system imports

import json
import sys

# 3rd party imports

import requests

#--- main ---

url = "https://services.nvd.nist.gov/rest/json/cves/1.0?keyword=openssl&pubStartDate=2021-07-17T00:00:00:000%20UTC-05:00"
r = requests.get(url, verify='/etc/ssl/certs').json()
print(json.dumps(r, indent=4))