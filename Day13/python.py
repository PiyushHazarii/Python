#MAP, FILTER, & REDUCE IN PYTHON

l = [1, 2, 3, 4, 5]

square = lambda x: x*x

#example of map function
# map pehele ek function leta hai then iterable object leta hai
# and then wo function ko iterable object ke har element pe apply karta hai
# and returns a map object
sqList = map(square, l)
print(list(sqList))


# Filter Example
# ye filter function bhi ek function leta hai and iterable object leta hai
# and wo function ko iterable object ke har element pe apply karta hai
# and returns a filter object
#matlab ye sirf wahi elements ko return karega jo function ke condition ko satisfy karega
def even(n):
    if (n%2 == 0):
        return True
    return False

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # Added a list 'l' to provide input for filter

onlyEven = filter(even, l)
print(list(onlyEven))


from functools import reduce

# Reduce Example
# ye reduce function bhi ek function leta hai and iterable object leta hai

def sum(a, b):
    return a + b
# same as above 
# sum = lamda a, b: a + b
mul = lambda x, y: x * y

l = [1, 2, 3, 4, 5] # Added a list 'l' to provide input for reduce

# ye plus krke return kr dega 
print(reduce(sum, l))

# and ye multiply krke return karega
print(reduce(mul, l))



l = [111, 2, 65, 53, 635, 65, 74, 45, 55]

# sabse bada number return karega ye 
def greater(a, b):
    if a > b:
        return a
    return b

print(reduce(greater, l))