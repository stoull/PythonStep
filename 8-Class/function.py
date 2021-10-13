def printme( str ):
	print(str)
	return
printme("I'm first call user defined function")
printme("Again second call to same function")

def changeme( mylist ):
	mylist.append([1, 2, 3, 4])
	print(f"Get value in the function: {mylist}")
	return

mylist = [10, 20, 30]
changeme( mylist)
print(f"Get value out of the function: {mylist}")


def count():
	fs = []
	for i in range(1, 4):
		print(f"out {i}")
		def f():
			print(f"now {i}")
			return i*i
		fs.append(f)
	print(f"lenth of fs: {len(fs)}")
	return fs
f1, f2, f3 = count()

print(f1())

print(f"lenth of list: {len(f1)}")

