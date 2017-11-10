#!python

from linkedlist import LinkedList

class LinkedSet(object):
	
	def __init__(self, elements=None):
		self.list = LinkedList()
		self.size = 0

		# If given elements, add them to list
		if elements is not None:
			for element in elements:
				self.add(element)


	'''Returns True if the element exists in the set, otherwise returns False'''
	def contains(self, element):
		found = self.list.find(lambda x: x == element)
		return True if found is not None else False


	'''Used to add an element to the set, if not already present'''
	def add(self, element):
		if element is None or element == '':
			raise ValueError("Cannot add None or '' to Set")

		if self.contains(element):
			raise ValueError("Cannot add {} to set, it already exists".format(element))
		else:
			self.list.append(element)
			self.size += 1