#FILE HANDLING ...!!!

# har bar jab hum write karenge to wo har baar new data enter karega 
# uske pehle jo data hoga wo delete ho jayega

#append jaha se khatam hoga wahi se data add karega

#x mode har bar new file chaiye isko data rakhne ke liye 
# agar hum new file pehele se nhi banate to wo error dega 

a = "a very long string with emails"

emails = []


f = open("Day10/hiscore.txt", "r") # Open the file in read mode
data = f.read() # Read the entire file content
print(data) # Print the content of the file
f.close()



# Assuming 'file.txt' exists in the same directory as the script

f = open("file.txt", "r")

# print(lines, type(lines))  # Commented out as per the image
line1 = f.readline()
print(line1, type(line1))


# Read the first line.
#jab tak line khatam nahi hoti tab tak wo read karega
line = f.readline()
while line != "":
    print(line)
    line = f.readline()

f.close()

# Farenheit to Celsius code 
def f_to_c(f):
  return 5 * (f - 32) / 9

f = int(input("Enter temperature in F: "))
print(f_to_c(f))



#INCH TO CM code 
def inch_to_cms(inch):
  return inch * 2.54

n = int(input("Enter value in inches: "))

print(f"The corresponding value in cms is {inch_to_cms(n)}")





#Game in python in which it random generates a score and checks if it is greater than the hiscore
# and if it is greater than the hiscore then it will write the new hiscore to the file
# and if it is not greater than the hiscore then it will not write anything to the file
# and it will just print the score
import random

def game():
    print("You are playing the game..")
    score = random.randint(1, 62)

    # Fetch hiscorethe hiscore
    #r se wo only read karega 
    with open("Day10/hiscore.txt", "r") as f:
        hiscore = f.read()
        if hiscore != "":
            hiscore = int(hiscore)
        else:
            hiscore = 0

    print(f"Your score: {score}")

    if score > hiscore:
        # Write this hiscore to the file
        # w se wo write karega kya write karega niche likha hua hai wo....
        with open("Day10/hiscore.txt", "w") as f:
            f.write(str(score))

    return score

game()
