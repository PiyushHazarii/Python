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