#!python

def does_contain(string, pattern):
	assert isinstance(string, str), 'input is not a string: {}'.format(string)

	return does_contain_iterative(string, pattern)
	# return does_contain_recursive(string, pattern)


def does_contain_iterative(string, pattern):
	pass