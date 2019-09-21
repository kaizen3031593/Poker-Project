class Player:
  def __init__(self,name, amount):
    self.name= name
    self.amount = amount
    #self.cards=cards

  def getName(self):
    return self.name

  def getAmount(self):
    return self.amount

  def getCards(self):
    return self.cards

  def setAmount(self,new):
    self.amount = new

  def makeDecision(self):
    if self.name=="FISH":
      return "BET"
    else:
      return "FOLD"
