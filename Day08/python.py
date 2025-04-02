#DOUBLE FOR LOOP.........!!!  &&&&& #EVAL Function...

#end is to stop the print statement from going to next line 
for i in range(5):
    print("A",end="")
    for j in range(3):
        print("B",end="")
    print()


#* printing
for i in range(6):
    for j in range(i):
        print("*",end="")
    print()
  
  
#* printing
for i in range(1, 5):
    for j in range(1, 8):
        if j >= 5 - i and j <= 3 + i:
            print("*", end="")
        else:
            print(" ", end="")
    print()
    
    
#eval ek aisa jo data ko dekh kar uska type bata deta hai...
# x = eval(input("Enter a data:"))
# print(x, type(x))

x, y = input("Enter first number:"), input("Enter second number:")
print(x, y)

# another way to do the above
# ye split karke input ko alag alag variable me daal deta hai
# matlab ye input ko space se alag kar deta hai 
m, n = input("Enter numbers:").split(" ");
print(x, y)

x, y, z = input("Enter a date:").split('/')
print(x, y, z)

x = input("tell me about yourself:")
y = x.split() # ye list bana deta hai and data usme rehta hai 
print(y, type(y))

# ye phele 3 numbers ko space se alag karke input lega 
#then wo ek ek number ko int me convert karega with the help of for loop
# for i in range(11,22,33): kuch aisa dikhega niche wala program.
g,h,i = [int(i) for i in input("Enter Three numbers:").split()]
print(g,h,i)


#same as above
g,h,i = [eval(i) for i in input("Enter Three numbers:").split()]
print(g,h,i)

# if you want to take input in a list
l1 = list([eval(i) for i in input("Enter a list:").split()])
print(l1, type(l1))

# if you want to take input in a tuple
l2 = tuple([eval(i) for i in input("Enter a list:").split()])
print(l2, type(l1))



#if you want to take input in a dictionary
# it take input in the form of key-value pairs
# for example: 1-2 3-4 5-6
l3 = dict(input(i).split("-") for i in range(3))
print(l3, type(l3)) 

#har bar ek baar key and ek baar value chalega
#pehele key wala input lega then value wala input lega.
d2 = {input("Enter a key: "): input("Enter a value: ") for x in range(3)}
print(d2)