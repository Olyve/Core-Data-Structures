#!python

from hashtable import HashTable

class Set(object):

	def __init__(self, elements=None):
		self.ht = HashTable()
		self.size = 0

		if elements is not None:
			for element in elements:
				self.add(element)


if __name__ == '__main__':
	pass