# # "And" logical operator for conditions - only evaluates to true if both sides equate to true 

# x = 2
# y = 4

# compound = x < y and y < x + 3 and True

# print(compound)

# # "Or" logical operator for conditions - anything that evaluates to true will return true. If they all evaluate to false, then it will return a false 

# x = 2
# y = 4

# compound = x > y or False or True

# print(compound)

# # "Not" logical operator for conditions - negates or swaps whatever the value or the condition is
# # returns the opposite of the evaluated condition 
# # All operators takes precedence over the not operator 

# x = 2
# y = 4

# # compound = not (x > y)

# # or 

# # This returns a syntax error because == operator is evaluated before the not operator 
# # compound = True == not False

# # This will compile because Python knows to evaluate the expression in parenthesis 
# compound = True == (not False)

# print(compound)


# compound = True or False and not True or False 
# print(compound)
"""
Order of precedence: 

1. Conditional/Comparison operators
2. Not 
3. And 
4. Or  
"""

"""
DeMorgan's Law: 
Take a "Not" that's being applied to a parenthesized expression and apply it inside of the parenthesis
"""
x = 2
y = 3

not (x and y) == (not x) or (not y)
not (x or y)  == (not x) and (not y)

not (x and y or (not x))
(not(x and y)) and (not(not x))
(not x) or (not y) and x

"""
Truth Table - the different possible combinations a variable could have
2^3
X Y Z
-----
T T F
F T T
T F T
F T F
T F T
F T F
T F T
F T F
"""