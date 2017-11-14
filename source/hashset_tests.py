#!python

from hashset import Set
import unittest

# Throughout tests, 'ts' is used to represent test_set
class SetTest(unittest.TestCase):

	def test_init_no_elements(self):
		ts = Set()
		assert ts.size == 0

	def test_init_with_elements(self):
		data = ['A', 'B', 'C']
		ts = Set(data)
		assert ts.size == 3

	def test_add(self):
		ts = Set()
		ts.add('A')
		assert ts.size == 1
		ts.add('A')
		assert ts.size == 1
		ts.add('B')
		assert ts.size == 2

	def test_contains(self):
		ts = Set()
		ts.add('A')
		ts.add('B')
		ts.add('C')
		assert ts.contains('A') == True
		assert ts.contains('B') == True
		assert ts.contains('C') == True
		assert ts.contains('D') == False

	def test_delete(self):
		ts = Set(['A', 'B', 'C'])
		assert ts.size == 3
		ts.delete('A')
		assert ts.contains('A') == False
		assert ts.size == 2
		ts.delete('B')
		assert ts.contains('B') == False
		assert ts.size == 1
		with self.assertRaises(KeyError):
			ts.delete('Z')
		assert ts.size == 1

	def test_union(self):
		set_a = Set(['A', 'B', 'C'])
		set_b = Set(['C', 'D', 'E'])
		set_c = set_a.union(set_b)
		assert set_c.size == 5
		assert set_c.contains('A') == True
		assert set_c.contains('B') == True
		assert set_c.contains('C') == True
		assert set_c.contains('D') == True
		assert set_c.contains('E') == True
		assert set_c.contains('g') == False

	def test_intersection(self):
		pass

if __name__ == '__main__':
    unittest.main()