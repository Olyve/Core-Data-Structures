#!python

from linkedlist import LinkedList

class LinkedSet(object):
	
	def __init__(self, elements=None):
		self.list = LinkedList()
		self.size = 0

		# If given elements, add them to list
		if elements is not None:
			for element in elements:
				self.list.append(element)
