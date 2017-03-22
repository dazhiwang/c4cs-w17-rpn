import unittest
import rpn
import sys
from termcolor import colored, cprint
import logging
logging.basicConfig(level=logging.DEBUG)
class TestBasics(unittest.TestCase):
	def test_add(self):
		logging.info('add test start')
		input_string = '1 1 +'
		#for c in input_string:
		#	if c.isdigit():
		#		print colored(c, 'red')
		#	else:
		#		print colored(c, 'green')
		result = rpn.calculate(input_string)
		self.assertEqual(2, result)
	def test_subtract(self):
		logging.info('subtract test start')
		result = rpn.calculate('5 3 -')
		self.assertEqual(2, result)
	def test_exponentiation(self):
		#logging.info('exponentiation test start')
                result = rpn.calculate('5 3 ^')
                self.assertEqual(125, result)
	#def test_ifloordiv(self):
	#	result = rpn.calculate('5 3 //')
	#	self.assertEqual(1, result)
