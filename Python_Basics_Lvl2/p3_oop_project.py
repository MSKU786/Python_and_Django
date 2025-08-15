from random import shuffle

# Two useful variables to create cards 

SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

class Deck:
  """
    This is Deck Class. The object will create a deck of cards to initate play. You can then use this Deck list of artds to split in half and give to the player.s It will use SUITE and RANKS to create the dec. It should aslo have a methods for spllitting the deck in half and shuffling the deck.
  """

  def __init__(self):
    print("Creating new orderd deck")
    self.cards = []
    for s in SUITE:
      for r in RANKS:
        self.cards.append(s+'_'+r)
    print(self.cards)
  
  def shuffleDeck(self):
    return shuffle(self.cards)
  
  def split(self):
    len_cards = len(self.cards)
    return self.cards[:len_cards//2], self.cards[len_cards//2:]


class Hand:
  """
    This is the Handclass. each player has a Hand, and can add or remove cards from that hand. There should be an add and remove card method here
  """
  def __init__(self, cards):
    self.cards = cards

  def addCard(self, card):
    temp = self.cards
    self.cards = [card]
    self.cards.append(temp)

  def removeCard(self):
    return self.cards.pop()

class Player:
  """
  This is the player class, whichc takes in a name an instance of a Hand class object. The player can they play cards and check if they still have cards. 
  """

  def __init__(self, name, hand):
    self.name = name
    self.hand = hand 
  
  def isCardsLeft(self):
    return self.hand.cards.length > 0

deck = Deck()
deck.shuffleDeck()
p1,p2 = deck.split()
print(p1)
print(p2)