# Using function of filter
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 22, 46, 87]

def only_odd(item):
	return item % 2 != 0

new_list = list(filter(only_odd, my_list))

print(new_list)

# New example for using filter to choose membership

class User():
	def __init__(self, name, isMembership = False):
		self.name = name
		self.isMembership = isMembership

def only_membership(user):
	return user.isMembership

def get_username(user):
	return user.name

andy = User("Andy", True)
lucas = User("Lucas", True)
kath = User("Kath")
lina = User("Lina", True)
kevin = User("Kevin")
		
user_list = [andy, lucas, kath, lina, kevin]
user_name_list = map(get_username, user_list)

filted_list = list(filter(only_membership, user_list))

print("    All user list      ")
print(list(user_name_list))
print("    Only memeber ship   ")
print(list(map(get_username, filted_list)))


