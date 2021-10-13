# Sets are unordered collections with no duplicate elements

alpha = {'a', 'b', 'c', 'a'}

print(alpha) # no duplicate

# Can't access by index because Sets are unordered
for item in alpha:
	print(item)

# Adding one element into the set
alpha.add('t')

print(alpha)

# Adding multiple elements
alpha.update(['a', 'b', 't', 'i'])

print(alpha)

print(len(alpha))


#Remove the element from the set
alpha.remove('a')
alpha.discard('h') # It's safer to use discard than remove.
# Discard will never throw an error if the element is not preset, remove will
print(alpha)
