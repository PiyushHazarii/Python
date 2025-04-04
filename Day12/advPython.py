myList = [1, 2, 9, 5, 3, 5]

# squaredList = []
# for item in myList:
#     squaredList.append(item*item)

#this is the new way of writing the above code 
squaredList = [i*i for i in myList]

print(squaredList)




l = [3, 513, 53, 535]

# index = 0
# for item in l:
#     print(f"The item number at index {index} is {item}")
#     index += 1

#NEW WAY
# This can be simplified using enumerate function
#List comprehension.
for index, item in enumerate(l):
    print(f"The item number at index {index} is {item}")
    
    
from typing import List, Tuple, Dict, Union

# List of integers
numbers: List[int] = [1, 2, 3, 4, 5]

# Tuple of a string and an integer
person: Tuple[str, int] = ("Alice", 30)

# Dictionary with string keys and integer values
scores: Dict[str, int] = {"Alice": 90, "Bob": 85}
 
# Union type for variables that can hold multiple types
identifier: Union[int, str] = "ID123"
identifier = 12345  # Also valid 

# union type for variable explaination 
#here it takes different types of variable like int, float and string
def process(value: Union[int, float, str]):
    if isinstance(value, int):
        print("Integer:", value)
    elif isinstance(value, float):
        print("Float:", value)
    else:
        print("String:", value)
print(process(10))


#ADVANCE DICTIONARY METHODS
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

# ye math ka union kr dega means jo dono mein rahega usko ek barr hi print karega
merged = dict1 | dict2
print(merged)  # Output: {'a': 1, 'b': 3, 'c': 4}

# You can now use multiple context managers in a single with statement more cleanly
# using the parenthesised context manager

with (
    open('file1.txt', 'r') as f1,
    open('file2.txt', 'r') as f2
):
    # Process files
    content1 = f1.read()
    content2 = f2.read()
    print("Content of file1.txt:\n", content1)
    print("Content of file2.txt:\n", content2)