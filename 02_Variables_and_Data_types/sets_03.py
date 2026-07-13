s1={2,4,6,8}
s2={3,6,9}
print(s1|s2) #union
#s1.union(s2) alternate way
print(s1 & s2) #intersection
#s1.intersection(s2)
print(s1-s2) #{8,2,4} which are present in s1 but not in s2
#s1.difference(s2)
print(s1^s2) #{2,3,4,8,9}symmetric difference, not common elements
#s1.symmetric_difference(s2)
