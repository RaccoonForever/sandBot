"""
Script qui va gérer le déroulement des rounds du jeux
"""

import logging
import time
from ..gameclasses.gameconstants import (
	MAP_BOT_CELL,
	MAP_COIN_CELL
)
from ..utils.prettyprint import printfield

class Roundhandler:
	"""
	Classe qui va gérer le déroulement des rounds de jeux
	"""

	def __init__(self, *args, **kwargs):
		"""
		Constructor
		"""
		if len(kwargs) != 2:
			raise Exception("Mauvais nombre d'argument pour la classe Roundhandler")
		else:
			self.field = kwargs['field']
			self.bots = kwargs['bots']

	def run(self):
		"""
		Function that will run the game and execute actions

		End condition : no more coin on the map or 20 rounds without gathering coin
		"""

		end = False
		roundwithoutmodif = 0
		itemsremaining = self.field.getmap().itemremaining()
		logging.info("Starting run with %s items", str(itemsremaining))
		while not end:
			for bot in self.bots:
				nextmove = bot.nextmove(self.field)
				logging.info("Next move for : %s is %s", bot.botname, str(nextmove))
			self.computeitemgathered()

			printfield(self.field)
			new_items_number = self.field.getmap().itemremaining()
			logging.info("New items number %s ", str(new_items_number))
			if (itemsremaining != new_items_number):
				itemsremaining = new_items_number
				roundwithoutmodif = 0
			else:
				roundwithoutmodif += 1

			logging.info("roundwithoutmodif : %s", str(roundwithoutmodif))
			if (itemsremaining == 0 or roundwithoutmodif > 18):
				end = True

			time.sleep(2)


	def computeitemgathered(self):
		"""
		Function that will handle if bots walked on coins
		"""
		for bot in self.bots:
			if self.field.getmap().getmap()[bot.x][bot.y] == MAP_COIN_CELL:
				bot.increaseitemgathered()
				self.field.getmap().removeitem(bot.x, bot.y)


