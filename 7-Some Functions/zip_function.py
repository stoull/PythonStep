# Using function of 'zip'
usernames = ["Andy", 
			"Lucas", 
			"Kath", 
			"Lina", 
			"Linda", 
			"Kevin"]

phonenumbers = ["18923542376", 
				"18923542376", 
				"18923542376", 
				"18923542376", 
				"18923542376", 
				"18923542376"]

emails = ["andy@gamil.com", 
		"lucas@gamil.com", 
		"kath@gamil.com"]

# the lenght is equal to the lenth of the minimine list 
ziped_list = list(zip(usernames, phonenumbers, emails))

print(ziped_list)
