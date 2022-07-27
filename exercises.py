w = "b"  # <- Change this
x = "hello"  # <- Change this
y = "hello"  # <- Change this
z = "d"  # <- Change this

# Don't change any of these `condition_` variables.
condition_1 = w != "a" 
        #   = "b" != "a"

condition_2 = w < x
        #   = "b" < "hello"   

condition_3 = x == y
        #   = "hello" == "hello"

condition_4 = y == "hello"
        #   = "hello" == "hello"

condition_5 = z > "c"
          # = "d" > "c"


# All of these should print `True`.
print(condition_1)
print(condition_2)
print(condition_3)
print(condition_4)
print(condition_5)