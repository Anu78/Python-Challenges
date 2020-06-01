import requests, json

r = requests.get("https://opentdb.com/api.php?amount=1&type=boolean")
r = r.text

questions = json.loads(r)

print(questions.get('question'))