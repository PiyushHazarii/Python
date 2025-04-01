# IF & ELSE & ITERATIVE STATEMENTS

x= 5;
#this is the to write if else in python...
if x>3:
    print("Yes It is greater than 3")
else:
    print("No It is not greater than 3")
# there is no else if in python we have to use elif...
#Iterative Statements

#ye har baar ek character lega and print karwa dega.
a = "Piyush"
for i in a:
    print(i)

# ye utna baar print karwayega jitna character hai a mein.
for i in a:
    print("Hello");
    
# isme ye 0 se lekar 19 tak print karega. ek kaam print krta hai ye 
for i in range(20):
    print(i);
    
#ye start karega 2 se aur 4 tak chalega
for i in range(2,5):
    print(i);
    
#range function mien 3 value daal skte hai start, stop, step
#isme ye start hoga 2 se jayega 10 se 1 kam tak and 3 plus hote rahega 
for i in range(2,10,3):
    print(i);
    
    

#this is while-else loop    
p = 1234
c = 0

while c != 3:
    c = c + 1
    pin = input("Enter a pin: ")
    if pin == str(p):  # Convert p to string for comparison
        print("Transaction Successful")
        break
    else:
        print("Incorrect Pin")

else:  # This 'else' block is associated with the 'while' loop
    print("Card Blocked")