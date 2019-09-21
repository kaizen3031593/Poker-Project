class BoardState:
  def __init__(self,community,p1,p2):
    self.community = community
    self.p1 = p1
    self.p2 = p2
    self.printCardState()

  #prints line by line
  def printCard(self, lines):
    for line in lines:
      for piece in line:
        print(piece)

  #function that takes in a list of cards
  #returns a matrix of 5 cards lined up in a row to represent community cards
  def fiveCards(self):
    number = len(self.community)
    line=[[] for i in range(30)]
    for i in range(0,len(self.community)):
      cardLine = self.community[i].realCard()
      for j in range(0,len(cardLine)):
        line[j].extend(cardLine[j])
    final=[[] for i in range(50)]
    for i in range(10):
      final[i].append(line[i][0]+" "+line[i][1]+" "+line[i][2]+" "+line[i][3]+" "+line[i][4])
    return final

  #function that takes in a list of cards
  #returns a matrix of 2 cards lined up in a row to represent personal cards
  def twoCards(self, cards):
    line=[[] for i in range(30)]
    for i in range(0,len(cards)):
      cardLine = cards[i].realCard()
      for j in range(0,len(cardLine)):
        line[j].extend(cardLine[j])
    final=[[] for i in range(50)]
    for i in range(10):
      final[i].append(line[i][0]+" "+line[i][1])
    return final

  #function that takes in two sets of two cards
  #returns a single matrix with both cards combined
  def mergeTwoCards(self, cards1, cards2):
    merge = []
    for i in range(10):
      cardLine = cards1[i]+cards2[i]
      merge.append(cardLine)
    final=[[] for i in range(30)]
    for i in range(10):
      final[i].append(merge[i][0]+"\t\t\t   "+merge[i][1])
    return final

  #function prints 5 cards in the desired format
  def printCommunityCards(self):
    print("\t\t\t\t   ==== COMMUNITY CARDS ====")
    self.printCard(self.fiveCards())
    print("\t\t\t\t   =========================")

  #function prints 2 cards (player) and 2 cards (computer) in desired format
  def printYourAICards(self):
    print("  ==== YOUR CARDS ====\t\t\t\t    ==== COMPUTER CARDS ====")
    y=self.twoCards(self.p1)
    a=self.twoCards(self.p2)
    self.printCard(self.mergeTwoCards(y,a))

  #function prints the state of the game
  def printCardState(self):
    self.printCommunityCards()
    self.printYourAICards()