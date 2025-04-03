#List & Tuple
#list is mutable but tuple is not mutable 
x = 5
print(x/2) #this will print 2.5
print(x//2) #this will print 2


h1 = [1, 34, 56, 71, 18, 10, 91, 5] 

#slicing operations  syntax = [start:stop:step]
p = h1[2:6:1]
print(p)

#start se end tak jayega
print(h1[5:])

#start se 9 tak jayega with step 2
print(h1[2:9:2])

#python mein negative indexing bhi hota hai 
#to -1 last wala index ko point krta hai 
print(h1[-1])


#this is tuple
t1 = (5, 7, 1, 8, 3, 9)

# t1.sort()  # This will raise an AttributeError as tuples are immutable

t2 = list(t1)
print(t2)

t2.sort()
print(t2)

# ye kitna 0 hai wo count krke de dega 
a = (7, 0, 8, 0, 0, 9)
n = a.count(0)
print(n)