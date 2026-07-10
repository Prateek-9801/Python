#type() in python
#data types are present in python too as other languages
#but we need not write data-type to create object
a=10
print(type(a))
b=10.5
print(type(b))
c=2+4j
print(type(c))
#above are the examples of numeric values in python
#below are the examples of None and bool
a=True
print(type(a))
b=None
print(type(b))
#Example program for sequence types given below
#sequence is collection of multiple smaller items
#string is a collention of multiple character items
str="gfg"
print(type(str)) #String
l=[10,20,30]
print(type(l)) #List: These are mmutable, ordered
t=(10,20,30)
print(type(t)) #Tuple: These are immutable, can't modify
s={10,20,30}
print(type(s)) #Set: All the items are distinct, no order
d={10:"gfg", 20:"ide"}
print(type(d)) #Dict: Dictionary are used to store mappings, stores key value pairs
