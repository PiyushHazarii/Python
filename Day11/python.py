#Recursion in Python 

# The above code will run infinitely and will give a RecursionError:
# maximum recursion depth exceeded in comparison
# def fun():
#     print("Hello World")
#     fun()
# fun()


# ye pura shuru se print kar dega n-1 tak ka factorail
def fun(n):
    if n==1 or n==0:
        return 1
    return n * fun(n-1) 
for i in range(6):
    print(fun(i))
    
    
#fabonacci series 
def fab(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fab(n-1) + fab(n-2)
for i in range(10):
    print(fab(i))
    
