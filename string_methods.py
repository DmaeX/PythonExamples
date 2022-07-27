"""
.count() method counts how many times this element appears in a string  
"""
# s = "hello"
# word = s.count("l")
# print(word)

"""
.find() method gives the index of a character 
"""
# s = "hello"
# word = s.find("l")
# print(word)

"""
.upper() and .lower() method turns the string into all lower or all upper case
"""
# s = "hello"
# word = s.lower()
# print(word)

# m = "hello"
# word = m.upper()
# print(word)

# or 

# name = input("Enter a name: ")

# if name.lower() == "tim":
#     print("Correct")
# else:
#     print("Incorrect")    

"""
.capitalize() method capitalizes the first letter of the string
"""
# s = "donna"
# name = s.capitalize()
# print(name)

"""
contains method returns a bool if the string contains a specific element
"""

# s = "this is my home"
# contains = "s" in s
# print(contains)

"""
isdigit() method returns a bool if the element is a digit
"""
# s = "19"
# is_digit = s.isdigit()
# print(is_digit)

#or 

# num = input("Enter a number: ")

# if num.isdigit():
#     print("This is a number.")
#     num = int(num)
#     print(num + 5)
# else: 
#     print("This is not a number.")

"""
.split() method splits a string to different delimiters i.e (',', '|', '/', etc.)
# sentence = "Hello,there,my,name,,,is,tim"
"""
# words = sentence.split("Hello")
# print(words)

"""
.replace() method replaces a character with another given character 
"""
# sentence = "Hello,my,name,is,DM"

# s1 = sentence.replace(",", "|")
# print(s1)

"""
printing multiple strings 
"""
# name = input("Enter your name: ")
      
# print(name * 5)

"""
Multi-line string 
"""
# name = input("Enter a name: ")

# string = """ this is a 
# multi-line string 
# example
# """
# print(string)

"""
Escaping a character 
"""
# name = input("Enter your name: ")
# string = f'{name}\'s'
# print(string)

"""
.join() method combines the strings together
Good for building a collection of strings into one whole string.
"""

# name = "t", "i", "m"

# new_name = "".join(name)
# print(new_name)