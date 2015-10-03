import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class AllCards(Base):
    __tablename__ = 'all_cards'

    id = Column(Integer)
    name = Column(Text, primary_key=True)
    faction = Column(Text)
    rarity = Column(Text)
    cost = Column(Integer)
    typeOfCard = Column(Text)
    x_set = Column(Text)
    img = Column(Text)
    imgGold = Column(Text)
    flavor = Column(Text)
    artist = Column(Text)

class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(Text)
    email = Column(Text)

class Decks(Base):
    __tablename__ = 'decks'

    id = Column(Integer, ForeignKey('users.id'))
    name = Column(Text, primary_key=True)
    decklist = Column(Text)
    hero = Column(Text)

engine = create_engine('sqlite:///hearthstonecards.db')

Base.metadata.create_all(engine)
