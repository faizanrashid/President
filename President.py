import Deck
class President(object):
	'''Model of the game'''

	def __init__(self):
		''' Initialize the game '''
		self.deck = Deck.Deck()
		self.players = []
		self.field = []
		self.players_in_round = []
		self.winners = []
		self.curr_turn = None
		self.game_over = False

	def add_player(self, player):
		''' Add a new player to the game '''
		self.players.append(player)

	def has_player_won(self):
		''' The current player may have won if so remove him from the game '''
		player = self.curr_turn
		if not len(self.curr_turn.cards):
			index_round = self.players_in_round.index(self.curr_turn)
			index_player = self.players.index(self.curr_turn)
			self.next_player_move()
			self.players_in_round.pop(index_round)
			self.players.pop(index_player)
		
		return len(player.cards) == 0

	def player_burned(self):
		''' The player burned the field '''
		self.field = []
		self.curr_turn.make_move()
		self.has_player_won()
		self.game_over = self.is_game_over()
		self.players_in_round = self.players[:]


	def player_passed(self):
		''' The player passed remove him from the current round '''
		index = self.players_in_round.index(self.curr_turn)
		self.next_player_move()
		self.players_in_round.pop(index)
		self.round_over()

	def next_player_move(self):
		index = self.players_in_round.index(self.curr_turn)
		if index >= len(self.players_in_round)-1:
			self.curr_turn = self.players_in_round[0]
		else:
			self.curr_turn = self.players_in_round[index+1]

	def round_over(self):
		'''Check if the round is over if so restart it'''
		if len(self.players_in_round) == 1:
			self.field = []
			self.players_in_round = self.players[:]


	def is_game_over(self):
		'''Check if the game is over '''
		return len(self.players) == 1

	def make_move(self):
		self.field = self.curr_turn.cards_selected
		self.curr_turn.make_move()
		if not self.has_player_won():
			self.next_player_move()
		self.game_over = self.is_game_over()

	def distribute_cards(self):
		''' Distribute cards to all the players '''
		while self.deck.size() > 0:
			for player in self.players:
				if (self.deck.size() > 0):
					player.add_card(self.deck.draw_card())
		self.curr_turn = self.players[0]
		self.players_in_round = self.players[:]
	





