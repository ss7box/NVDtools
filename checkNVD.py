#!/usr/bin/python3.8

# system imports

import json
import sys

# 3rd party imports

import requests

#--- main ---

if len(sys.argv) != 2:
    print ('ERROR:missing search start date (YYYY-MM-DD)')
    sys.exit(-1)

base = "https://services.nvd.nist.gov/rest/json/cves/1.0?keyword="
#date = "2021-08-15"
date = sys.argv[1]
startDate = "&pubStartDate=" + date +"T00:00:00:000%20UTC-05:00"

#urlOpenssl = "https://services.nvd.nist.gov/rest/json/cves/1.0?keyword=openssl&pubStartDate=2021-07-17T00:00:00:000%20UTC-05:00"
#urlTuxedo = "https://services.nvd.nist.gov/rest/json/cves/1.0?keyword=tuxedo&pubStartDate=2021-02-10T00:00:00:000%20UTC-05:00"

urlTuxedo = base + "tuxedo" + startDate
urlOpenssl = base + "openssl" + startDate

print ('Openssl results:')
r = requests.get(urlOpenssl, verify='/etc/ssl/certs').json()
print(json.dumps(r, indent=4))

print ('Oracle Tuxedo results:')
r = requests.get(urlTuxedo, verify='/etc/ssl/certs').json()
print(json.dumps(r, indent=4))

sys.exit(0)
