#FILE HANDLING ...!!!

# har bar jab hum write karenge to wo har baar new data enter karega 
# uske pehle jo data hoga wo delete ho jayega

#append jaha se khatam hoga wahi se data add karega

#x mode har bar new file chaiye isko data rakhne ke liye 
# agar hum new file pehele se nhi banate to wo error dega 

import random

def game():
    print("You are playing the game..")
    score = random.randint(1, 62)

    # Fetch hiscorethe hiscore
    with open("Day10/hiscore.txt", "r") as f:
        hiscore = f.read()
        if hiscore != "":
            hiscore = int(hiscore)
        else:
            hiscore = 0

    print(f"Your score: {score}")

    if score > hiscore:
        # Write this hiscore to the file
        with open("Day10/hiscore.txt", "w") as f:
            f.write(str(score))

    return score

game()