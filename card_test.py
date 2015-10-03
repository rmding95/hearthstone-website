import json
from pprint import pprint

with open('allcards.json') as data_file:
    data = json.load(data_file)

#print(data["Classic"][0]["name"])
count = 0;
for category in data:
    if (category == "Basic" or category == "Classic" or
    category == "Naxxramas" or category == "Goblins vs Gnomes" or
    category == "Promotion" or category == "Reward" or
    category == "Blackrock Mountain" or category == "The Grand Tournament"):
        for i in range(len(data[category])):
            card = data[category][i]
            print(card["name"])
            print(card["rarity"])
            count += 1
print(count)
