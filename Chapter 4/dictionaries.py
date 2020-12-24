user = {'id': 1, 'name': 'John wick', 'email': 'john@gmail.com'}

print(user['id'])
print(user['name'])

print(f"The lenth of the dictioinary of user {len(user)}")

user['age'] = 35

keys = user.keys() # This will reture a list
print(keys); print(f"The lenth of Keys is: {len(keys)}")


# to delete a key
del user['age']; print(user)

# Example of nested dict
user = {
	'id': 1,
	'name': 'John wick',
	'cars': ['audi', 'bmw', 'tesla'],
	'projects':[
	 {
		'id': 10,
		'name': 'Project 1'		
 	 },
	 {
		'id': 11,
		'name': 'Project 2'
	 }
	]
}

print(f"user dictionary {user}")
