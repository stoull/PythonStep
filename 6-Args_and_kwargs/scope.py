
a = 1
def parent():
  a = 10
  def confusion():
    return a
  return confusion()

print(parent())
print(a)

#1 - start with local
#2 - parent local
#3 - Global

annotation = "1 - Start with local \n2 - looking for parent\n3 - Global"
print(annotation)


print("Example of using Global function")
step = 0
def move_forward(move_step):
  global step
  step += move_step
  return step

move_forward(2)
move_forward(4)

print(step)



