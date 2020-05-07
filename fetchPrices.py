import requests as rq
import json
import time
from datetime import datetime
from os.path import join

# URL to fetch bazaar data from
BASE_URL = r"https://api.hypixel.net/skyblock/bazaar"

# Fetch API key from creds.txt
with open(join("Resources","creds.txt"), 'r') as file:
    KEY = str(file.readlines()[0].rstrip())

# Set date for recording purposes
prices = {}
prices["time"] = datetime.now().strftime(r"%A %d %b - %H:%M %Z")
print(f"[TIME] {prices['time']}")

response = rq.get(BASE_URL+"?key="+KEY)
if response.status_code == 200:
    # Extract price from quick status response
    bazdat = response.json()['products']
else:
    raise ConnectionError(f"ERROR code from bazaar api: {response.status_code}")

for item in bazdat:
    sells=[x['pricePerUnit'] for x in bazdat[item]['sell_summary']]
    if sells!=[]:
        sell=max(sells)
    else:
        sell=0
    prices[item]=sell

# Save item prices in json file
with open(join("Resources","bazaarPrices.json"), 'w') as file:
    json.dump(prices, file, indent=3)

