
def print_hello_world():
  print("Hello world")

print_hello_world()


# Return statement
def hello_something(something):
  return "Hello " + something

hi = hello_something("Python")
print(hi)


def say_hi_to_world(hi_words = "Hello"):
  return hi_words + " World"

hi_world = say_hi_to_world("Hei, your")
print(hi_world)


def movie_info(title, director_name, ratings):
  print(title + " - " + director_name + " -  " + ratings)

movie_info(ratings = '8.8', title = 'Big fish', director_name = "Li An")

def languages(*names):
  print(names)
  return 'You are mentioned ' + str(len(names)) + ' languages'

print(languages('Python', 'Swift', 'JavaScript', 'Object-C'))


# Two paramaters
def in_my_favorite_movie(fav_movie, *movies):
  print(movies)
  print("You are mentioned " + str(len(movies)) + ". And you favorite movie is: " + fav_movie)

in_my_favorite_movie("Qie Fu", "Seven Ken", "Big Fish", "Xing JI")

def person_info(id, name, **info):
  print("Name is " + name + " And id is " + id)
  print(info)

person_info(info = {"name" : "Andy", "id" : "22", "descrption" : "This person has no functin"}, id = "22", name = "Andy")
  





