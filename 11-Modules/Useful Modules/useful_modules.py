from collections import Counter, defaultdict, OrderedDict


# Counter is counting how many times a character has repeated

li = [12, 12, 31, 2, 3, 4, 4, 7, 23, 32, 31]

print(Counter(li))

a_sentence = "Whether you're new to programming or an experienced developer, it's easy to learn and use Python."

print(Counter(a_sentence))




# defaultdict 
dictionary_normal = {'a' : 23, 'b' : 32}
# dictionary_normal['k']	# Here is KeyError


dictionary_def1 = defaultdict(lambda: 'does not exist', {'a' : 23, 'b' : 32})
print(dictionary_def1['k']) # No error


# OrderedDict, keys and values are ordered like array
d1 = OrderedDict()
d1['a'] = '1'
d1['b'] = '2'

d2 = OrderedDict()
d2['b'] = '2'
d2['a'] = '2'

print(d1 == d2)		# False

d_n_1 = {'a' : '1', 'b' : '2'}
d_n_2 = {'b' : '2', 'a' : '1'}
print(d_n_1 == d_n_2)	# True




