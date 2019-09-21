import Card
import random

class Deck:
  def __init__(self):
    self.cards=[]
    self.build()
    self.shuffle()

  def build(self):
    for i in range(2,14):
      for j in ["Heart","Diamond","Club","Spade"]:
        self.cards.append(Card.Card(i,j,False))
        
  def pop(self):
    return self.cards.pop()

  def shuffle(self):
    random.shuffle(self.cards)