import random
import time
import itertools
import Card
import Player
import Deck
import BoardState
import BetState

#flips over first 3 cards
def flop(cards):
  for i in range(3):
    cards[i].show=True
  return cards

#flips over fourth card
def turn(cards):
  cards[3].show=True
  return cards

#flips over last card
def river(cards):
  cards[4].show=True
  return cards

#function creates 2 cards for player
def createYourCards(deck):
  card1=deck.pop()
  card1.show=True
  card2=deck.pop()
  card2.show=True
  return [card1,card2]

#function creates 2 cards for computer
def createCompCards(deck):
  return [deck.pop(),deck.pop()]

#function creates 5 community cards
def createComCards(deck):
  return [deck.pop(),deck.pop(),deck.pop(),deck.pop(),deck.pop()]

#START poker hand checking functions
#-----------------------------------
def checkRoyalFlush(hand):
  if checkStraightFlush(hand):
    for card in hand:
      if card.number == 14:
        return True
  return False

def checkStraightFlush(hand):
  return checkStraight(hand) and checkFlush(hand)

def checkFourOfAKind(hand):
  freq = {}
  for card in hand:
        if card.number in freq:
            freq[card.number] += 1
        else:
            freq[card.number] = 1
  for number in freq:
    if freq[number]==4:
      return True
  return False

def checkFullHouse(hand):
  return checkThreeOfAKind(hand) and checkPairs(hand) == 1

def checkFlush(hand):
  suit = hand[0].suit
  for card in hand:
    if card.suit != suit:
      return False
  return True

def checkStraight(hand):
  numbers=[]
  for card in hand:
    numbers.append(card.number)
  numbers.sort()
  a = numbers[0]
  for i in range(len(numbers)):
    if a != numbers[i]:
      return False
    a+=1
  return True

def checkThreeOfAKind(hand):
  freq = {}
  for card in hand:
        if card.number in freq:
            freq[card.number] += 1
        else:
            freq[card.number] = 1
  for number in freq:
    if freq[number]==3:
      return True
  return False

def checkPairs(hand):
  freq = {}
  for card in hand:
        if card.number in freq:
            freq[card.number] += 1
        else:
            freq[card.number] = 1
  pairs = 0
  for number in freq:
    if freq[number]==2:
      pairs+=1
  return pairs

def yourHand(hand):
  if checkRoyalFlush(hand) == True:
    return ["A ROYAL FLUSH",1, hand]
  elif checkStraightFlush(hand) == True:
    return ["A STRAIGHT FLUSH",2, hand]
  elif checkFourOfAKind(hand) == True:
    return ["FOUR OF A KIND",3, hand]
  elif checkFullHouse(hand) == True:
    return ["A FULL HOUSE",4, hand]
  elif checkFlush(hand) == True:
    return ["A FLUSH",5, hand]
  elif checkStraight(hand) == True:
    return ["A STRAIGHT",6, hand]
  elif checkThreeOfAKind(hand) == True:
    return ["THREE OF A KIND",7, hand]
  elif checkPairs(hand) == 2:
    return ["TWO PAIRS",8, hand]
  elif checkPairs(hand) == 1:
    return ["A PAIR",9, hand]
  else:
    return ["A HIGH CARD",10, hand]

#function takes in two sorted lists of cards and returns correct winner
def checkOrder(hand1, hand2):
  while len(hand1)!=0 and len(hand2)!=0:
    if hand1[0].number>hand2[0].number:
      print("\t\t\t\t==== "+User.getName()+" HAS A HIGHER KICKER ====")
      return 1
    if hand1[0].number<hand2[0].number:
      print("\t\t\t\t==== "+Computer.getName()+" HAS A HIGHER KICKER ====")
      return 2
    else: 
      hand1.pop(0)
      hand2.pop(0)
  print("\t\t\t\t==== SAME HAND ====")

  return 3

def findPairs(hand):
  pairs=[]
  nonpairs=hand
  freq={}
  for card in hand:
    if card.number in freq:
      freq[card.number] += 1
    else:
      freq[card.number] = 1
  for card in hand:
      if freq[card.number]==2:
        pairs.append(card)
        nonpairs.remove(card)

  return [pairs,nonpairs] #returns list of list of cards(list)

def findThree(hand):
  freq={}
  for card in hand:
    if card.number in freq:
      freq[card.number]+=1
    else:
      freq[card.number] = 1
  for card in hand:
    if freq[card.number]==3:
      return card.number

