# lambda expression
# lambda expression is a anonymous function, and only can use once

"""
syntax
lambda param: action(using param)

example
lambda x: x +1 
 the expression is composed of:
 1. The keyword: lambda
 2. A bound variable: x
 3. A body x+1

""" 



lambda_result1 = (lambda x: x + 1)(2)
print(lambda_result1)

# The example above like
lambda_expression1 = lambda x: x + 1
print(lambda_expression1(2))

# Another example
full_name = lambda first, second: f"Full name: {first.title()} {second.title()}"
print(full_name("Kevin", "Chen"))

my_list = [1, 2, 3]

mulip_list = list(map(lambda item: item*2, my_list))

print(mulip_list)



my_movies = ["Portrait of a Lady on Fire", 
			"The Invisible Man", 
			"Never Rarely Sometimes Always",
			"Hamilton",
			"Da 5 Bloods"]

def add_suffix_mp4(item):
	return item + ".mp4"

new_movies = list(map(lambda item: {item + ".mp4"}, my_movies))


print(f"old movies list : {my_movies}")
print(f"new movies list : {new_movies}")

# Exercises 

# List Sorting 
aList = [(0, 2), (3, 4), (9, 9), (10, -2), (7, 4)]
aList.sort(key = lambda x: x[1], reverse = False)

print(aList)


# difference between functions

import dis
def function_add(x, y): return x + y
print(f"Type: {type(function_add)}") 
dis.dis(function_add)

lambda_add = lambda x, y: x + y
print(f"Type: {type(lambda_add)}")
dis.dis(lambda_add)

# There are same


# Applying Decorator to a lambda
def trace(f):
	def wrapper(*args, **kwargs):
		print(f"TRACE func: {f.__name__}, args:{args}, kwargs: {kwargs}")
		result = f(*args, *kwargs)
		return result
	return wrapper

# Applying Decorator to a function
@trace
def kiss(name):
	print(f"{name} is kissing")

kiss("Hen，Cock")

# Applying Decorator to a lambda
trace(lambda x: print(x))("lambda is kissing")












