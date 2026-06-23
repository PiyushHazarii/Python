class Employee:
    a = 1

    @classmethod #ek tarika hai class ke andar hum method ko jab declare karte hai to kuch bhi update karenge 
    #to wo class ke andar hi update hoga aur object ke andar nahi hoga jaise ki hum emp.a = 3 kiye to wo class ke andar hi update hoga
    #iss object ke andar nhi hoga...
    def show(cls):
        print("This is a class method")
        print(cls.a) # this will access only class attributes
    
    @property
    def name(self):
        return self.ename

    @name.setter
    def name(self, value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]



    
emp = Employee()
emp.a=3
# ye krne ke baad bhi ye class attribute ko hi access karega
# kyunki ye class method hai
# ye instance method ko access nahi karega

#emp.name ("Harry khan") 
emp.name =  "Harry khan"  # Use the setter to set the name
print(emp.fname,emp.lname)  # Use the getter to get the name

emp.show()

