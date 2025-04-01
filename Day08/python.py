#DOUBLE FOR LOOP.........!!!

#end is to stop the print statement from going to next line 
for i in range(5):
    print("A",end="")
    for j in range(3):
        print("B",end="")
    print()


#* printing
for i in range(6):
    for j in range(i):
        print("*",end="")
    print()
  
  
#* printing
for i in range(1, 5):
    for j in range(1, 8):
        if j >= 5 - i and j <= 3 + i:
            print("*", end="")
        else:
            print(" ", end="")
    print()