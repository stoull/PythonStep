basket = ['a', 'x', 'b', 'c', 'd', 'e', 'd']
basket.sort()
basket.reverse()
print(basket[::-1]) # This will copy the list
print(f"basket is : {basket}")

print("Create a large list")
print(list(range(2, 100)))

print("Using method of join()")


sentence = ''
new_sentence = sentence.join(['hi ', 'my ', 'name ', 'is ', 'Lamp'])

print(new_sentence)


annotation = " === list unpacking === "
print(annotation)
a,b,c, *other, d = [1,2,3,4,5,6,7,8]
print(a); print(b); print(c); print(other); print(d)

annotation = " === Using None === "
print(annotation)
weapons = None
print(weapons)
