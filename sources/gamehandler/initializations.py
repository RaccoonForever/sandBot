"""
Script that will contain all initialization methods for the game
"""

import random
import logging
from ..gameclasses.bot import generatebots
from ..gameclasses import field
from ..gameclasses.gameconstants import (
	MAP_WALL_CELL,
	MAP_EMPTY_CELL,
	MAP_BOT_CELL,
	MAP_COIN_CELL
)

def initializebots(number):
	"""
	Function that will return all bots initialized

	Parameters
	----------
	number
		the number of bots to initialize

	Returns
	--------
		The list of initialized bots
	"""
	return generatebots(number)

def initializefield(number, width, height):
	"""
	Function that will return a list of initialized field

	Parameters
	----------
	number
		The number of fields to generate
	width
		The width of the field
	height
		The height of the field

	Returns
	---------
		The initialized field
	"""
	result = []
	for i in range(number):
		tempfield = field.Field(width=width, height=height)
		result.append(tempfield)
	return result


def initializemaze(field, percentage):
	"""
	Put some walls on the map

	Parameters
	-----------
	field
		The field
	percentage
		The percentage of walls to remove (from 0 to 100)
	"""
	x = field.getmap().getwidth()
	y = field.getmap().getheight()
	originalmap = field.getmap().getmap()

	nbcellstoremove = (x * y) * percentage/100

	while nbcellstoremove > 0: 
		x_remove = random.randint(0, field.getmap().getwidth() - 1)
		y_remove = random.randint(0, field.getmap().getheight() - 1)
		if originalmap[x_remove][y_remove] == MAP_WALL_CELL:
			originalmap[x_remove][y_remove] = MAP_EMPTY_CELL
			nbcellstoremove -= 1

	logging.info("Maze generated")

def initializefielditems(field, percentage):
	"""
	Initialize items on the field

	Parameters
	-----------
	field
		The field
	percentage
		The percentage of items to add over all cells
	"""
	number = field.getmap().getwidth() * field.getmap().getwidth() * percentage / 100
	print(number)

	while number > 0:
		x_add = random.randint(0, field.getmap().getwidth() - 1)
		y_add = random.randint(0, field.getmap().getheight() - 1)
		if field.getmap().getmap()[x_add][y_add] == MAP_EMPTY_CELL:
			field.getmap().getmap()[x_add][y_add] = MAP_COIN_CELL
			number -= 1

	logging.info("Adding items")

def initializebotpositions(bots, field):
	"""
	Function that will initialize bot positions on the field

	Parameters
	-----------
	bots
		Bot list
	field
		The war field

	Returns
	--------
		The field with initialized bots position
	"""

	# Loop over each bot
	for bot in bots:
		foundpositionavailable = False
		while not foundpositionavailable:
			x = random.randint(0, field.getmap().getwidth() - 1)
			y = random.randint(0, field.getmap().getheight() - 1)
			if field.getmap().getmap()[x][y] == MAP_EMPTY_CELL:
				bot.initposition(x, y)
				field.getmap().getmap()[x][y] = MAP_BOT_CELL
				foundpositionavailable = True
	logging.info("Bots position initialized")


def logginginit(level):
	"""
	Initialization of logging

	Parameters
	----------
	level
		The minimum logging level we want
	"""
	logger = logging.getLogger()
	logger.setLevel(level)

