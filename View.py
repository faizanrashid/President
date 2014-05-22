class View(object):
	''' The view for the game '''

	def __init__(self, game):
		'''Initializes the view '''
		self.game = game
		self.players = game.players
		self.field = game.field
		self.players_in_round = game.players_in_round
		self.winners = game.winners
		self.curr_turn = game.curr_turn
		self.game_over = False

	def update(self):
		''' get all the current information from the Model '''

		self.players = self.game.players
		self.field = self.game.field
		self.players_in_round = self.game.players_in_round
		self.winners = self.game.winners
		self.curr_turn = self.game.curr_turn
		self.game_over = self.game.game_over

	def before_start_show(self):
		'''Show this before you start the game'''

		print "The current players are: \n" + '\n'.join([player.name for player in self.players])
		print "Time to add players, you must add atleast two"

	def show(self):
		'''show the current state of the game '''
		print [player.name for player in self.players_in_round]
		print [player.name for player in self.players]
		print "\n\nThe current cards on the field are: \n" + "\n".join([card.name for card in self.field])
		print "\n\n It's " + self.curr_turn.name + " turn:"
		cards = sorted(self.curr_turn.cards, key= lambda card: card.num)
		count = 0
		print "The following are the cards they may play: \n" + "\n".join([card.name for card in cards])

		selected_cards = self.curr_turn.cards_selected
		print "\n\nThe following are the cards they have selected: \n" + "\n".join([card.name for card in selected_cards])

	def show_winners(self):
		''' Show the winners in the correct order at the end of the game '''
		print '\n'.join([player.name for player in self.winners])