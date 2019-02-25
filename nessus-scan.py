#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Name: nessus-scan.py
Description: Example how to use the Nessus API 6.4 or greater to authenticate using accessKey and secretKey and output scan info as json
Author: Bryan Hutchins (greengeek)
"""

import requests
import json
import urllib3
import time

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

accessKey = "[YOUR_ACCESS_KEY]"
secretKey = "[YOUR_SECRET_KEY]"
headers   = {"Content-type": "application/json", "X-ApiKeys": "accessKey=" + accessKey + "; secretKey=" + secretKey}

# Get fileid and token
scanurl = "https://[NESSUS_SERVER_ADDRESS]:8834/scans/" 
scanpld = {"format":"nessus"}
results = requests.get(scanurl, headers=headers, data=scanpld, verify=False)
print (results.text)
