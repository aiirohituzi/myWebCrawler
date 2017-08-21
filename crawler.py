import requests
from bs4 import BeautifulSoup
import json
import os
import siteAdr

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MIN_RANGE = 1
MAX_RANGE = 1
data = ""
for i in range(MIN_RANGE, MAX_RANGE+1):
    req = requests.get(siteAdr.SITE_ADDRESS+str(i))

    html = req.text

    soup = BeautifulSoup(html, 'html.parser')

    keys = soup.select(
        'body > pre.keys'
    )

    data += keys[0].text
    print(data)
    
data = data.replace("Private Key                                            Address                            Compressed Address", "")
data = data.replace("+", "")

f = open("keys.txt", 'w')

for i in data:
    f.write(i)
f.close()


# with open(os.path.join(BASE_DIR, 'result.json'), 'w+') as json_file:
#     json.dump(data, json_file)