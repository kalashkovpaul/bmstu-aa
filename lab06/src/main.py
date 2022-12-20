import json
from human import Human

with open('/Users/p.kalashkov/Desktop/fifthTerm/bmstu-aa/lab06/src/data/Humans.json', 'r') as file:
    data = file.read().replace('\n', '')
true_data = []
data = json.loads(data)
for d in data:
    r = d.get('result')
    h = Human(r.get('name'), r.get('gender'), r.get('country'), r.get('skill'), r.get('height'))
    item = {r.get('height'): h}
    true_data.append(h)