def compareHighCard(hand1,hand2):
  hand1[2].sort(key=lambda x: x.number, reverse=True)
  hand2[2].sort(key=lambda x: x.number, reverse=True)
  return checkOrder(hand1[2],hand2[2])

def comparePair(hand1,hand2):
  pairs1=findPairs(hand1[2]) #hand of cards
  pairs2=findPairs(hand2[2]) #hand of cards
  if pairs1[0][0].number>pairs2[0][0].number:
    print("\t\t\t\t==== "+User.getName()+" HAS A BETTER PAIR ====")
    return 1
  elif pairs1[0][0].number<pairs2[0][0].number:
    print("\t\t\t\t==== "+Computer.getName()+" HAS A BETTER PAIR ====")
    return 2
  else: 
    pairs1[1].sort(key=lambda x: x.number, reverse=True)
    pairs2[1].sort(key=lambda x: x.number, reverse=True)
    return checkOrder(pairs1[1],pairs2[1])

def compareTwoPairs(hand1,hand2):
  pairs1=findPairs(hand1[2])
  pairs2=findPairs(hand2[2])
  if pairs1[0][0].number>pairs2[0][0].number:
    print("\t\t\t\t==== "+ User.getName() +" HAS A BETTER PAIR ====")
    return 1
  elif pairs1[0][0].number<pairs2[0][0].number:
    print("\t\t\t\t==== "+ Computer.getName() +" HAS A BETTER PAIR ====")
    return 2
  elif pairs1[0][1].number>pairs2[0][1].number:
    print("\t\t\t\t==== "+ User.getName()+" HAS A BETTER PAIR ====")
    return 1
  elif pairs1[0][1].number<pairs2[0][1].number:
    print("\t\t\t\t==== "+ Computer.getName()+" HAS A BETTER PAIR ====")
    return 2
  else: 
    pairs1[1].sort(key=lambda x: x.number, reverse=True)
    pairs2[1].sort(key=lambda x: x.number, reverse=True)
    return checkOrder(pairs1[1],pairs2[1])

def compareThrees(hand1,hand2):
  three1=findThree(hand1)
  three2=findThree(hand2)
  if three1>three2: 
    return 1
  elif three1<three2:
    return 2
  else:
    return compareHighCard(hand1,hand2)

#hand1 is a [string,order hierarchy, actual hand of cards]
def compareHands(hand1, hand2):
  #high card
  if hand1[1]==10:
    return compareHighCard(hand1,hand2)
  #check greater pair first
  elif hand1[1]==9:
    return comparePair(hand1,hand2)
  #check both pairs first
  elif hand1[1]==8:
    return compareTwoPairs(hand1,hand2)
  #check threes first
  elif hand1[1]==7:
    return compareThrees(hand1,hand2)
  #straight, just check for highest card
  elif hand1[1]==6:
    return compareHighCard(hand1,hand2)
  #flush, just check for highest card
  elif hand1[1]==5:
    return compareHighCard(hand1,hand2)
  #full house, check threes then twos
  elif hand1[1]==4:
    result = compareThrees(hand1,hand2)
    if result !=3:
      return result
    else:
      return comparePair(hand1,hand2)
  else:
    print("\t\t\t\t==== SAME HAND ====")
    return 3
#---------------------------------
#END poker hand checking functions

#function takes in a set of 6 or 7 cards and determines the best poker hand out of the different combinations
def nCr(cards,num):
  if len(cards) == 6:
    tempNumbers=list(findsubsets([0,1,2,3,4,5],5))
  if len(cards) == 7:
    tempNumbers=list(findsubsets([0,1,2,3,4,5,6],5))
  bestHand = ["A HIGH CARD",10,cards[:5]]
  for i in range(len(tempNumbers)):
    tempHand=[]
    for j in range(len(tempNumbers[0])):
      tempHand.append(cards[tempNumbers[i][j]])
    resultHand = yourHand(tempHand)
    if resultHand[1]<=bestHand[1]:
      bestHand = resultHand
  return bestHand

#function uses itertools to determine combinations of elements
def findsubsets(S,m):
    return set(itertools.combinations(S, m))


#PROGRAM STARTS HERE
print("\n\t\t\t==== WELCOME TO KAIZEN'S TEXAS HOLD-EM ====")
Computer=Player.Player("FISH",1000) #starting amount hardcoded in
User=Player.Player("PLAYER 1",1000)
pot=0
ante=10 #ante is hardcoded at 10

