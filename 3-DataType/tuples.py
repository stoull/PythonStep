# Tuples are just like lists but the are immutable.

nums = (1, 2, 3)
print(nums)

print(len(nums)); print(nums[0])

empty_tuple = () # is a empty tuple

new_tuple = (1, ) # Note the trailing comma.

print(type(new_tuple))
print(new_tuple)

new_tuple = (1)
print(type(new_tuple)) # <type 'init'> It won't return a tuple. Because there is no trailing comma

# Createing a new tuple from the existing tuple
numbers = (1, 2, 3)
char = ('a', )
new_tuple = nums + char
print(new_tuple)
