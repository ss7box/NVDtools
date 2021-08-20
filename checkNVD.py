#!/usr/bin/python3.8

# system imports

import json
import sys

# 3rd party imports

import requests

#--- main ---


base = "https://services.nvd.nist.gov/rest/json/cves/1.0?keyword="
date = "2021-08-15"
startDate = "&pubStartDate=" + date +"T00:00:00:000%20UTC-05:00"

#urlOpenssl = "https://services.nvd.nist.gov/rest/json/cves/1.0?keyword=openssl&pubStartDate=2021-07-17T00:00:00:000%20UTC-05:00"
#urlTuxedo = "https://services.nvd.nist.gov/rest/json/cves/1.0?keyword=tuxedo&pubStartDate=2021-02-10T00:00:00:000%20UTC-05:00"

urlTuxedo = base + "tuxedo" + startDate
urlOpenssl = base + "openssl" + startDate

r = requests.get(urlOpenssl, verify='/etc/ssl/certs').json()
print(json.dumps(r, indent=4))

r = requests.get(urlTuxedo, verify='/etc/ssl/certs').json()
print(json.dumps(r, indent=4))
