numbs = [1,3,4]
numbs.append(4)
print(numbs)
print(len(numbs))
#insert method similar as append function but this help you to add element any position
index = 1
numbs.insert(index, "tomato")
print(numbs)
#index method returns the index of a element
print(numbs.index(3))
numbs = [1,3,4,5,6,6]
print(max(numbs))
print(min(numbs))
print(numbs.count(6))
numbs.remove(3)
print(numbs)
numbs.reverse()
print(numbs)
del numbs
print(numbs)
