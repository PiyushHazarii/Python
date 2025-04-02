#FUNCTIONS IN PYTHON...!!!

def fun():
  print("CoDing SeeKho")
  print("Bye")
  print("A")

# pehele ye print hoga then function call hoga 
print("Hello")
fun()

#Addition function
def add(x, y):
  z = x + y
  print("Addition is", z)

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
add(x, y)

#functional argument

def fun1(x, y, z=0):
  print(x + y + z)
  print(z)

fun1(z=11, x=22, y=33)


#this will take the input as a tuple 
def fun10(*p):
  print(p, type(p))

fun10(22, 33, 44, 55, 66, 777, 88, 99)
# fun1(11, 22, w=33, z=44)