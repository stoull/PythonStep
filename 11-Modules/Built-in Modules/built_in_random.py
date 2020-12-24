import random

print(random)

num = random.random()
print(num)

num_int = random.randint(1,10)
print(num_int)

seed_list = [11, 21, 32, 1, 19, 12]
print(f"The original list: {seed_list}")

the_one = random.choice(seed_list)
print(f"Choice one in random: {the_one}")

# shuffle all items in a list
random.shuffle(seed_list)
print("Shuffle all items in the list")
print(seed_list)





