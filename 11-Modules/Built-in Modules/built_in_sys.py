import sys

print(sys)
# print(dir(sys))
# help(sys)

# sys.argv is the param with command line
# like your using command 'python3 ./built_in_sys.py Kevin Chen' in Terminal
# 'Kevin' and 'Chen' will pass to sys.argv

first = sys.argv[0]
second = sys.argv[1]
thrid = sys.argv[2]

# As the example above
print(first) 	# will be the file name
print(second)	# will be Kevin
print(thrid)	# will be Chen
