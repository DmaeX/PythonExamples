"""
Sets are an ordered collection of unique elements
Sets are unique collection of elements, meaning no elements can be duplicated 
Cannot use mutable objects inside of a set. Can only add immutable objects inside of it
    - No adding lists, dictionaries, or sets
"""

"""
Use set() function to create an empty set
If you want to designate values to a set, you can use the {} curly brackets syntax with values inside
"""
# x = set()
# # or 
# y = {1, 2}
# print(type(x))
# print(type(y))

# if you have multiple elements of the same value, then all of the duplicate elements are going to be removed. 
# With sets, we do not care about the frequency or the index of an element, we only care if it exists. 
x = {1, 2, 2, 3, 4, 4, 5, 6}
print(x)

"""
Use the .add or .remove function to add and remove elements from a set
"""
y = {1, 2, 2, 3, 5, 6, 7, 7}
y.add(4)
y.remove(7)
print(y)

"""
Use the clear() function to clear a set
"""
a = {1, 2, 2, 3, 5, 6, 7, 7}
a.clear()
print(a)

"""
Use the len() function to check the length of a set
"""
b = {"a", "d", "c", "e", True, 3, (1, 2)}
print(len(b))

"""
Use contains operator if you want to check if something exists in a set
"""
c = {"hello(", "world", "abd", 0.3, False, (3, 4)}
contains = (3, 4) in c
print(contains)

"""
Use .union() function to combine two sets in one
"""
d = {1, 2}
e = {3, 4, 5, 6, 7}
f = d.union(e)
print(f)

# or use the pipe operator | (only used in sets)

g = {8, 9, 10, 11}
h = {12, 13, 14, 15, 16, 17}
i = g | h
print(i)
print(g)
print(h)

"""
Use the .intersection() method to check the items contained in both sets 
"""
j = {"hello", "there", 4, 5, 6, 0.235464, True, (1, 2, 3)}
h = {"4", False, 2, 4, 0, "hello"}
i = j.intersection(h)
print(i)

# shortcut for intersection is the & syntax 

k = j & h
print(k)

"""
Use the .difference() method to check the difference between the set values of two sets 
"""
l = j.difference(h)
print(l)

m = h.difference(j)
print(m)

# shortcut for difference is the - syntax 

n = j - h
print(n)

"""
Use the symmetric_difference() method to check the items given in the present sets, except for the ones in the intersection - checking difference
"""
o = {"hello", "there", 4, 5, 6, 0.235464, True, (1, 2, 3)}
p = {"4", False, 2, 4, 0, "hello"}

q = p.symmetric_difference(o)
print(q)

# shortcut for symmetric difference is the ^ syntax

r = p ^ o
print(r)

"""
Use the .update() function to add the elements from one set to the other
"""
s = {1, 2, 3, 4, 5}
t = {2, 6, 7, 8, 9}
# s.update(t)
# print(s)

# Use .difference_update() to remove the common element 

t.difference_update(s)
print(t)

# Use .symmetric_difference_update() to check the difference and add the to the set

t.symmetric_difference_update(s)
print(t)

"""
Superset - the elements in one set contains all of the elements from another set or more
Subset - the elements in the set is contained in a superset

These concepts will not apply if a new number is added to either sets.  
"""
# This is a subset because it contains all of the elements thats in set y
z = {1, 2, 3}
# This is a superset because it contains all of the elements in set z and more
y = {1, 2, 3, 4, 5, 6, 7}

# Use .issubset() to check if a set is a subset of another set
print(z.issubset(y))

# Use .issuperset() to check if a set is a superset of another set
print(y.issuperset(x))

"""
Convert a collection to a set 
"""
u = [1, 2, 2, 3, 4, 5, 6, 7]
set_x = set(u)
print(set_x)
