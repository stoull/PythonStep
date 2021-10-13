
def super_func(*args):
  print(*args)
  return sum(args)

five_sum = super_func(1, 2, 3, 4, 5)
print(five_sum)

# correct_function_definition.py
def my_function(a, b, *args, **kwargs):
    pass

print("=== Example of using *args and **kwargs === ")
def power_func(*args, **kwargs):
  print(f"args is {args}")
  print(f"kwargs is {kwargs}")
  total = 0
  for item in kwargs.values():
    total += item
  return sum(args) + total

six_sum = power_func(1, 2, 3, 4, 5, last=10)
print(six_sum)


#Rule: params, *args, default parameters, **kwargs
rule = "Rule: params, *args, default parameters, kwargs"
print(rule)
def god_function(name, *args, i="hi", **kwargs):
  print(f"The name is: {name}")
  print(f"args is {args}")
  print(f"i is {i}")
  print(f"kwars is {kwargs}")
  total = 0
  for item in kwargs.values():
    total += item
  return sum(args) + total

god_sum = god_function('Kevin', 1, 2, 3, 4, 5, 6, num1=5, num2=10)
print(god_sum)




