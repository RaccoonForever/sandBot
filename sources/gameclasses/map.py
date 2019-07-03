"""
Script that will handle Map class
"""

import logging
from .gameconstants import (
	MAP_WIDTH,
	MAP_HEIGHT,
	MAP_WALL_CELL,
	MAP_EMPTY_CELL,
	MAP_COIN_CELL
)

class Map:
	"""
	Class that will handle everything for a map
	"""

	def __init__(self, *args, **kwargs):
		"""
		Initialization of the class
		"""
		if len(kwargs) != 2:
			self.height = MAP_HEIGHT
			self.width = MAP_WIDTH
		else:
			self.height = kwargs['height']
			self.width = kwargs['width']

		# Initialization of the map
		self.map = [[MAP_WALL_CELL] * self.height for i in range(self.width)]
		logging.info("Instantiating a new map %s x %s", str(self.width), str(self.height))


	def generatemaps(number, width, height):
		"""
		Function that will return a certain number of new maps

		Parameters
		----------
		number
			The number of maps to generate
		width
			The width of each map
		height
			The height of each map

		Returns
		---------
			The list of map generated
		"""
		result = []
		for i in range(number):
			result.append(Map(width=width, height=height))

		return result

	def removeitem(self, x, y):
		"""
		Function that will remove an item from a cell and put it to empty cell
		"""
		self.map[x][y] = MAP_EMPTY_CELL

	def getmap(self):
		"""
		Map getter
		"""
		return self.map

	def getwidth(self):
		"""
		width getter
		"""
		return self.width

	def getheight(self):
		"""
		height getter
		"""
		return self.height

	def itemremaining(self):
		"""
		Function that will give the number of item remaining on the map
		"""
		result = 0
		for x in range(self.width):
			for y in range(self.height):
				if self.map[x][y] == MAP_COIN_CELL:
					result += 1

		return result