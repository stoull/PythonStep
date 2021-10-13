is_magician = False
is_expert = True

if is_magician and is_expert:
  print("You are a master magician")
elif is_magician and not is_expert:
  print("At least you're getting there")
elif not is_magician:
  print("You need magic powers")
else:
  print("You are nothing!")

print("Do magic") if is_magician else print("You need magic powers")


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sum = 0.0
for item in my_list:
  sum += item
print(str(my_list) + " sum is: " + str(sum))

