from random import shuffle

# Two useful variables to create cards 
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

class Deck:
  """
    This is Deck Class. The object will create a deck of cards to initiate play. You can then use this Deck list of cards to split in half and give to the players. It will use SUITE and RANKS to create the deck. It should also have methods for splitting the deck in half and shuffling the deck.
  """

  def __init__(self):
    print("Creating new ordered deck")
    self.cards = []
    for s in SUITE:
      for r in RANKS:
        self.cards.append((s,r))
    print(self.cards)
  
  def shuffleDeck(self):
    shuffle(self.cards)
  
  def split(self):
    len_cards = len(self.cards)
    return self.cards[:len_cards//2], self.cards[len_cards//2:]


class Hand:
  """
    This is the Hand class. Each player has a Hand, and can add or remove cards from that hand. There should be an add and remove card method here
  """
  def __init__(self, cards):
    self.cards = cards

  def __str__(self):
    return "Contains {} cards".format(len(self.cards))

  def addCard(self, card):
    self.cards.extend(card)

  def removeCard(self):
    return self.cards.pop()

class Player:
  """
  This is the player class, which takes in a name and an instance of a Hand class object. The player can then play cards and check if they still have cards. 
  """

  def __init__(self, name, hand):
    self.name = name
    self.hand = hand 
  
  def isCardsLeft(self):
    return len(self.hand.cards) > 0
  
  def playCard(self):
    drawn_card = self.hand.removeCard()
    print("{} has placed: {}".format(self.name, drawn_card))
    print("\n")
    return drawn_card
  
  def removeWarCards(self):
    war_cards = []
    # Draw 3 cards for war (or however many are left)
    for x in range(min(3, len(self.hand.cards))):
      war_cards.append(self.hand.removeCard())
    
    return war_cards


# Create a new Deck and split in half
deck = Deck()
deck.shuffleDeck()
half1, half2 = deck.split()

# Create both players
comp = Player("computer", Hand(half1))

name = input("What is your name? ")
user = Player(name, Hand(half2))

total_rounds = 0
war_count = 0

print("Let's play War!")
print("=" * 50)

while user.isCardsLeft() and comp.isCardsLeft():
  total_rounds += 1
  print(f"\n=== ROUND {total_rounds} ===")
  print("Current standings:")
  print(f"{user.name} has {len(user.hand.cards)} cards")
  print(f"{comp.name} has {len(comp.hand.cards)} cards")
  print("Play a card!")
  print()

  table_cards = []

  c_card = comp.playCard()
  u_card = user.playCard()
  
  table_cards.append(c_card)
  table_cards.append(u_card)

  print(f"Computer plays: {c_card}")
  print(f"{user.name} plays: {u_card}")

  # Check if it's a tie (war)
  if c_card[1] == u_card[1]:
    war_count += 1
    print("WAR!")
    
    # Check if players have enough cards for war
    if len(user.hand.cards) < 3 or len(comp.hand.cards) < 3:
      print("Not enough cards for war! Game ends.")
      break
    
    # Draw war cards
    user_war_cards = user.removeWarCards()
    comp_war_cards = comp.removeWarCards()
    
    table_cards.extend(user_war_cards)
    table_cards.extend(comp_war_cards)
    
    print(f"{user.name} draws 3 war cards")
    print(f"{comp.name} draws 3 war cards")
    
    # Draw one more card to compare for war
    if user.isCardsLeft() and comp.isCardsLeft():
      c_war_card = comp.playCard()
      u_war_card = user.playCard()
      table_cards.append(c_war_card)
      table_cards.append(u_war_card)
      
      print(f"War comparison: {comp.name} plays {c_war_card}, {user.name} plays {u_war_card}")
      
      # Compare war cards - higher rank wins
      if RANKS.index(c_war_card[1]) < RANKS.index(u_war_card[1]):
        user.hand.addCard(table_cards)
        print(f"{user.name} wins the war and gets all cards!")
      else:
        comp.hand.addCard(table_cards)
        print(f"{comp.name} wins the war and gets all cards!")
    else:
      # If someone ran out of cards during war, give remaining cards to the other player
      if user.isCardsLeft():
        user.hand.addCard(table_cards)
        print(f"{user.name} wins by default!")
      else:
        comp.hand.addCard(table_cards)
        print(f"{comp.name} wins by default!")
  
  else:
    # Normal round - higher rank wins
    if RANKS.index(c_card[1]) > RANKS.index(u_card[1]):
      comp.hand.addCard(table_cards)
      print(f"{comp.name} wins this round!")
    else:
      user.hand.addCard(table_cards)
      print(f"{user.name} wins this round!")

# Game over
print("\n" + "=" * 50)
print("GAME OVER!")
print(f"Total rounds played: {total_rounds}")
print(f"Wars occurred: {war_count}")

if len(user.hand.cards) > len(comp.hand.cards):
  print(f"{user.name} wins the game!")
elif len(comp.hand.cards) > len(user.hand.cards):
  print(f"{comp.name} wins the game!")
else:
  print("It's a tie!")

print(f"Final score - {user.name}: {len(user.hand.cards)}, {comp.name}: {len(comp.hand.cards)}")