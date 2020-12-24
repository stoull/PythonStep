# Using try and except

"""
try:
	age = int(input("Please enter your age:"))
	print(f"Your age is: {age}")
except:
	print("Please input a number to present your age!")
"""


# while True
while True:
	try:
		age = int(input("Please enter you age:"))
		10/age
		print(f"Your age is: {age}")
	except ValueError:
		print('Please enter a number!')
	except ZeroDivisionError:
		print("Your age can not be zero!")
	else:
		print("Thank You!")
		break
	finally:
		print("=======================")
		pass


# Get error information
def sum(num1, num2):
	try:
		return num1/num2
	except (TypeError, ZeroDivisionError) as error:
		print(error)
	else:
		print("Do nothing with errors")

print(sum('a', 0)) 

# Raise a error

def sum_with_error_raise():
	try:
		print("A error will raise immediate")
		raise ZeroDivisionError("Here is a zero division error")
		raise ValueError("Here is cut out")		# Can raise differ types of error
		raise Exception("Here is a exception")  # again differ type of error
	except (ValueError, ZeroDivisionError) as error:
		print(f"Here is except with error infor: {error}")
	else:
		print("Here is else")

sum_with_error_raise()

