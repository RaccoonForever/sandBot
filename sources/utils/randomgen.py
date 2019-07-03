"""
Script that will handle every function relative to random things
"""

import string
import random

def generatebotname(length):
	"""
	Generate a random botname with only upper and lower character

	Parameters
	----------
	length
		The length of the name to generate

	Returns
	---------
		A bot name of length characters
	"""
	result = ""
	for i in range(length):
		result += str(random.choice(string.ascii_letters))
	return result