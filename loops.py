# For loops uses two keywords, if and in, which is used to describe the element and object that is being iterated over 

# nums = [0, 1, 2, 3, 4, 5, 6]

# for num in nums:
#     print(num + 1)


# For loops with range() is used toi execute a block of code multiple times 

# for i in range(4):
#     print(i)

    


# Nested for loops is used when the items that you are iterating contains subitems (list within a list)
#Triple nested loop

# couples = [
#     ["Clarissa", "Daylen"], 
#     ["Victoria", "Brandon"], 
#     ["Donna Mae"]
# ]

# for couple in couples:
#     for name in couple:
#         print("\n")
#         for c in name:
#             print(c)
        

# for i in range(100):
#     if i % 5 == 0 and i % 3 == 0 and i % 4 == 0 and i % 5 == 0:
#         print(i)


# friendsAge = [
#     [12,14], 
#     [13, 24], 
#     [16, 18], 
#     [26]
#     ]

# for friendAge in friendsAge:
#     print()
#     for age in friendAge:
#         print(age, end = '')
#         print(end = ' ')


# # Does the placement of the operator and the print statement matter. I noticed that the result changed. Run code: 
# i = 1 
# while i < 6: 
#     i += 1
#     print(i)
    

# i = 1 
# while i < 6: 
#     print(i)   
#     i += 1 



# couples = [
#     ["Clarissa", "Daylen"], 
#     ["Victoria", "Brandon"], 
#     ["Donna Mae", "Ronan"]
# ]

# for couple in couples:
#     for name in couple:
#         for c in name:
#             print(c)