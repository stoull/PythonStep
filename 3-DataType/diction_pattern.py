dictionary = {
  123: [1, 2, 3],
  True: 'hello',
  'isTrue': True,
  (1, 2): [23, 4, 33]
}

print(dictionary['isTrue'])
print(dictionary[(1, 2)])

for key,value in dictionary.items():
  print(f"key is: {key}, value: is {value}")