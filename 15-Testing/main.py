
def do_stuff(num = 0):
	try:
		if num:
			return int(num) + 5
		else:
			return "Please input a number"
	except ValueError as err:
		print("here is a ValueError")
		return err
	except TypeError as err:
		print("Type error here")
		return err