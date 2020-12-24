my_movies = ["Portrait of a Lady on Fire", 
			"The Invisible Man", 
			"Never Rarely Sometimes Always",
			"Hamilton",
			"Da 5 Bloods"]

def add_suffix_mp4(item):
	return item + ".mp4"

it = map(add_suffix_mp4, my_movies)

print(next(it))
print(next(it))

# convert a iterator to a list
print(list(it))


print("\n\n\n  ==============")
print("Example of using map with a dictionary")

def remove_suffix(item):
	start_index = item.find(".mp4")
	print(item[0:start_index])


	

star_movies = ["Portrait of a Lady on Fire.mp4", 
			"The Invisible Man.mp4", 
			"Never Rarely Sometimes Always.mp4",
			"Hamilton.mp4",
			"Da 5 Bloods.mp4"]

print(f"All movies: {star_movies}")

movies_without_suffix = list(map(remove_suffix, star_movies))
print(movies_without_suffix)




