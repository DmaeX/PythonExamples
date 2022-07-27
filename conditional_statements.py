# # If, elif, else 

# # If statements 
# testScore = 90

# if testScore >= 80:
#     print("You are able to graduate!")


# # Else statements 
# testScore = 90

# if testScore >= 100:
#     print("You are able to graduate!")

# else:
#      print("You are not able to graduate!")     


# Elif statements are added between an if and else statement to evaluate for another condition 
# testScore = 80

# if testScore >= 100:
#     print("You are able to graduate!")
# elif testScore > 75:
#     print("You are able to graduate! Find a passion.")
# else
#      print("You are not able to graduate")    

# x = 9
# y = 4

# cond = x >= 9

# print(cond)

# Comparing strings 

# str1 = "b"
# str2 = "a"

# cond = str1 == str2

# print(cond)

      
# Returns a unicode code from a given character 
# value1 = ord("a")
# value2 = ord("A")

# result = value2 + value1

# print(result)



# Chr function takes the ordinal value and give you the character associated with it 
# value1 = chr(65)

# print(value1)

# # or 

# print(chr(68))

# Comparing strings 
# value1 = "ABc"
# value2 = "ABC"

# cond = (value1 < value2) 

# print(cond)


# Comparing strings continuation 
import json
from re import X


# cond = True == 1

# # or 

# cond1 = False == 0 

# print(cond)
# print(cond1)


# cond = "hello" 

# print(cond)

# print(ord("hello"))

# number1 = float(input("Enter a number: "))

# if number1 >= 10 and number1 <= 20:
#     number2 = float(input("Enter a second number: "))
#     sum = number1 + number2

#     print("The sum of these two numbers is: ", sum)

#     if sum > 100:
#         print("This is a large sum!")


person = {
    'name': "DM",
    'age': 26,
    'hates_ronan': True,
    'metadata': {
        'key_1': 'test',
        'number': 5
    }
}

print(json.dumps(person['metadata']))