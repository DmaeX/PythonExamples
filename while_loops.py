# num = input("Enter a number: ")

# while not num.isdigit():
#     num = input("Enter a number: ")

"""
To prevent having to declare the same variable, use a bool
"""    
# while True:
#     num = input("Enter a number: ")
#     if num.isdigit():
#         break 

"""
Break out of the while loop as soon as the sum of all the numbers is greater than 9 
"""
# list of numbers
lst = [2, 3, 4, 5, 1, 3, 1]

# a variable that stores the sum of our list
result = 0

# keeping track of our current index
i = 0

while result < 9:
    num = lst[i]
    # increment result 
    result += num
    # increment i
    i += 1
    print(num)
