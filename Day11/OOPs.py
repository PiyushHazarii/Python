class Employee:
    id = 10
    lang = "Hindi"
    salary = 10000
    
obj = Employee()
print(obj.salary)
print(obj.lang)
print(obj.id)



class Employee:
    language = "Py" #this is a class attribute
    salary = 1200000

harry = Employee()
harry.name = "Harry" # this is an object attribute
print(harry.name, harry.language, harry.salary)

rohan = Employee()
rohan.name = "Rohan Roro Robinson"
print(rohan.name, rohan.salary, rohan.language)

# Here name is object attribute and 
# salary and language are class attributes as they directly belong to the class