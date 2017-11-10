#!python

from key_value import KeyValue
import unittest

class KeyValueTest(unittest.TestCase):

	def test_init_with_values(self):
		kv = KeyValue('key', 'value')
		assert kv.key == 'key'
		assert kv.value == 'value'


if __name__ == '__main__':
    unittest.main()