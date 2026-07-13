#Program to demostrate removal of item
s={10,30,20,40}
s.discard(30) #if the item is present in the set it is removed but if the item is not present it not going to do anything
print(s)
s.remove(20) #if the item is present in the set it is removed else raise an error that's the difference between discard and remove
print(s)
s.clear() # set() #everything will be removed from the set and will give an empty set
print(s)
s.add(50)
print(s)
del s #the whole object is revomed which means empty set will also be removed

