class Employee:
    language = "Python" # This is a class attribute
    salary = 1200000
    
    # this is also called a constructor
    
    def __init__(self):
        print("dunder or constructor method called") # this is dunder method which is automatically called when object is created
        
        
emp = Employee()

class Employee:
    language = "Python" # This is a class attribute
    salary = 1200000
    
    # this is also called a constructor
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        print("parameterised constructor or  dunder method called") # this is dunder method which is automatically called when object is created
emp = Employee("John", 1200000)
