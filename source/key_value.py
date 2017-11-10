#!python

class KeyValue(object):
	"""A class to represent a key value pair. Helpful when working with
	HashTables and Trees that need to be generic."""
	def __init__(self, key, value):
		super(KeyValue, self).__init__()

		self.key = key
		self.value = value

	def __str__(self):
		return 'Key: {}, Value: {}'.format(self.key, self.value)

	def __repr__(self):
		return 'KeyValue(key: {}, value: {})'.format(self.key, self.value)


if __name__ == '__main__':
	kv = KeyValue('a', 1)
	print(kv)