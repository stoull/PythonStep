# Decorator 
# Using a wrap function to add extra functions to a function
def my_decorator(fun):
	def wrap_fun():
		print(f"==== Function: {fun.__name__}")
		fun()
	return wrap_fun

@my_decorator
def say_hi():
	print(f"Hello everyone, nice to be here!")
say_hi()

@my_decorator
def generator_even_odd():
	result_list = ["even" if num % 2 == 0 else "odd" for num in range(10)]
	print(result_list)

generator_even_odd()


# Decorator Pattern
def new_decorator(fun):
	def wrap_fun(*args, **kwargs):
		print(f"==== Function: {fun.__name__}")
		fun(*args, **kwargs)
	return wrap_fun

@new_decorator
def say_something(words, emoji = ":)"):
	print(words, emoji)

say_something("A bomb is coming!!!!!!")


# Another example
from time import time
def performance(fn):
	def wrapper(*args, **kwargs):
		t1 = time()
		result = fn(*args, **kwargs)
		t2 = time()
		print(f"This function took: {t2 - t1}s")
		return result
	return wrapper

@performance
@new_decorator
def caculate():
	for i in range(10000):
		i*5

caculate()






