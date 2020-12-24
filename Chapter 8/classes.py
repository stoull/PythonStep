import keyword
is_self_keyword = keyword.iskeyword("self")

print(is_self_keyword)

class Animal():
  def __init__(self, name):
    self.name = name

  def eat(self):
    print(self.name + " eats")

dog = Animal('Hot spot')
dog.eat()

print(dog.name)

dog.name = "Harry"
print(dog.name)


class Person():
  def __init__(my_instance, name):
    # name is protected
    my_instance._name = name

  def reads(my_instance):
    print(my_instance._name + ' reads')

  def writes(my_object):
    print(my_object._name + ' writes')

aChange = Person('AChange')
aChange.writes()
print(aChange._name)

class Vehical():
  def __init__(self, type):
    self.__type = type

  def drive(self):
    print(__type + " vehical is driving")

  def __some_helper_method():
    print("Some helper methods")

class Car(Vehical):
  def __init__(self, name):
    self.__type = 'car'
    self.name = name

  def drive(self):
    print(name + self.__type + " is driving")


a_type_vechial = Vehical('two wheels')
# print(a_type_vechial.type) # 'Vehical' oject has no attribute 'type'

a_car = Car("BWM")
print(a_car.name)
print(a_car.type)



