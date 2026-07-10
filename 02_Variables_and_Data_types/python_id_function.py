print(id(5))
a=10
print(id(a))
b=10
print(id(b))
x=10
y=10
print(id(x))
print(id(y)) #address of a, b, x, y reamains same beacause of same literal i.e. 10
c="Prateek"
d="Prateek"
print(id(c)) #address of c and d remains same because same string literals
print(id(d)) 
# is operator
i=12
j=12
print(i is j)
k=i
print(k is j)
k=20
print(k is j)
