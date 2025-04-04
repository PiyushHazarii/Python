# LAMDA FUNCTION IN PYTHON 

square = lambda x: x*x
print(square(6)) # returns 36

sum = lambda a,b,c: a+b+c
print(sum(1,2,3)) # returns 6

# WITHOUT NAME hota hai lamda function
r = lambda a, b: a + b
p = r(6, 7)
print("Sum is", p)


#factorial using lambda function
r = lambda n:{
    1 if n == 1 else n * r(n - 1)
}
x = int(input("Enter number: "))
p = r(x)
print("Factorial is", p)

