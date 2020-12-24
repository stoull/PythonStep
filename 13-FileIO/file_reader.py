
# About file path, read more information with module 'pathlib'

with open('pi_digits.txt') as file_object:
  contents = file_object.read()
print(contents.rstrip())
print("======= End ========")

annotation = "read file with file path"
print(annotation)
with open('/Users/kevin/Desktop/hutspace/python_space/13-FileIO/test_files/pi_digits.txt') as file_object:
  contents = file_object.read()
print(contents.rstrip())
print("======= End ========")


annotation = "read file line by line"
print(annotation)
filePath = './pi_digits.txt'
with open(filePath) as file_object:
  for line in file_object:
    print('++++++++++++++++++++ line by line')
    print(line.rstrip())

annotation = "Making a list of Lines from a file"
print(annotation)
with open(filePath) as file_object:
  lines = file_object.readlines()
pi_string = ""
for line in lines:
  pi_string += line.rstrip()

print(pi_string)
print("The length of pi is: " + str(len(pi_string)))

annotation = "Is Your Birthday Contained in Pi?"
print(annotation)
file_name = "pi_million_digits.txt"
with open(file_name) as file_object:
  lines = file_object.readlines()
pi_string = ""
for line in lines:
  pi_string += line.rstrip()

print("Check if you birthday is appear in the first million digits of Pi")
birthday = input("Enter your birthday, in the format yymmdd: ")
if birthday in pi_string:
  print("Your birthday appears in the first million digits of pi")
else:
  print("Your birthday does not appear in the first million digits of pi")


