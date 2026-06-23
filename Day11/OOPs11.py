class Number:
    def __init__(self, n):
        self.n = n 

    def __add__(self, num):
        return self.n + num.n  # Access the 'n' attribute of the 'num' object

n = Number(1)
m = Number(2)

print(n + m)


class Number:
    def __init__(self, n):
        self.n = n

n = Number(1)
m = Number(2)

print(n.n + m.n)


#explanation : Python does not directly add the objects.

# Instead, it translates:

# n + m

# into

# n.__add__(m)

# This is called Operator Overloading.