#continues while both players have money
while Computer.getAmount()>0 and User.getAmount()>0:
  fold=False
  deck = Deck.Deck()
  yourCards=createYourCards(deck) 
  AICards=createCompCards(deck) 
  cards=createComCards(deck)
  board=BoardState.BoardState(cards,yourCards, AICards)
  betState=BetState.BetState(User,Computer,ante)
  
  fold=betState.betting()
  if fold==True:
    print("\t\t\t\t==== " + Computer.getName() +
    " WINS ====")
    Computer.setAmount(Computer.getAmount()+pot)
  else:
    print("\t\t\t\t  ==== LETS SEE THE FLOP ====")
    dots="."
    for i in range(3):
      print(dots)
      dots+=" ."
      time.sleep(1)
    cards=flop(cards)
    board=BoardState.BoardState(cards,yourCards, AICards)
    print("\t\t\t\t==== "+User.getName()+ " HAS " + yourHand([yourCards[0],yourCards[1],cards[0],cards[1],cards[2]])[0] + " ====")
    fold=betState.betting()
    if fold==True:
      print("\t\t\t\t==== " + Computer.getName() + " WINS ====")
      Computer.setAmount(Computer.getAmount()+betState.getPot())
    else: 
      print("\t\t\t\t  ==== LETS SEE THE TURN ====")
      cards=turn(cards)
      board=BoardState.BoardState(cards,yourCards, AICards) 
      print("\t\t\t\t==== "+User.getName()+ " HAS "+ nCr([yourCards[0],yourCards[1],cards[0],cards[1],cards[2],cards[3]],6)[0] + " ====")
      fold=betState.betting()
      if fold==True:
        print("\t\t\t\t==== " + Computer.getName() + " WINS ====")
        Computer.setAmount(Computer.getAmount()+betState.getPot())
      else: 
        print("\t\t\t\t  ==== LET'S SEE THE RIVER ====")
        cards=river(cards)
        board=BoardState.BoardState(cards,yourCards, AICards)
        #printCardState(cards, yourCards, AICards)
        print("\t\t\t\t==== "+ User.getName()+" HAS "+ nCr([yourCards[0],yourCards[1],cards[0],cards[1],cards[2],cards[3],cards[4]],7)[0] + " ====")
        fold=betState.betting()
        if fold==True:
          print("\t\t\t\t\t==== " + Computer.getName() + " WINS ====")
          Computer.setAmount(Computer.getAmount()+betState.getPot())
        else:
          print("\t\t\t\t     ==== LETS REVEAL ====")
          time.sleep(2)
          AICards[0].show=True
          AICards[1].show=True
          board=BoardState.BoardState(cards,yourCards, AICards)
          time.sleep(2)
          print("\t\t\t\t==== " + Computer.getName() +" HAS "+ nCr([AICards[0],AICards[1],cards[0],cards[1],cards[2],cards[3],cards[4]],7)[0] + " ====")
          yourFinalHand=nCr([yourCards[0],yourCards[1],cards[0],cards[1],cards[2],cards[3],cards[4]],7)
          compFinalHand=nCr([AICards[0],AICards[1],cards[0],cards[1],cards[2],cards[3],cards[4]],7)
          if yourFinalHand[1]<compFinalHand[1]:
            print("\t\t\t\t==== " + User.getName()+" WINS ====")
            User.setAmount(User.getAmount()+betState.getPot())
          elif yourFinalHand[1]>compFinalHand[1]:
            print("\t\t\t\t==== " + Computer.getName() +" WINS ====")
            Computer.setAmount(Computer.getAmount()+betState.getPot())
          else:
            answer = compareHands(yourFinalHand,compFinalHand)
            if answer==1:
              print("\t\t\t\t==== " + User.getName() + " WINS ====")
              User.setAmount(User.getAmount()+betState.getPot())
            elif answer==2:
              print("\t\t\t\t==== " + Computer.getName() +" WINS ====")
              Computer.setAmount(Computer.getAmount()+betState.getPot())
            else: 
              print("\t\t\t\t==== IT'S A TIE ====")
              User.setAmount(User.getAmount()+int(betState.getPot()/2))
              Computer.setAmount(Computer.getAmount()+int(betState.getPot()/2))
  again= input("\t\t\t\t==== PLAY AGAIN? Y/N: ")
  if again!="Y":
    break
