#list, set, dictionary


my_list1 = [char for char in "hello"]
my_list2 = [num for num in range(0,100)]
my_list3 = [num*2 for num in range(0, 20)]
my_list4 = [num**2 for num in range(0, 20) if num % 2 == 0]


print("    =====list======    ")
print(my_list4)

print("    ===== Using IF ELSE =====")
odd_even_list = ["even" if num % 2 ==0 else "odd" for num in range(0, 10)]
print(odd_even_list)

#like limbda expression
print("===== like using lambda expression =====")
create_new_list = list(map(lambda char: char, "Hello"))
print(create_new_list)

# Set 
my_set1 = {char for char in "hello"}
my_set2 = {num for num in range(0,100)}
my_set3 = {num*2 for num in range(0, 20)}
my_set4 = {num**2 for num in range(0, 20) if num % 2 == 0}

print("    =====set======    ")
print(my_set4)


# Dictionary
simple_dic = {'a' : 1,
			  'b' : 2,
			  'c' : 3,
			  'd' : 4}

multiple2_dic = {k:v*2 for k,v in simple_dic.items() if v % 2 == 0}

print(f"Dictionary example: {multiple2_dic}")


print("Another example of dictionary")
another_dic = {num : num**2 for num in range(2, 16) if num % 2 == 0}
print(another_dic)


