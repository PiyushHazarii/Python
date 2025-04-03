#BASICS OF PYTHON

#this input function is used to get the input from the user
x = input();
print("The input is :-"+x)

#another way to do this 
y=input("Enter the value of y: ");

#input fuction jab koi data leta hai na to wo string type ka data leta hai 
# agar humko usko plus krke print karana hai to pehele usko humko 
# typecast karna padega
x=int(x) #like this 


s = 10;
print(id(s)) #this will give the address of the variable s;

#python will not create new address for 10 it will refer d to the same address.
d = 10;
print(id(s))


n=5
v=5
print(n==v); #ye values ko compare karega
print(n is y) #ye address ko compare karega ki same hai ki nahi 

#String functions in python 

name = "piyush"

print(len(name))
print(name.endswith("sh"))
print(name.startswith("pi"))
print(name.capitalize()) # ye sirf pehla letter ko capital karega

#this is a new way to print variable in double string 
name = input("Enter Your Name :")
print(f"Good Morning {name}")

#you have to replave name and date in this string 
letter = '''Dear <|Name|>,
You are selected!
<|Date|>'''

# ye pehele string ko piyush se replace kr dega then
# uss string ko date se replace karega then print karega 
print(letter.replace("<|Name|>", "Piyush").replace("<|Date|>", "24 September 2050"))