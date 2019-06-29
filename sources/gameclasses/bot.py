"""
Script that will handle the class Bot
"""

import logging
from ..utils.randomgen import generatebotname
from .gameconstants import BOT_NAME_LENGTH

class Bot:
	"""
	Class that will handle every characteristics and behaviour of a Bot
	"""

	def __init__(self):
		"""
		Class initialization
		"""
		self.botname = generatebotname(BOT_NAME_LENGTH)
		logging.info("Creating a new BOT : %s ", self.botname)

