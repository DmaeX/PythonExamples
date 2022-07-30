
try: 
    2 / 0
except ValueError as e: 
    print("Exception!", e)
except ZeroDivisionError as e:
    print("Division Error!", e)
   
print("Done!")    

