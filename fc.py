#!/usr/bin/env python3
# Tasha, March 28 2018
# write program to connect to Foundation Center API
# based on these Python 3.5+ instructions https://api.foundationcenter.org/docs/v2.0/documentation.html#/README


import json
from urllib import request

url = "https://api.foundationcenter.org/v2.0/aggregates/funding"
opts = {"year": 2015, "subject": "SA"}

req = request.Request(url, data=json.dumps(opts).encode('utf8'),
                      headers={"Content-Type": "application/json"})
req.add_header("x-fc-api-key", "YourAPI key")

response = request.urlopen(req).read().decode('utf8')
response_dict = json.loads(response)
print(response_dict["data"]["results"][0]["number_of_grants"])
