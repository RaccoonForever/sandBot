"""
Script that will handle the War Field
"""

import logging
from .map import Map
from ..gamehandler.initializations import initializebotpositions
from .gameconstants import (
	MAP_WIDTH,
	MAP_HEIGHT,
	MAP_COIN_CELL
)

class Field:
	"""
	Object that will contain everything to describe a war field 
	"""

	def __init__(self, *args, **kwargs):
		"""
		Constructor
		"""
		if len(kwargs) != 2:
			self.map = Map(width=MAP_WIDTH, height=MAP_HEIGHT)
		else:
			self.map = Map(width=kwargs['width'], height=kwargs['height'])


	def addbots(self, bots):
		"""
		Function that will handle the adding of bots on the field

		Parameters
		----------
		bots
			Bot list
		"""
		initializebotpositions(bots, self)

	def getmap(self):
		"""
		map getter
		"""
		return self.map

	def getitemdictionnary(self):
		"""
		Function that will return all items in a dictionnary
		"""
		dictionnary = {}
		for x in range(self.map.getwidth()):
			for y in range(self.map.getheight()):
				if self.map.getmap()[x][y] == MAP_COIN_CELL:
					dictionnary['coin' + str(x) + str(y)] = (x, y)

		return dictionnary





