
#  Functions for every primitive operator 
def Addition(x:int, y:int) -> int:
    return x + y

def Subtraction(x:int, y:int) -> int:
    return x - y 

def Multiplication(x:int, y:int) -> int:
    return x * y

def Division(x:int, y:int) -> int: 
    return x / y


#  Select a operator
print("Select an arithmetic operator from the following choices:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

while True:
    choice = input("Pick an operator(1/2/3/4)")
    if choice in ("1", "2", "3", "4"):
        x = (int(input("Enter first number: ")))
        y = (int(input("Enter second number: ")))

        if choice == "1": 
            print(int(Addition(x, y)))
        elif choice == "2":
            print(int(Subtraction(x, y)))
        elif choice == "3":
            print(int(Multiplication(x, y)))  
        elif choice == "4":
            try:
                print(int(Division(x, y))) 
            except ZeroDivisionError as e:
                print("Zero Division Error!", e)  

    else: 
        print("Thanks for using DM's calculator! Enjoy your day! ") 
        break
        

     
        
         


      

    