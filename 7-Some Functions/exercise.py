from functools import reduce

#1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']
def capitalize(pet):
	return pet.upper()

cap_my_pets = list(map(capitalize, my_pets))
print(cap_my_pets)

capitalize_pets_list = []
for pet in my_pets:
	capitalize_pets_list.append(pet.upper())
print(capitalize_pets_list)


#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]

# my_numbers.sort(reverse = False)
# print(my_numbers)
ziped_list = list(zip(my_strings, my_numbers))
def takeSecond(elem):
	return elem[1]
ziped_list.sort(key = takeSecond, reverse = False)
print(ziped_list)


#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]
def over_50_percent(item):
	return item >= 50

filtered_scores = list(filter(over_50_percent, scores))
print(sorted(filtered_scores))


#4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
def accaculate(acc, item):
	return acc + item

scores_total = reduce(accaculate, scores, 0)
total = reduce(accaculate, my_numbers, scores_total)
print(total)




