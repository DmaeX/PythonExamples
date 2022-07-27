
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
        print('My favorite color is {}'.format(self.color))

#  creating new object
r1 = Robot("Tom", "red", 30)
r2 = Robot("Jerry", "blue", 40) 

r1.introduce_Self() 
r2.introduce_Self()


class Person: 

    def __init__(self, name:str, personality:str, dance:bool, robot):
        self.name = name
        self.personality = personality
        self.dance = dance 

    def introduce_Person_Self(self): 
     print(f"Hello there, my name is {self.name}. I am friends with {robot1}!")
     print(f"Hello, there, my name is {self.name}. I am friends with {robot2}!")

robot1 = Robot("Tom", "red", 30)
robot2 = Robot("Jerry", "blue", 40)

p1 = Person("Kerry", "outgoing", "true", robot1)
p2 = Person("Crissy", "quiet", "false", robot2)

p1.introduce_Person_Self()
p2.introduce_Person_Self()    

    






