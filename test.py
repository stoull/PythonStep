

class My_iterate_class():

	def __init__(self, last):
		self.last = last
		self.current = 0

	def __iter__(self):
		return self

	def __next__(self):
		if self.current < self.last:
			num = self.current
			self.current += 1
			return num
		else:
			self.current = 0
			raise StopIteration

aclass = My_iterate_class(2)

for i in aclass:
	print(i)

from time import time
def performance(fn):
	def wrapper(*args, **kwargs):
		t1 = time()
		result = fn(*args, **kwargs)
		t2 = time()
		print(f"{fn.__name__} has taken {t2 - t1}s")
		return result
	return wrapper

@performance
def iterator_a_large_number():
	print("iterator_a_large_number is runing")
	for i in list(range(9999999)):
		i*2

iterator_a_large_number()





