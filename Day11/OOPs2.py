class Employee:
    language = "Python" # This is a class attribute
    salary = 1200000

me = Employee()
me.language = "JavaScript" # This is an instance attribute
# isme baad mein jo language assign kiya wo instance attribute hai 
# aur wo hi print hoga naa ki class attribute wala 
print(me.language, me.salary)