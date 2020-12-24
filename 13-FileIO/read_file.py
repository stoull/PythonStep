
test_file = open('Test.txt')

print("File read object:")
print(test_file)

print("Read file first time")
print(test_file.read())			# The point will move to the end of file
print("Read file second time")
test_file.seek(0)		# move the point back to the head of file
print(test_file.read())
print("Read file third time")
print(test_file.read())  # nothing will print here


test_file.seek(0)
print(test_file.readline())	# read file line by line
print(test_file.readline())

print(" ======== readlines =======")
test_file.seek(0)
file_list = test_file.readlines()
print(file_list)
print(" ======= end =========")

test_file.close()		# close the file

# The standard way to open a file
# Do not need seek with as handle file opening and closing
print(" ======== open file with as First  =======")
with open('Test.txt') as file_object:
	print(file_object.read())
print(" ======= end =========")

print(" ======== open file with as Second  =======")
with open('Test.txt') as file_object:
	print(file_object.readlines())
print(" ======= end =========")








