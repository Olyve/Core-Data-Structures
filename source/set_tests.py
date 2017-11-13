#!python

import Set
import unittest

# Throughout tests, 'ts' is used to represent test_set
class SetTest(unittest.TestCase):

	def test_init_no_elements(self):
		ts = Set()
		assert ts.size == 0

if __name__ == '__main__':
    unittest.main()