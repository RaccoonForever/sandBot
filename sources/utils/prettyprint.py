"""
Script that will contain everything to pretty print bots, field ...
"""

from os import system
from ..gameclasses.gameconstants import (
	MAP_BOT_CELL,
	MAP_EMPTY_CELL,
	MAP_WALL_CELL,
	MAP_COIN_CELL
)

def printfield(field):
	"""
	Print the field to see where are each bots

	Parameters
	----------
	field
		The field
	"""
	#clear()
	result = ""
	for y in range(field.getmap().getheight()):
		for x in range(field.getmap().getwidth()):
			if field.getmap().getmap()[x][y] == MAP_EMPTY_CELL:
				result += "."
			elif field.getmap().getmap()[x][y] == MAP_WALL_CELL:
				result += "W"
			elif field.getmap().getmap()[x][y] == MAP_BOT_CELL:
				result += "B"
			elif field.getmap().getmap()[x][y] == MAP_COIN_CELL:
				result += "c"
		result += "\n"
	print(result)

def clear():
	"""
	Clear command screen
	"""
	_ = system('cls')
