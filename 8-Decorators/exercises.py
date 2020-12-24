# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    'valid': True #changing this will either run or not run the message_friends function.
}

kevin = {
    'name': 'Kevin',
    'valid': False #changing this will either run or not run the message_friends function.
}

def authenticated(fn):
  def wrapper(*args, **kwargs):
  	user = args[0]
  	if user["valid"]:
  		fn(*args, **kwargs)
  	else:
  		print(f"Hi {user['name']}, you are invalid to send message")
  return wrapper

@authenticated
def message_friends(user):
    print(f'Hi {user["name"]}, your message has been sent')

message_friends(user1)
message_friends(kevin)