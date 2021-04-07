from random import shuffle, choice

''' Module containing Card and Deck class '''

class Card:
	def __init__(self, name, number = 0, assoc = []):
		self._name = name
		self.number = number
		self.assoc = assoc
		self.reversed = False
		self.power = "Kohzani Vahul Foris Manavit " + \
					 "Ahcarin Pulsarum Varelor " + \
					 "Qavalec Vortisrit Vooradu " + \
					 "Faras Curactem Asafaril" # magical words channeled using infernal energy 

	def __add__(self, item):
		if type(item).__name__ == "Card":
			return Deck([self, item])
		if type(item).__name__ == "Deck":
			tmp = Deck(item.cards)
			tmp.cards.append(self)
			return tmp

	def __neg__(self):
		self.reversed = not self.reversed;
		return self

	def __pos__(self):
		return self.number

	@property
	def name(self):
		if self.reversed:
			return "%s Reversed" % self._name
		else:
			return self._name

class Deck:
	cards = []

	def __init__(self, cards=[]):
		if len(cards) == 0:
			self.cards = []
		else:
			self.cards = cards

		self.power = "Mavoris Varasis Havoratim " + \
					 "Contarctura Variri Cunaver " + \
					 "Saverifsa Vasarasis Panvaru " + \
					 "Kuntani Magus Manas" # magical words channeled using infernal energy 

	def __add__(self, item):
		if type(item).__name__ == "Card":
			card_clone = self.cards[:]
			card_clone.append(item)
			return card_clone
		if type(item).__name__ == "Deck":
			card_clone1 = item.cards[:]
			card_clone2 = self.cards[:]
			for card in card_clone1:
				card_clone2 += card
			return card_clone2

	def __iadd__(self, item):
		if type(item).__name__ == "Card":
			self.cards.append(item)
			return self

		if type(item).__name__ == "Deck":
			card_clone1 = item.cards[:]
			for card in card_clone1:
				self.cards.append(card)
			return self

	def reveal(self):
		names = []
		for card in self.cards:
			names.append(card.name)
		return names

	def __invert__(self):
		shuffle(self.cards)
		for card in self.cards:
			if choice([True,False]):
				-card
		return self

	def __sub__(self, take_count):
		if take_count < 2:
			return self.cards.pop()
		else:
			popped = []
			for i in range(take_count):
				popped.append(self.cards.pop())
			return Deck(popped)

	def __rshift__(self, take_count):
		if (take_count < 2):
			return choice(self.cards)
		else:
			chosen = []
			clone = Deck(self.cards[:])
			~clone
			for i in range(take_count):
				chosen.append(clone.cards.pop())
			return Deck(chosen)

	def __contains__(self, card):
		return (card.name in self.reveal())

	def __getitem__(self, index):
		return self.cards[index]

	def __len__(self):
		return len(self.cards)

	def __neg__(self):
		for i in self.cards:
			-i
		return self

	def __pos__(self):
		sum_value = 0
		for card in self.cards:
			if not card.reversed:
				sum_value += card.number
			else:
				sum_value += card.number
		return sum_value

	def format(self, string):
		kcount = string.count("%s")
		return string%tuple(((~self)>>kcount).reveal())
