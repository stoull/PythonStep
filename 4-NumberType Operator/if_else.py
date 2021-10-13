a = 5
b = 10

# See for the indentation
if a == 5:
	print('Awesome')

# Indentatins are very important in Python
# Python will throw error if there is no indentation, like:
'''
if a == 5:
print('Awesome')
'''

# and is equivalent &&

if a == 5 and b == 10:
  print("A is five and b is ten")

# multiple conditions
if a == 5:
  print("A is five")
elif a == 6:
  print("A is six")
elif a == 7:
  print("A is seven")
else:
  print("A is some number")

# or is equivalent to ||
if a < 6 or a == 10:
  print('A should be less than 6 or should be equal to ten')

# not is equivalent to !
if not a == b:
  print('a is not equivalent to b')

# Short-hand notation of if statement
if a == 5: print('A is five')

# a=b? "a=b":"a!=b"
print('A is five') if a == 5 else print('A is not five')

