#!python

from set import LinkedSet
import unittest

class SetTest(unittest.TestCase):
	
	def test_init_no_elements(self):
		ls = LinkedSet()
		assert ls.size == 0

	def test_init_with_elements(self):
		elements = [1, 3, 5, 7, 9, 11]
		ls = LinkedSet(elements)
		assert ls.size == 6


if __name__ == '__main__':
    unittest.main()