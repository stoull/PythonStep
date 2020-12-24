# Here is Utitlity
from Rate.helper import Helper

#Generate a normal Sequence
class Ultility():
	def even_sequence(number):
		return list(n*2 for n in range(number))

	def odd_sequence(number):
		return list((n*2 -1 ) for n in range(1, number + 1))


	# Generate a Fibonacci Sequence
	def fibonacci(num):
		a = 0
		b = 1
		for i in range(num):
			yield a
			temp = a
			a = b
			b = b + temp

ulti = Ultility()
help = Helper()

if __name__ == '__main__':
	print(type(ulti))
	print(type(help))
