"""
Script that will launch the game
"""

import logging
from sources.gameclasses.bot import Bot
from sources.gameclasses.field import Field
import sources.gamehandler.initializations as init
import sources.utils.prettyprint as pp
from sources.gamehandler.roundhandler import Roundhandler

def main():
	"""
	Main function
	"""
	init.logginginit(logging.INFO)

	# Randomly create bots
	botlist = init.initializebots(1)

	# Create a war field
	fields = init.initializefield(number=1, width=25, height=25)
	init.initializemaze(fields[0], 90)
	init.initializefielditems(fields[0], 3)

	# Initialize bot positions
	init.initializebotpositions(botlist, fields[0])

	roundhandler = Roundhandler(field=fields[0], bots=botlist)

	roundhandler.run()


if __name__ == "__main__":
	main()