#!python

from hashtable import HashTable

class Set(object):

	def __init__(self, elements=None):
		self.ht = HashTable()
		self.size = 0

		if elements is not None:
			for element in elements:
				self.add(element)

	"""Return a boolean indicating whether the underlying hashtable includes the element provided."""
	def contains(self, element):
		return self.ht.contains(element)

	"""Add the provided element to the Set, but only if it does not already contain the value."""
	def add(self, element):
		if self.ht.contains(element) == False:
			self.ht.set(element, 'junk')
			self.size += 1

	"""Delete the element from the set if it exists, otherwise raise KeyError."""
	def delete(self, element):
		self.ht.delete(element)
		self.size -= 1

	"""Return a new set that contains the elements of this set and other_set."""
	def union(self, other_set):
		new_set = Set()
		# Add items from this set
		for item in self.ht.items():
			new_set.add(item)
		# Add other_set items
		for item in other_set.ht.items():
			new_set.add(item)
		# Return the new set
		return new_set

	"""Return a new set that contains the intersection of this set and other_set. 
	Basically a new set containing only the elements that are found in both sets."""
	def intersection(self, other_set):
		new_set = Set()
		for item in self.ht.items():
			if other_set.contains(item):
				new_set.add(item)


if __name__ == '__main__':
	pass