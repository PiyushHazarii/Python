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

# this is dictionary 
d1 = dict(one="Amit", two="Ajay", three="atul", four="ashish")
print(d1)

#ye items de dega sara dictionary ka 
marks = {
    "Harry": 100,
    "Shubham": 56,
    "Rohan": 23,
    0: "Harry"
}

print(marks.items())
print(marks.keys)
print(marks.values)

marks.update({"Harry":32})
print(marks.get("Rohan"))

print(marks.get("Rohanwe")) # ye none print karega koi bhhi error nhi dega 
print(marks["husdfjsd"]) # ye error dega none wagera kuch bhi print nhi karega


#Empty set aise banta hai 
e = set()  # Don't use s = {} as it will create an empty dictionary

#dono rahega set mein kyuki ek string hai aur ek integer.
s = set()
s.add(18)
s.add("18")
print(s)

#in keyword list mein bhi chalta hai 
# uska kaam ye hai wo jo in ke baad likha gaya hai wo in se pehele wale 
# variable mein present hai ki nhi wo check krte hai aur true aur false mein
# return krta hai value..
l = ["Harry", "Rohan", "Shubham", "Divya"]

name = input("Enter your name: ")

if name in l:
    print("Your name is in the list")
else:
    print("Your name is not in the list")