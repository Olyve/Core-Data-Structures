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

	def test_contains_element_exists(self):
		elements = [1, 3, 5, 7, 9, 11]
		ls = LinkedSet(elements)
		assert ls.contains(3) == True

	def test_contains_element_does_not_exist(self):
		elements = [1, 3, 5, 7, 9, 11]
		ls = LinkedSet(elements)
		assert ls.contains('a') == False

	def test_add_inserts_element(self):
		ls = LinkedSet()
		ls.add(3)
		assert ls.contains(3) == True

	def test_add_fails_if_item_already_exists(self):
		ls = LinkedSet([3])
		with self.assertRaises(ValueError):
			ls.add(3)


if __name__ == '__main__':
    unittest.main()