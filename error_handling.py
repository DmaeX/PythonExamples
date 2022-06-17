# Try and Except Clauses 
# Try attempts to execute a block of code
# Except executes another block of code if try fails


# nums = [12, 3, 14, 60, 125]

# try:
#     print(sum(nums))
# except: 
#     print("This function will not execute!")


# nums = [12, 3, 14, 60, 125, "x"]

# try:
#     print(sum(nums))
# except: 
#     print("This function will not execute!")



# Finally Clause
# Finally clause executes a block of code regardless of which clause, try or except, was executed. The finally clause is useful in cases where both of your try and except might fail.
# Finally is always executed regardless if ttry or except did. 

# nums = [12, 3, 14, 60, 125, "x"]

# try:
#     print(sum(nums))
# except: 
#     print("This function will not execute!")
# finally:
#     print("Hope this helps!")



friendsAges = [20, 21, 22, 23, 25, 18]

try: 
        avg = (sum(friendsAges)) * (len(friendsAges))
        print (f"This is the average of your friend's ages: {avg}")
except:
        print("There is something wrong with your variable's values. Unable to execute.")
finally: 
        print("I hope that you figured this simple math out. :)")

if avg == 774:
    print(avg)
else: 
    print("You're shit out of luck.")


