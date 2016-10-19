import random

class Card (object):
  RANKS = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)

  SUITS = ('C', 'D', 'H', 'S')

  def __init__ (self, rank = 12, suit = 'S'):
    if (rank in Card.RANKS):
      self.rank = rank
    else:
      self.rank = 12

    if (suit in Card.SUITS):
      self.suit = suit
    else:
      self.suit = 'S'

  def __str__ (self):
    if (self.rank == 14):
      rank = 'A'
    elif (self.rank == 13):
      rank = 'K'
    elif (self.rank == 12):
      rank = 'Q'
    elif (self.rank == 11):
      rank = 'J'
    else:
      rank = str (self.rank)
    return rank + self.suit

  def __eq__ (self, other):
    return (self.rank == other.rank)

  def __ne__ (self, other):
    return (self.rank != other.rank)

  def __lt__ (slef, other):
    return (self.rank < other.rank)

  def __le__ (self, other):
    return (self.rank <= other.rank)

  def __gt__ (self, other):
    return (self.rank > other.rank)

  def __ge__ (self, other):
    return (self.rank >= other.rank)

class Deck (object):
  def __init__ (self):
    self.deck = []
    for suit in Card.SUITS:
      for rank in Card.RANKS:
        card = Card (rank, suit)
        self.deck.append (card)

  def shuffle (self):
    random.shuffle (self.deck)

  def deal (self):
    if (len(self.deck) == 0):
      return None
    else:
      return self.deck.pop(0)

class Poker (object):
  def __init__ (self, num_players):
    self.deck = Deck()
    self.deck.shuffle()
    self.players = []
    numcards_in_hand = 5

    for i in range (num_players):
      hand = []
      for j in range (numcards_in_hand):
        hand.append (self.deck.deal())
      self.players.append (hand)

  def play (self):
    #  Sort the hands of each player
    for i in range (len(self.players)):
      sortedHand = sorted (self.players[i], reverse = True)
      self.players[i] = sortedHand
      hand = ''
      for card in sortedHand:
        hand = hand + str (card) + ' '
      print ('Player ' + str (i + 1) + ' : ' + hand)

    # determine each type of hand and print
    points_hand = []

    # determine winner and print


  def is_royal (self, hand):
    same_suit = True
    for i in range (len(hand) - 1):
      same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)
    if (not same_suit):
      return False

    rank_order = True
    for i in range (len(hand)):
      rank_order = rank_order and (hand[i].rank == 14 - i)

    return (same_suit and rank_order)
    
  def is_straight_flush (self, hand):
    for i in range (len(hand) - 4):
      if (hand[i].rank == hand[i + 1].rank + 1) and (hand[i].rank == hand[i + 2].rank + 2) and (hand[i].suit == hand[i + 1].suit) and (hand[i].suit == hand[i + 2].suit):
        if (hand[i].rank == hand[i + 3].rank + 3) and (hand[i].rank == hand[i + 4].rank + 4) and (hand[i].suit == hand[i + 3].suit) and (hand[i].suit == hand[i + 4].suit):
          return True
    return False

  def is_four_kind (self, hand):
    for i in range (len(hand) - 3):
      if (hand[i].suit == hand[i + 1].suit) and (hand[i] == hand[i + 2]):
        if (hand[i].suit == hand[i + 3].suit) and (hand[i] == hand[i + 4]):
          return True
    return False

  def is_full_house (self, hand):
    for i in range (len(hand) - 4):
      if (hand[i].rank == hand[i + 1].rank) and (hand[i].rank == hand[i + 2].rank):
        if (hand[i + 3].rank == hand[i + 4].rank):
          return True
      if (hand[i].rank == hand[i + 1].rank):
        if (hand[i + 2].rank == hand[i + 3].rank) and (hand[i + 2].rank == hand[i + 4].rank):
          return True
    return False

  def is_flush (self, hand):
    for i in range (len(hand) - 4):
      if (hand[i].suit == hand[i + 1].suit) and (hand[i].suit == hand[i + 2].suit):
        if (hand[i].suit == hand[i + 3].suit) and (hand[i].suit == hand[i + 4].suit):
          return True
    return False

  def is_straight (self, hand):
    for i in range (len(hand) - 4):
      if (hand[i].rank == hand[i + 1].rank + 1) and (hand[i].rank == hand[i + 2].rank + 2):
        if (hand[i].rank == hand[i + 3].rank + 3) and (hand[i].rank == hand[i + 4].rank + 4):
          return True
    return False

  def is_three_kind (self, hand):
    for i in range (len(hand) - 2):
      if (hand[i].rank == hand[i + 1].rank) and (hand[i].rank == hand[i + 2].rank):
        return True
    return False

  def is_two_pair (self, hand):
    for i in range (len(hand) - 3):
      if (hand[i].rank == hand[i + 1].rank) and (hand[i + 2].rank == hand[i + 3].rank):
        return True
    return False

  # determine if a hand is one pair
  def is_one_pair (self, hand):
    for i in range (len(hand) - 1):
      if (hand[i].rank == hand[i + 1].rank):
        return True
    return False

  # determine if a hand is high card
  def is_high_card (self, hand):
    for i in range (len(hand) - 1):
      if (hand[i].rank == hand[i + 1].rank):
        return False
    return True

def main():
  #  Prompt user to enter the nuimber of players
  num_players = int (input ('Enter number of players: '))
  while ((num_players < 2) or (num_players > 6)):
    num_players = int (input ('Enter number of players(must be less than 6 or greater than 2): '))

  #  Create the poker object
  game = Poker (num_players)

  #  Play the game
  game.play()

main()