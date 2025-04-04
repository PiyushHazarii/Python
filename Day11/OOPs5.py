class Demo:
    a = 4

o = Demo()
print(o.a)
o.a = 0
print(o.a)
#class attribute ko change nahi kar sakte hum
print(Demo.a)