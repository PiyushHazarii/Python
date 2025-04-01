#set and dictionary..

s1 = {11, 22, 33, 44, 55, 66, 11, 22, 11, 55}
print(s1)

s2 = {55, 66, 77, 88}
print(s2)

#ye union kr dega 
s1.update(s2)
print(s1)


s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6}

print(s1.union(s2))
print(s1)

s3 = s1.union(s2)
print(s3)

print(s1.intersection(s2))

s1.discard(11)  # No error if 11 is not in s1
# s1.remove(11)  # This will raise a KeyError because 11 is not in s1

d1 = {1, 2, 3, 4, 5, 6}
d2 = {2, 3, 4}

print(d1.issubset(d2))
print(d2.issubset(d1))
print(d1.issuperset(d2))

k1 = {}
print(type(k1))

t1 = 55,
print(t1)

k1 = set()
print(type(k1))