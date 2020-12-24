# interable
# iterate
# generators


# Using keyword 'yield'
print("Using keyword 'yield'")

def iteratable_fun(num):
	for i in range(num):
		print("Before yield")
		yield i
		print("After yield")

for item in iteratable_fun(4):
	print(f"item print  {item}")


def iterate_for(interable_item):
	iterator = iter(interable_item)
	while True:
		try:
		    print(iterator)
		    print(next(iterator))
		except StopIteration as e:
			print (e)
			break
		else:
			pass

iterate_for([1, 2, 3])



# How a Iterable class works
class My_iterable_class():
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
		raise StopIteration

aClass = My_iterable_class(10)
for i in aClass:
	print(i)
print(f"Wo Wooooooo oooooo  {aClass.current}")

# Compare the time used by differ function

from time import time
def performance(fn):
	def wrapper(*args, **kwargs):
		t1 = time()
		result = fn(*args, **kwargs)
		t2 = time()
		print(f"{fn.__name__} has spent {t2 - t1}s")
		return result

	return wrapper

@performance
def long_timer():
	print('long_timer is running')
	for i in range(40000000):
		i*2


@performance
def long_time2():
	print('long_time2 is running')
	for i in list(range(40000000)):
		i*2

long_timer()
long_time2()
