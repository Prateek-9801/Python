#tuples are similar to list, they are ordered and indexed
t=(10,20,"geek")
print(t)
t=() #empty tuple
print(type(t))
print(t)
t=(10)
print(type(t))
t=(10,)
print(type(t))
t=("AntMAn")
print(type(t))
#difference btw list and tuples
#tuples are immutable
#tuples are faster than list
t=10 #if single value then not a tuple
print(type(t))
t=10,20,30,40,10 #this is also a tuple, parenthesis are optional
print(t[2])
print(t[-1])
print(t[-3])
print(t[1:3])
print(len(t))
print(t.count(10))
print(t.index(20))

