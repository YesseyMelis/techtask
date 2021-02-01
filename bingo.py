import random
import time
from typing import List


class Player:
	def __init__(self, name):
		self.name = name
		self.ticket = []
		self.found = []
		self.won = False
		for i in range(5):
			self.ticket.append(random.randint(1, 99))

	def check(self, number):
		if number in self.ticket:
			self.found.append(number)
			if sorted(self.found) == sorted(self.ticket):
				print('{} BINGO!!!'.format(self.name))
				self.won = True


class Program:
	def __init__(self):
		self.winning_set = []
		self.players: List[Player] = []
		self.have_winner = False
		print('Welcome to the bingo game')
	
	def attach(self, player: Player):
		self.players.append(player)
	
	def detach(self, player: Player):
		self.players.remove(player)

	def show_number(self):
		for player in self.players:
			player.check(number=self.winning_set[len(self.winning_set) - 1])
			if player.won:
				self.have_winner = True
				break

	def start(self):
		numbers = list(range(1, 99))
		random.shuffle(numbers)
		for number in numbers:
			if not self.have_winner:
				self.winning_set.append(number)
				print("We got number: ", number)
				self.show_number()
				time.sleep(0.5)
			else:
				break


if __name__ == "__main__":
	bingo = Program()

	player1 = Player(name="AZAMAT")
	bingo.attach(player1)
	player2 = Player(name="BEKZAT")
	bingo.attach(player2)
	player3 = Player(name="SANJAR")
	bingo.attach(player3)
	player4 = Player(name="DAULET")
	bingo.attach(player4)
	player5 = Player(name="GULNUR")
	bingo.attach(player5)

	bingo.start()

