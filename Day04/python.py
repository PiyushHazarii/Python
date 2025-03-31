x = int(input("Enter first number:"))
y = int(input("Enter second number:"))

print("x=", x, "y=", y, sep="")

temp = x
x = y
y = temp

print("After Swapping.")
print("x=", x, "y=", y, sep="")