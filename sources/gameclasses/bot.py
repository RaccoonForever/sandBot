"""
Script that will handle the class Bot
"""

import math
import random
import logging
from ..utils.randomgen import generatebotname
from .move import Move
from .gameconstants import (
	BOT_NAME_LENGTH,
	BOT_STRATEGY_COINS_FIRST,
	BOT_STRATEGY_RUN_RUN,
	MAP_WALL_CELL,
	MAP_EMPTY_CELL,
	MAP_BOT_CELL
)

class Bot:
	"""
	Class that will handle every characteristics and behaviour of a Bot
	"""

	def __init__(self):
		"""
		Class initialization
		"""
		self.botname = generatebotname(BOT_NAME_LENGTH)
		self.x = -1
		self.y = -1
		self.strategy = 1
		self.itemgathered = 0
		logging.info("Creating a new BOT : %s with strategy : %s", self.botname, str(self.strategy))

	def initposition(self, x, y):
		"""
		Initializae the position of the bot

		Parameters
		-----------
		x
			The x coordinate
		y
			The y coordinate
		"""
		self.x = x
		self.y = y

	def nextmove(self, field):
		"""
		Function that will return the next move of the bot
		"""
		if self.strategy == BOT_STRATEGY_COINS_FIRST:
			# Compute closest coins
			max_dist = field.getmap().getwidth() * field.getmap().getheight()
			for itemname, (x, y) in field.getitemdictionnary().items():
				dist = math.sqrt((x - self.x)*(x - self.x) + (y - self.y)*(y - self.y))
				if dist < max_dist:
					max_dist = dist
					name = itemname
					item = field.getitemdictionnary()[itemname]
			print("Choosing closest : ", item)
			print("Bot position ", self.x, self.y)

			# First width movement
			x_item, y_item = item
			nextmove_found = False
			impossiblemove = []
			while not nextmove_found:
				if x_item - self.x > 0 and y_item - self.y == 0 and Move.RIGHT not in impossiblemove:
					next_move = Move.RIGHT
					if (field.getmap().getmap()[self.x+1][self.y] == MAP_WALL_CELL):
						impossiblemove.append(Move.RIGHT)
					else:
						field.getmap().getmap()[self.x][self.y] = MAP_EMPTY_CELL
						nextmove_found = True
						self.x += 1
						field.getmap().getmap()[self.x][self.y] = MAP_BOT_CELL
				elif x_item - self.x > 0 and y_item - self.y > 0 and Move.DOWN_RIGHT not in impossiblemove:
					next_move = Move.DOWN_RIGHT
					if (field.getmap().getmap()[self.x+1][self.y+1] == MAP_WALL_CELL):
						impossiblemove.append(Move.DOWN_RIGHT)
					else:
						field.getmap().getmap()[self.x][self.y] = MAP_EMPTY_CELL
						nextmove_found = True
						self.x += 1
						self.y += 1
						field.getmap().getmap()[self.x][self.y] = MAP_BOT_CELL
				elif x_item  - self.x > 0 and y_item - self.y < 0 and Move.UP_RIGHT not in impossiblemove:
					next_move = Move.UP_RIGHT
					if (field.getmap().getmap()[self.x+1][self.y-1] == MAP_WALL_CELL):
						impossiblemove.append(Move.UP_RIGHT)
					else:
						field.getmap().getmap()[self.x][self.y] = MAP_EMPTY_CELL
						nextmove_found = True
						self.x += 1
						self.y -= 1
						field.getmap().getmap()[self.x][self.y] = MAP_BOT_CELL
				elif x_item - self.x == 0 and y_item - self.y == 0:
					next_move = Move.NOTHING
					nextmove_found = True
				elif x_item - self.x == 0 and y_item - self.y > 0 and Move.DOWN not in impossiblemove:
					next_move = Move.DOWN
					if (field.getmap().getmap()[self.x][self.y+1] == MAP_WALL_CELL):
						impossiblemove.append(Move.DOWN)
					else:
						field.getmap().getmap()[self.x][self.y] = MAP_EMPTY_CELL
						nextmove_found = True
						self.y += 1
						field.getmap().getmap()[self.x][self.y] = MAP_BOT_CELL
				elif x_item - self.x == 0 and y_item - self.y < 0 and Move.UP not in impossiblemove:
					next_move = Move.UP
					if (field.getmap().getmap()[self.x][self.y-1] == MAP_WALL_CELL):
						impossiblemove.append(Move.UP)
					else:
						field.getmap().getmap()[self.x][self.y] = MAP_EMPTY_CELL
						nextmove_found = True
						self.y -= 1
						field.getmap().getmap()[self.x][self.y] = MAP_BOT_CELL
				elif x_item - self.x < 0 and y_item - self.y == 0 and Move.LEFT not in impossiblemove:
					next_move = Move.LEFT
					if (field.getmap().getmap()[self.x-1][self.y] == MAP_WALL_CELL):
						impossiblemove.append(Move.LEFT)
					else:
						field.getmap().getmap()[self.x][self.y] = MAP_EMPTY_CELL
						nextmove_found = True
						self.x -= 1
						field.getmap().getmap()[self.x][self.y] = MAP_BOT_CELL
				elif x_item - self.x < 0 and y_item - self.y > 0 and Move.DOWN_LEFT not in impossiblemove:
					next_move = Move.DOWN_LEFT
					if (field.getmap().getmap()[self.x-1][self.y+1] == MAP_WALL_CELL):
						impossiblemove.append(Move.DOWN_LEFT)
					else:
						field.getmap().getmap()[self.x][self.y] = MAP_EMPTY_CELL
						nextmove_found = True
						self.x -= 1
						self.y += 1
						field.getmap().getmap()[self.x][self.y] = MAP_BOT_CELL
				elif x_item - self.x < 0 and y_item - self.y < 0 and Move.UP_LEFT not in impossiblemove:
					next_move = Move.UP_LEFT
					if (field.getmap().getmap()[self.x-1][self.y-1] == MAP_WALL_CELL):
						impossiblemove.append(Move.UP_LEFT)
					else:
						field.getmap().getmap()[self.x][self.y] = MAP_EMPTY_CELL
						nextmove_found = True
						self.x -= 1
						self.y -= 1
						field.getmap().getmap()[self.x][self.y] = MAP_BOT_CELL


			return next_move

	def increaseitemgathered(self):
		"""
		Function that will increase the number of item gathered by the bot
		""" 
		self.itemgathered += 1

def generatebots(number=10):
	"""
	Function that will generate n new bots

	Parameters
	----------
	number
		The number of bots to generate

	Returns
	---------
		The list of generated bot
	"""
	bots=[]
	for i in range(number):
		bots.append(Bot())

	return bots