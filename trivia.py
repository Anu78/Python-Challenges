import requests, json



r = requests.get("https://opentdb.com/api.php?amount=1&type=boolean").json()

print(r['results'])

# Work in progress
