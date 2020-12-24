# Here is a main file

from Rate.helper import Helper
from ultility import Ultility



class Sunflower():
	def __init__(self, radius):
		self.radius = radius
		super(Sunflower, self).__init__()
		self.arg = arg
		

# Testing computer's performance about caculate Fibonacci Sequence
class Testing():
	def __init__(self):
		pass

	@classmethod
	@Helper.performance
	def total_fib(number):
		total = 0
		for n in Ultility.fibonacci(number):
			total += n
		return total

helper = Helper()
print(type(helper))

test1 = Testing()
print(type(test1))

if __name__ == "__main__":
	print(f"The result is: {test1.total_fib(21)}")





