import Deck
import Player

class President(object):
	
	def __init__(self):
		self.players = register_players()
		self.initialize_game()
		self.cur_turn = 0
		self.field = None

	def register_players(self):
		list_players = []
	 	player_name = raw_input("Enter the name of a player" + str(len(list_players)+1))
		while (player_name.isalpha()):
			player = Player(player_name)
			list_players.append(player)
			player_name = raw_input("Enter the name of a player" + str(len(list_players)+1))

	def num_players(self):
		return len(self.players)

	def initialize_game(self):
		deck = Deck()
		while (deck.size()):
			for player in self.players():
				player.add_card(deck.draw_card())

	def next_move(self):
		if self.cur_turn == len(self.players)-1:
			self.cur_turn = 0
			return self.players[0]

		self.cur_turn += 1
		return self.players[self.cur_turn]


