class Card:
  def __init__(self,number, suit, show):
    self.number= number
    self.suit = suit
    self.show = show

  def cardList(self):
    return [self.number, self.suit, self.show]

  def inPlay(self):
    self.show=True

  def realCard(card):
    #if card is face up
    if card.show==True:
      #suit becomes a matrix of 6 rows for the suit shape
      suitString=[]
      if card.suit == "Heart":
        suitString = card.heart()
      elif card.suit== "Spade":
        suitString=card.spade()
      elif card.suit ==  "Diamond":
        suitString=card.diamond()
      elif card.suit == "Club":
        suitString=card.club()
      string = card.chrCard(card.number)
      lines = [[] for i in range(11)]
      lines[0].append("┌──────────┐")
      lines[1].append("│"+ string+ "        │")
      lines[2].extend(suitString[0])
      lines[3].extend(suitString[1])
      lines[4].extend(suitString[2])
      lines[5].extend(suitString[3])
      lines[6].extend(suitString[4])
      lines[7].extend(suitString[5])
      lines[8].append("│        "+string+"│")
      lines[9].append('└──────────┘')
      return lines
    else: #card is not flipped
      return card.flippedCard()

  def cardString(self):
    matrix=self.realCard()
    return matrix

  def chrCard(self,number):
    if number==1:
      return "A "
    elif number<10:
      return str(number)+" "
    elif number == 10:
      return str(number)
    elif number == 11:
      return "J "
    elif number == 12:
      return "Q "
    elif number == 13:
      return "K "

  #returns back of the card
  def flippedCard(self):
    lines = [['┌──────────┐'], ['│░░░░░░░░░░│'], ['│░░░░░░░░░░│'], ['│░░░░░░░░░░│'], ['│░░░░░░░░░░│'], ['│░░░░░░░░░░│'], ['│░░░░░░░░░░│'], ['│░░░░░░░░░░│'],['│░░░░░░░░░░│'], ['└──────────┘']]
    return lines

  def heart(self):
    heart=[[]for i in range(8)]
    heart[0].append("|  __  __  |")
    heart[1].append("| /  \\/  \\ |")
    heart[2].append("| \\      / |")
    heart[3].append("|  \\    /  |")
    heart[4].append("|   \\  /   |")
    heart[5].append("|    \\/    |")
    return heart

  #returns club drawing
  def club(self):
    club=[[]for i in range(8)]
    club[0].append("|    /\\    |")
    club[1].append("|  /    \\  |")
    club[2].append("| __\\  /__ |")
    club[3].append("|/        \\|")
    club[4].append("|\\__/||\\__/|")
    club[5].append("|   /__\\   |")
    return club

  #returns diamond drawing
  def diamond(self):
    diamond=[[]for i in range(8)]
    diamond[0].append("|    /\\    |")
    diamond[1].append("|  /    \\  |")
    diamond[2].append("| /      \\ |")
    diamond[3].append("| \\      / |")
    diamond[4].append("|  \\    /  |")
    diamond[5].append("|    \\/    |")
    return diamond

  #returns spade drawing
  def spade(self):
    spade=[[]for i in range(8)]
    spade[0].append("|    /\\    |")
    spade[1].append("|   /  \\   |")
    spade[2].append("| /      \\ |")
    spade[3].append("||        ||")
    spade[4].append("| \\_/||\\_/ |")
    spade[5].append("|   /__\\   |")
    return spade  

  