
"""
range function iterates through a loop containing a start, end, and step
"""
# for i in range(1, 21, 3):
#     print(i)

"""
range function with a len to access its index. Prints its index
"""    
from time import sleep


numbers = [2, 4, 6, 7, 40, 30, True, False, "okay"]

# for i in range(len(numbers)):
#     print(i)

for element in numbers:
    print(element)

"""
loops through items by their index and the element
"""
# for i, element in enumerate(numbers):
#     print(i, element)  

"""
Able to loop through a tuple 
"""
# tup = (1, 2, 3, "Hello", "DM", True)

# # prints the element in my collection by its index
# for i in range(len(tup)):
#     element = tup[i]
#     print(element)

# # or 

# # prints all of the elements 
# for element in tup:
#     print(element)

# # prints the element with its index
# for i, element in enumerate(tup):
#     print(i, element) 

# x = "my string"

# for i in range(0, len(x), 3):
#     print(x[i])

# for element in x:
#     print(element)

# for i, element in enumerate(x):
#     print(i, element)

"""
Break keyword is used to stop a loop
"""
x = [1, 2, 3, 3, 4, 4, 5, 6, 7, 2, 1]

# for num in x: 
#     if num == 6:
#         break 
#     print(num)

# print("Done")    

"""
Continue keyword is used to skip through a certain element and iterates through the rest of the for loop
"""

# for num in x:
#     if num == 7:
#         continue 
#     print(num)

# print("Done")    

"""
Nested for loop
"""
# for i in range(10):
#     for j in range(10):
#         for l in range(2):
#             print(i, j, l)

"""
Looping through a nested list
"""
# lst = [[1, 2], [3, 4], [5, 6], [7, 8]]

# for i in range(len(lst)):
#     inside_lst = lst[i]

#     for j in range(len(inside_lst)):
#         print(inside_lst[j])

"""
Use a for loop to find if a character exist within a string
"""
# st = "Hello World!"

# for i, char in enumerate(st):
#     if char == "W":
#         print(i)

"""
Use a for loop to create a new list
"""

# strings = []

# for i in range(4):
#     words = input("Enter a string: ")
#     strings.append(words)

# print(strings)    

"""
for loop using if, else statement and using break keyword to break out of loop
"""
words = ("hello", "there", "cutie", "pie") 
target = "cu"

for word in words: 
    if word == target:
        print("I found the word!")
        break 
else: 
    print("I did not find the word!")