#EXCEPTION HANDLING IN PYTHON...!!!!

print("hii")
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

# there is no catch block in python it has try and except block
try:
    z = x / y
    print(z)
    print("bye")
except ZeroDivisionError:
    print("Why you are dividing with 0?")
    

#Another example...   
print("hii")
x = input("Enter first number: ")
y = int(input("Enter second number: "))

try:
    z = x / y
    print(z)
except (ZeroDivisionError, TypeError):
    print("Error")
    

# agar exception ka naam nhi pata hai to to sirf except likh do
# wo khud samajh jayega and catch kar lega    
cb = 10000

while True:
    wb = int(input("Enter amount: "))
    
    try:
        if cb < wb:
            raise ValueError()
        
        cb = cb - wb
        print("Money Sent")
        print("Current Bal is", cb)
    
    except ValueError:
        print("Insufficient Balance.")
        print("Current bal is", cb)
    finally:
        print("ye to chalega hi")
        

#Another example...   
print("hii")
xx = input("Enter first number: ")
yy = int(input("Enter second number: "))

try:
    zz = xx / yy
    print(zz)
except (ZeroDivisionError, TypeError):
    print("Error")
else:
    print("else block") #agar koi exception nahi aata hai to else block chalega
    