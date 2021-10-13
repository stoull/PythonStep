birth_year_str = input("what year were you born?")

print(f"Your input type is: {type(birth_year_str)}")
birth_year = int(birth_year_str)

age = 2020 - birth_year

print(f"Your age is: {age}")
