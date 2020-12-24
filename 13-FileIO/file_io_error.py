try:
	with open('Sad.txt', mode = 'x') as my_file:
		print(my_file.read())
except FileNotFoundError as err:
	print(f"file not found {err}")
except IOError as err:
	print("EO error")
	# raise err
except UnsupportedOperation:
	print("Unsupported Operation")