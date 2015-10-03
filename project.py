from flask import Flask, render_template, request, redirect
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import exists
from database_setup import Base, AllCards, Users, Decks
import httplib2
import json
app = Flask(__name__)

engine = create_engine('sqlite:///hearthstonecards.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
def ListCards():
    cards = session.query(AllCards).all()
    return render_template('cardlayout.html', cards=cards)

@app.route('/cards/<cardname>/')
def DisplayCard(cardname):
    card = session.query(AllCards).filter_by(name=cardname).one()
    return render_template('card.html', card=card)

@app.route('/rarity/<rarity>/')
def ListRarity(rarity):
    if rarity == "basic":
        rarity = "free"
    cards = session.query(AllCards).filter_by(rarity=rarity.capitalize())
    return render_template('cardlayout.html', cards=cards)

@app.route('/class/<playerClass>')
def ListClass(playerClass):
    cards = session.query(AllCards).filter_by(faction=playerClass.capitalize())
    return render_template('cardlayout.html', cards=cards)

@app.route('/cost/<int:cost>')
def ListCost(cost):
    if cost < 7:
        cards = session.query(AllCards).filter_by(cost=cost)
    else:
        cards = session.query(AllCards).filter(AllCards.cost >= 7)
    return render_template('cardlayout.html', cards=cards)

@app.route('/set/<xset>')
def ListSet(xset):
    cards = session.query(AllCards).filter_by(x_set=xset)
    return render_template('cardlayout.html', cards=cards)

@app.route('/heroselection.html')
def ListHeroes():
    heroes = session.query(AllCards).filter(AllCards.typeOfCard=="Hero")
    return render_template('heroselection.html', heroes=heroes)

@app.route('/builddeck/<hero>')
def BuildDeck(hero):
    cards = session.query(AllCards).filter((AllCards.faction==hero) |
                                           (AllCards.faction=="Neutral"))
    return render_template('deckbuilding.html', cards=cards)

#Need to add deck name
#Probably something like '/savedeck/<deckname>'
@app.route('/savedeck/', methods=['POST'])
def saveDeck():
    deck = []
    if request.method == 'POST':
        temp = request.get_data()
        arr = temp.split("&")
        deckname = arr[0].split("=")[1].replace("+", " ")
        hero = arr[1].split("=")[1]
        for i in range(len(arr)-2):
            cardname = arr[i+2].split("=")[1]
            deck.append(cardname.replace("+", " "))
        deckstring = ','.join(deck)
        if session.query(Decks).filter(Decks.name==deckname).count():
            session.query(Decks).filter(Decks.name==deckname).one().decklist = deckstring
            session.commit()
            print(deckname + " already exists and was successfully edited")
        else:
            newDeck = Decks(name=deckname, decklist=deckstring, hero=hero)
            session.add(newDeck)
            session.commit()
            print(deckname + " was created successfully")
        #for u in session.query(Decks).filter(Decks.name==deckname).all():
        #    print u.__dict__
    return render_template('viewdeck.html', deck=deck, deckname=deckname,
                           hero=hero)

@app.route('/decks.html')
def listDecks():
    decks = session.query(Decks).all()
    name = []
    decklist = []
    hero = []
    for i in range(len(decks)):
        name[i] = decks[i].name
        decklist[i] = decks[i].decklist
        hero[i] = decks[i].hero
    return render_template('decks.html', name=name, decklist=decklist, hero=hero)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
