"""
Dictionaries are kept to store key value pairs: key -> value 
Keys can be a collection such as integers, tuple, strings
Allows you to look up values by their keys
Dictionaries are unordered collection of items - therefore, cannot use index
"""
# x = {2: "hello", "1": 5}
# print(x["1"])

"""
Adding values into an empty dictionaries 
"""
# x = {}
# x["key"] = "value"
# print(x)
# # to reference value:
# print(x["key"])

"""
To initialize an empty dictionary, use the dict() function 
"""
# x = dict()
# x["key"] = "value"
# print(x)

"""
Deleting items from a dictionary 
"""
# x = {1:1, 2:2, 3:3}
# # use del keyword 
# del x[1]
# print(x)

"""
To check if a key is in a dictionary, use the contains method
"""
# x = {1:1,  2:2, 3:3}
# # checking to see if a key is in a dictionary by writing the key in the variable name
# contains = 1 in x
# print(contains)

"""
To check the values of a dictionary, use the values() method
"""
# x = {1:1, 2:2, 3:3}
# # Gives you all values inside of a dictionary
# values = x.values()
# print(values)

"""
To check the keys of a dictionary, use the keys() method
"""
# x = {1:1, 2:2, 3:3}
# # Gives the keys inside of a dictionary
# keys = x.keys()
# print(keys)

"""
To get all the items from a list - FYI - will return a tuple if otherwise converted to a list
"""
# x = {1:1, 2:2, 3:3}
# items = x.items()
# print(items)

# # if you want to convert it into a list
# items = list(x.items())
# print(items)

"""
Get the length of a dict by using len() function
The example below is an example of looping through a dictionary
Rule: 
1. Dictionary is an unordered list - therefore, we cannot index through the items
2. Loop through every key of the dictionary
"""

# x = {2: 1, 3: 3}

# for key in x: 
#     value = x[key]
#     print(key, value)

# # or - loops through a tuple containing our key and value - 
# for key, value in x.items(): 
#     print(key, value)    

"""
Using a .get() method - checks to see if the current character exist as a key because we cannot index through a dictionary
"""    
# x = {2: 1, 3: 3}
# X at the key 4, is equal to whatever value is associated with key 4, if it exists. 
# If 4 does not exist, add one to it 
# x[4] = x.get(4, 0) + 1
# print(x)

# Loops through a string to check if a current character exist as a key
# Loops through the string to see how many times a character occurs and adding them up at the end
characters = {}
string = "hello world"
for char in string:
    # characters at char
    characters[char] = characters.get(char, 0) + 1
print(characters)    

# Asking a user to input different values and count how many times they insert all of the values
counts = {}
while True:
    num = input("Number (enter q to quit): ")

    if num == "q":
        break
    # converts the num to an int
    num = int(num)
    counts[num] = counts.get(num, 0) + 1

print (counts)