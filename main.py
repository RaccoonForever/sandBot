"""
Script that will launch the game
"""

from sources.gameclasses.bot import Bot
from sources.gameclasses.field import Field
import logging

def main():
	"""
	Main function
	"""
	logginginit(logging.INFO)

	# Randomly create a bot
	acg = Bot()

	# Create a war field
	field = Field()

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

if __name__ == "__main__":
	main()