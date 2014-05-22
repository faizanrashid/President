class Player(object):
	
	''' A player in the model '''
	def __init__(self, name):
		''' Initialize the player object'''
		self.name = name
		self.title = None
		self.cards = []
		self.cards_selected = []

	def discard_card(self, cards):
		''' Play a card from the hand'''
		for card in cards:
			self.cards.remove(card)

	def add_card(self, cards):
		'''Add a card to the hand '''
		self.cards.append(cards)

	def select(self, card):
		'''Select the card'''
		self.cards.remove(card)
		self.cards_selected.append(card)

	def make_move(self):
		'''Discard the selected cards'''
		self.cards_selected = []

	def unselect_all(self):
		'''unselect all cards'''
		
		for card in self.cards_selected:
			self.cards.append(card)

		self.cards_selected = []