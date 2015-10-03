from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import json
from pprint import pprint

from database_setup import AllCards, Base

engine = create_engine('sqlite:///hearthstonecards.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

with open('allcards.json') as data_file:
    data = json.load(data_file)

for category in data:
    if (category == "Basic" or category == "Classic" or
    category == "Naxxramas" or category == "Goblins vs Gnomes" or
    category == "Promotion" or category == "Reward" or
    category == "Blackrock Mountain" or category == "The Grand Tournament"):
        for i in range(len(data[category])):
            cards = data[category][i]
            playerClass = ""
            if 'playerClass' not in cards:
                playerClass = "Neutral"
            else:
                playerClass = cards["playerClass"]
            cardCost = 0
            if not ("cost" not in cards):
                cardCost = cards["cost"]
            flavorText = ""
            if not ("flavor" not in cards):
                flavorText = cards["flavor"]
            cardArtist = ""
            if not ("artist" not in cards):
                cardArtist = cards["artist"]
            #print(cards["name"])
            card = AllCards(name = cards["name"], faction = playerClass,
                    rarity = cards["rarity"], cost = cardCost,
                    typeOfCard = cards["type"], x_set = cards["cardSet"],
                    img = cards["img"], imgGold = cards["imgGold"],
                    flavor = flavorText, artist = cardArtist)
            session.add(card)
            session.commit()
