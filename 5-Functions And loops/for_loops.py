arr = ['apple', 'banana', 'cake', 'dot', 'egg']
for ele in arr:
  print (ele)

print(" === new for loop === ")
word = "Python"
for char in word:
  print(char)

print(" === new for loop === ")

for ele in range(1, 8, 2):
  print(ele)

print(" === new for loop === ")
for ele in range(0, len(arr)):
  print(arr[ele])

print(" === new for loop === ")
dict = {"name" : "John wick", "age" : "34"}

for key, value in dict.items():
  print(key + "is: " + value)

print(" === new for loop === ")
#Use a built-in function enumerate()
for index, value in enumerate(arr):
  print(value + "is present in " + str(index))


