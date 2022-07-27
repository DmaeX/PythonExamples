# # Defining a function 

# def function1(x):
#     print("ahhh")
#     print("ahhh2")
# function1()

 
# Mapping 

# def function3(x):
#     return 2 + x

# a = function3(3)
# print(a)


# def function4(x, y):
#     return x * y

# b = function4(4, 3)
# print(b)    


# name1 = "Ronan"
# weight_lbs1 = 165 
# height_inch1 = 70


# name2 = "DM"
# weight_lbs2 = 150
# height_inch2 = 62


# name3 = "Clarissa"
# weight_lbs3 = 125 
# height_inch3 = 60


# print ("Enter your name. ")
# name = input()
# print ("Hello " + name + ", tell me your weight. ")
# weight_lbs = int(input())
# print ("Thanks, now tell me your height in feet inches, separated by a comma. ")
# height_str = input()
# height = height_str.split(',')
# feet = int(height[0])
# inches = int(height[1])
# tot_inches = feet*12 + inches
# print("Awesome, you are " + str(tot_inches) + " inches tall!")

# def bmiResults(name, weight_pounds, height_inches):
#     bmi = weight_pounds / (height_inches**2) * 703

#     if bmi <= 25: 
#         return name + ", your BMI is " + str(bmi) + ". You are not overweight."
#     elif bmi <= 18:
#         return name + ", your BMI is " + str(bmi) + ".  You are underweight."
#     else:
#         return name + ", your BMI is " + str(bmi) + ". You are overweight... Damn go see a doctor!"


# result1 = bmiResults(name, weight_lbs, tot_inches)

# print(result1)
# print()


# num_1 = 20 
# num_2 = 30
# num_3 = 40

# def threeNumbers(num_1, num_2, num_3):
#     sumOfThree = num_1 + num_2 + num_3
#     return sumOfThree

# totalOfEverything = threeNumbers(2, 3, 4)
# totalOfEverything1 = totalOfEverything / num_2
# print(totalOfEverything1)
# print()



# people = ["Clarissa", "DM", "Ronan", "Gian"]

# def favoritePerson(people): 
#     for person in people:
#         if "m" in person.lower():
#             continue 
#         elif "s" in person.lower():
#             continue
#         elif "i" in person.lower():
#             break
#         else: 
#             return person 

# nameOfFavoritePerson = favoritePerson(people)
# print(nameOfFavoritePerson)


# x = 20

# def test_operation(x):
#     return x * 7




# numbers = [10, 20, 30, 40, 50, 55, 60, 70, 80, 85, 90, 100]

# def evenNumbers(numbers):
#     evens = []
#     for number in numbers:
#         if number % 2 == 0: 
#             evens.append(number)
#     return evens
        
# numWithEvenNumbers = evenNumbers(numbers)
# print(evenNumbers(numbers))

  
# numbers = [10, 20, 30, 40, 50, 55, 60, 70, 80, 85, 90, 100]

# def oddNumbers(numbers):
#     odds = []
#     for number in numbers:
#         if number % 2 == 1: 
#             odds.append(number)
#     return odds
        
# numWithOddNumbers = oddNumbers(numbers)
# print(oddNumbers(numbers))



# def greeting(name):
#     print(f"Hello there, {name}!")

# greeting("DM")


# def addingSimpleNumbers(n1, n2):
#     sumOfTwoNumbers = n1 + n2
#     print(sumOfTwoNumbers)

# number1 = 53.4
# number2 = 43.6
# addingSimpleNumbers(number1, number2)



# def FunOperations(n1, n2, n3):
#     totalForAll = n1 + (n2 * n3)
#     print(f"This simple math returns something large such as this: {totalForAll}.")

# number1 = 53.4
# number2 = 43.6
# number3 = 60
# FunOperations(number1, number2, number3)



# def FunOperations(n1, n2, n3):
#     totalForAll = n1 + (n2 * n3)
#     print (f"This simple math returns something large such as this: {totalForAll}.")

# number1 = 53.4
# number2 = 43.6
# number3 = 60
# FunOperations(number1, number2, number3)


# def square(x): 
#     y = x * x
#     return y

# print(square(4))


# def square(x, y): 
#     return x * y / x

# print(square(4, 3))


animals = ["cats", "dogs", "aligators", "tigers", "snakes"]

def FavoriteAnimal(animals):
    animal = []
    for animal in animals: 
        if 'd' in animal.lower():
            continue 
        elif 'g' in animal.lower(): 
            continue
        else:
            print(f"Your favorite animal are {animal}.")
        return animal

MyFavoriteAnimal = FavoriteAnimal(animals) 
     


