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





print ("Enter your name. ")
name = input()
print ("Hello " + name + ", tell me your weight. ")
weight_lbs = int(input())
print ("Thanks, now tell me your height in feet inches, separated by a comma. ")
height_str = input()
height = height_str.split(',')
feet = int(height[0])
inches = int(height[1])
tot_inches = feet*12 + inches
print("Awesome, you are " + str(tot_inches) + " inches tall!")

def bmiResults(name, weight_pounds, height_inches):
    bmi = weight_pounds / (height_inches**2) * 703

    if bmi <= 25: 
        return name + ", your BMI is " + str(bmi) + ". You are not overweight."
    elif bmi <= 18:
        return name + ", your BMI is " + str(bmi) + ".  You are underweight."
    else:
        return name + ", your BMI is " + str(bmi) + ". You are overweight... Damn go see a doctor!"


result1 = bmiResults(name, weight_lbs, tot_inches)

print(result1)
print()


# print(result2)
# print()
# print(result3)
# print()







  

