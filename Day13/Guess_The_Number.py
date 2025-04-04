import random

n = random.randint(1, 100)
a = -1
guesses = 1

# jab tak a means jo number hum guess kr rahe hai wo 
# equal nahi hota n se tab tak ye loop chalega
# n means jo number computer ne randomly generate kiya hai
while a != n:
    a = int(input("Guess the number: "))
    if a > n:
        print("Lower number please")
    elif a < n:
        print("Higher number please")
    guesses += 1

print(f"You have guessed the number {n} correctly in {guesses} attempts")