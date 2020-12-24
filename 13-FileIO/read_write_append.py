
# will crash if the files doesn't exist
with open('Test2.txt', mode = 'r+') as my_file: 	# 'r+' meas read then write
	my_file.write("Here is my test file")

# will crash with 'r+' if the files doesn't exist
with open('Test2.txt', mode = 'r+') as my_file: 	# 'r+' meas read and write
	my_file.write("Do you mean this")	#This will overwirte file's content

with open('Test2.txt', mode = 'a') as my_file:	# a means append mode
	my_file.write(':)')

# write mode will delete all old content 
with open('Test2.txt', mode = 'w') as my_file:	# 'w' means wirte as a new file
	my_file.write('======')

# in mode 'w', will create a new file if it doesn't exist
with open("Sad.txt", mode = 'w') as my_file:
	my_file.write(":(")

with open('Test2.txt', mode = 'r') as my_file:
	print(my_file.read())