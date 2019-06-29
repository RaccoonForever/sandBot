"""
Script that will handle the War Field
"""

import logging
from .gameconstants import (
	FIELD_WIDTH,
	FIELD_HEIGHT
)

class Field:
	"""
	Object that will contain everything to describe a war field 
	"""

	def __init__(self):
		"""
		Initialization of the class
		"""
		self.height = FIELD_HEIGHT
		self.width = FIELD_WIDTH
		# Initialization of the field
		self.field = [[0] * self.height for i in range(self.width)]
		logging.info("Instantiating a new field %s x %s", str(self.width), str(self.height))
