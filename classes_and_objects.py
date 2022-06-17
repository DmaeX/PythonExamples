
#  Define a class called Robot
class Robot: 

    #  Contructor
    def __init__(self, name:str, color:str, weight:float):
        self.name   = name
        self.color  = color
        self.weight = weight

    #  Self refers to whatever we run this function on
    #  Whenever a method is within a call, you have to pass in an argument 
    def introduce_Self(self): 
        print(f"My name is {self.name}!")
        print('My favorite color is {}, {}, {}'.format(self.color, 5, 6))

#  creating new object
r1 = Robot("Tom", "red", 30)
r2 = Robot("Jerry", "blue", 40) 

r1.introduce_Self()
r2.introduce_Self()
