#INHERITANCE IN PYTHON.

class One:
    company = "ITC"
    def show(self):
        print(f"The name of the Company is {self.company}")
#this is the way to inherit the class in python
class Two():
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"The name is {self.company} of the company")

class Three(One,Two):
    def multipleInheritance(self):
        print(f"This is multiole inheritance")
        
b = Three()

b.show()
b.showLanguage()
b.multipleInheritance()
