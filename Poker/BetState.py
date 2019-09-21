import Player
import time

class BetState:
  def __init__(self,Player1,Player2,ante):
    self.p1=Player1
    self.p2=Player2
    self.ante=ante
    self.pot=0

  #function prints the amount each player has as well as the pot
  def printBetState(self):
    print("  ==== YOUR AMOUNT ====\t\t\t       ==== COMPUTER AMOUNT ====")
    print("\t\t  $"+ str(self.p1.getAmount()) + "\t\t\t\t\t\t\t\t      $" + str(self.p2.getAmount()))
    print("  ========================== POT ===============================")
    print("\t\t\t\t\t\t\t$" + str(self.pot))
    print("\t\t\t\t   =========================")

  def getPot(self):
    return self.pot

  #function works through the betting phase of each round
  def betting(self):
    ripe=False
    newFold=False
    while ripe!=True and newFold==False:
      self.printBetState()
      action = input("\t\t\t\t==== ACTION: BET/RAISE/FOLD ====\n\t\t==== $" + str(self.ante) +" TO PLAY. ENTER AMOUNT (F=FOLD): \t")
      if action.isdigit() != True:
        newFold=True
      else:
        time.sleep(1)
        if self.p2.makeDecision()=="BET":
          print("\t\t\t\t===== " + self.p2.getName() + " MATCHES ====")
          self.p1.setAmount(self.p1.getAmount()-int(action))
          self.p2.setAmount(self.p2.getAmount()-int(action))
          self.pot+=int(action)*2
          ripe=True
    self.printBetState()
    time.sleep(1)
    return newFold