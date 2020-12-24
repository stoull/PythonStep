numbers = ["one", "two", "three"]

print(numbers[0])

print(numbers[::-1])

print(len(numbers))

del numbers[0] # will delete the value in the appropiate position

popped_element = numbers.pop() # Pop willl help you to remove the last element

print(numbers)

print(popped_element)

alpha = ["z", "c", "a"]
alpha.sort();  print(alpha)
alpha.sort(reverse = True); print(alpha)

import keyword
print(keyword.iskeyword("reverse"))

print(alpha[::-1])

print("=== copy whole list, not a reference ===")
amozon_shopping_list = ["notbooks", "foods", "mouse", "toys"]
shopping_list = amozon_shopping_list

shopping_list[0] = "laptop"
print(amozon_shopping_list)

another_list = shopping_list[:]
shopping_list[0] = "apples"

print(another_list)
print(shopping_list)

