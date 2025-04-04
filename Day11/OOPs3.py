class Employee:
    language = "Python" # This is a class attribute
    salary = 1200000
    
    # yaha pr humko hamesha self pass karna padega
    # kyunki ye function class ke andar hai
    # aur ye function class ke andar hi chalega essi liye 
    def func(self):
        print(f"hello function {self.language} {self.salary}")
    
    # agar self pass nhi karenge to error aayega positional argument missing krke 
    def greet(self):
        print("Hello, I am an employee")
        
    # agar humko self pass krna hi nhi to hum @staticmethod use kar sakte hain
    @staticmethod
    def static_method():
        print("Hello, I am a static method")

me = Employee()
me.language = "JavaScript"  
print(me.language, me.salary)

me.func()
#Employee.func(me) # ye bhi chalega
# Employee.func() # ye nahi chalega kyunki isme self nahi hai
me.greet()