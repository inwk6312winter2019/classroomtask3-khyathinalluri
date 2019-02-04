class card():
	suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
	rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7','8', '9', '10', 'Jack', 'Queen', 'King']
	"""this creates a card object"""
	def __init__(self,rank=0,suite=2):
		self.rank=rank
		self.suite=suite
	def __str__(self):
		return f"the rank is {card.rank_names[self.rank]} and the suite is {card.suit_names[self.suite]}"

	def __it__(self, other):
		t1 = self.suit, self.rank
		t2 = other.suit, other.rank
		return cmp(t1, t2)

	def __eq__(self,other):
		return self.rank == other.rank and self.suit == other.suit
class Deck(object):
	def __init__(self):
		self.cards = []
		for suit in range(4):
			for rank in range(1, 14):
				card = Card(suit, rank)
				self.cards.append(card)
	def pop_card(self):
		return self.card.pop()

ace_of_spade=card(1,3)
print(ace_of_spade)
