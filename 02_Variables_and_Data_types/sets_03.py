#operations on two sets
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
#more operations on two sets
s3={2,4,6,8}
s4={4,8}
print(s3.isdisjoint(s4)) # if no common element = True
print(s3<=s4) # s3.issubset(s4) s3 is subset of s4 or not
print(s3<s4) # proper subset 
print(s3>=s4) # s3.issuperset(s4) 
print(s3>s4) # proper superset
