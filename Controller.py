import Player

class Controller(object):
	''' The controller object to manipulate the model'''

	def __init__(self, game):
		'''initialize the controller '''
		self.game = game



	def register_player(self):
		''' register player '''
		player_name = raw_input("Enter a player name or press enter to stop adding more players: ")
		if player_name.isalnum():
			player = Player.Player(player_name)
			self.game.add_player(player)
		return not player_name.isalnum()

	def distribute_cards(self):
		''' Distribute cards initially '''
		self.game.distribute_cards()

	def make_move(self):
		''' Using the cards selected check to see if the move is possible, if so make it '''
		player = self.game.curr_turn
		cards = player.cards_selected
		
		valid = self.valid_move()
		if valid == "burn":
			self.game.player_burned()

		elif not self.valid_move():

			print "Invalid Card Selections"
			player.unselect_all()
		else:
			self.game.make_move()

	def valid_move(self):
		player_cards = self.game.curr_turn.cards_selected
		field = self.game.field
		card_num = player_cards[0].num
		
	
		#Check if all cards are the same number
		for card in player_cards:
			if card.num != card_num:
				return False

		if len(field) == 0:
			return True

		field_card_num = field[0].num
		if field_card_num > card_num:
			return False

		if field_card_num == card_num and len(field) == len(player_cards):
			return "burn"

		if card_num == 15: # It's a 2
			return (len(field) == len(player_cards) or len(field) == len(player_cards)+1)
				
		if card_num == 16 and field_card_num < 15:
			#joker played but field is less than 2
			return (len(field) == len(player_cards) or len(field) <= len(player_cards) + 2)

		if card_num == 16 and field_card_num == 15:
			#Joker played but field is 2
			return (len(field) == len(player_cards) or len(field) == len(player_cards) + 1)

		return card_num > field_card_num and len(field) == len(player_cards)
			


	def ask_move(self):
		''' ask for a move and then return it'''
		print "enter 'pass' to pass your turn or 'unselect' to unselect all cards or "
		card_name = raw_input("Enter the name of the card you want to select or press Enter to stop selecting: ")
		card_name = card_name.lower()
		player = self.game.curr_turn
		cards_name = [card.name.lower() for card in player.cards]
		field = self.game.field
		if card_name == "unselect":
			self.game.curr_turn.unselect_all()

		elif (card_name == "" and len(player.cards_selected) != 0) or (card_name == "pass" and len(field) != 0):
			return card_name

		elif card_name in cards_name:
			index = cards_name.index(card_name)
			card = player.cards[index]
			player.select(card)
		else:
			print "INVALID CARD SELECTION"

		return False

	def make_move_pass(self):
		''' The player passed '''

		self.game.curr_turn.unselect_all()
		self.game.player_passed()