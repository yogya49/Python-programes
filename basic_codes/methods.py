#using append method to add an element at a specific index
catoons=['doremon','dora and bujji','tom and jerry','kiki and pooh','luna ']
print(catoons)
print("after appending::::::::::::::::::::::")
catoons.append('puss in boots')
print(catoons)
#adding an element at a specific index
catoons.insert(0,'cheshire cat')
print("after inserting at index 0::::::::::::::::::::::")
print(catoons)
#pop method to remove the last element
#if we give index it will pop the elment at that index
catoons.pop()
print("after popping the last element::::::::::::::::::::::")
print(catoons)
catoons.remove('cheshire cat')
print("after removing cheshire cat::::::::::::::::::::::")
print(catoons)
catoons.reverse()
print(catoons)
