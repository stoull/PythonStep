

def square(n):
	print(n ** 3)

print(square(7))

print(str.__doc__)
print(sorted.__doc__)

def pow(n, p):
	"""
	param n: This is any integer number
	param p: This is power over n
	return: n to the power p = n^p
	"""
	return n **p

print(pow(3, 6))
print(pow.__doc__)


class BeanMilk(object):
	"""docstring fos BeanMilk"""
	color = "White"
	def __init__(self, amount):
		self.amount = amount
		