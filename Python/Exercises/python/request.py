import requests;
import sys;
import json;

if len(sys.argv) != 2:
    sys.exit();

response = requests.get(f"https://itunes.apple.com/search?entity=song&limit=15&term={sys.argv[1]}")
# print(json.dumps(response.json(),indent=4));

for i in response.json()["results"]:
    print(i["trackName"]);