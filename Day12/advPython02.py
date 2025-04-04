a = 89

#global kar dene se wo variable har jagah ek hi ho jayega jaise ki
# hum gloabl a niche function mein use kiye hai lekin wo bahar wala a 
# ka bhi value change kar de raha hai..
def fun():
    global a
    a = 3
    print(a)

fun()
print(a)


a = ["Harry", "Rohan", "Shubham"]

# aisa krne se wo join kr dega jo bhi a ke andar hoga with the seperation of ::
# for example: Harry::Rohan::Shubham
final = "::".join(a)
# final = "?".join(a)
print(final)

#this is the way in which we can define the data types of variables 
# this is new in python 3.6.
n: int = 5

name: str = "Harry"

# aisa krne se ye function ka readability badh jayega
def sum(a: int, b: int) -> int:
    return a + b

#this si same as switch case in Java.
def http_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unknown status"

print(http_status(200))