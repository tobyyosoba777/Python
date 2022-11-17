# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 07:46:49 2022

@author: TOBBY
"""

import array
for name in array.__dict__:
    print(name)






#defining a function
# when defining a function do not forget to add the () in front of it to symbolize it is a function
def circle():
    print("it is always curved and round in shape")
circle()


def new_functions():
    print("this is a new function practice again")
new_functions()


def another_function1():
    print("this is another function")
another_function1()


def function1():
    print("function 1")
function1()


def function2():
    print("function 2")
function2()


def function3():
    # the asteriks will print it out seperately in strings """ f u n c t i o n 3 """
    print(*"function 3")
    
    
#arbitrary arguments (*args)
def my_function(*kids):
  print("The youngest child is " + kids[2])
my_function("Emil", "Tobias", "Linus")


def my_function(*person):
    print("the friendly one is " + person[1])
    
my_function("gabriel", "michael", "raphael")


def new_practice(*car):
    print(f"i drive a {car[2]}")
new_practice("aston martin", "BMW", "lamborghini")


def headset(*model):
    print("i use a " + model[0] + " headset")
headset("Zealot", "oraimo")



def function(b):
    return b
a = function("hello this is a new function")
print(a)



def newfunction(a):
    print("new function defined with the ouput " + a )
newfunction("new")  #calling the function and setting an input



def somethingRandom(object1, object2, object3):
    a = f"{object1},{object2},{object3}"
    return a.title()
b = somethingRandom('power-bank', ' music-player', ' book')
print(b)



def somethingrandom(house, car, color):
    a = f'{house},{car},{color}'
    return a.title()
b = somethingrandom(house= 'duplex', car= ' honda-civic', color= ' grey')
print(b)



def a(set1,set2,set3,set4):
    a = f'{set1}{set2}{set3}{set4}'
    return a.title()
b = a('AB',' BA',' AA',' BB')
print(b)



def afunction(fun1, fun2, fun3):
    char = f'{fun1}{fun2}{fun3}'
    return char.title()
a = afunction('car', ' color', ' crayon')
print(a)






"""
Something a bit different here
"""

"""ARGS"""
#ARGS stands for arbitrary argument while KWARGS stands for Keyword Arguments
#making an argument optional
def get_formatted_name(first_name, middle_name, last_name):
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()
musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)



def orderly_name_model(brand, model, year):
    car = f"{brand} {model} {year}"
    return car.title()
car_spec = orderly_name_model('Lamborghini', 'huracan', '2019')
print(car_spec)




# a function to add multiple numbers in python
def add_numbers(*nums):  #use the keyword argument to hold multiple values in the parameter
    total = 0
    for num in nums:
        total += num
    return total

c = add_numbers(10,101, 200, 567)
print(c)











class MyClass:
    x = 120
    
#the MyClass is a class in python
p1 = MyClass()
print(p1.x)


#the __init__() function
#To understand the meaning of classes we have to understand the built-in __init__() function,All classes have a function called __init__(), which is always executed when the class is being initiated.
#The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
#The self in keyword in Python is used to all the instances in a class. By using the self keyword, one can easily access all the instances defined within a class, including its methods and attributes. init. __init__ is one of the reserved methods in Python. In object oriented programming, it is known as a constructor.

class Point:
    def move(self):
        print('move')
        
    def draw(self):
        print('draw')
point1 = Point()
point1.x = 10
point1.y = 20
print(point1.x)
point1.draw()


point2 = Point()
point2.x = 1
print(point2.x)  

print('\n')  #this will add a line break




#constructor
#the __init__ function is a constructor used to add extra parameters to the class
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def move(self):
        print('move')
        
    def draw(self):
        print('draw')
point = Point(10, 20)
point.x = 11
print(point.x)


print('\n')



class person:
    def __init__(self,talk, name):
        self.name = name
        self.talk = talk
    def Talk(self):
        print(f'hi, i am {self.name}')
    def Name(self):
        print(self.talk)
tobi = person('I love python programming for AI', 'Tobiloba ')
justin = person('I love playing games', 'Michael')

tobi.Talk()
justin.Talk()



class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
p1 = person('tobi', 18)
print(p1.age, p1.name)



class car_info:
    def __init__(self, car_brand, model):
        self.car_brand = car_brand
        self.model = model
p2 = car_info(car_brand="porsche" , model="991 gt3")
print(p2.car_brand, p2.model)
print(p2.model)



#define a class named athlete use the __init__() function to assign a value named name, age and profession
class Athlete:
    def __init__(self,name,age,profession):
        self.name = name
        self.age = age
        self.profession = profession
a1 = Athlete(name="Lionel Messi", age=35, profession="footballer")
print(f"{a1.name} is {a1.age} and is a professional {a1.profession}")



class colors:
    def __init__(self,black,white,yellow,red,orange,grey,purple):
        self.black = black
        self.white = white 
        self.yellow = yellow
        self.red = red
        self.orange = orange
        self.grey = grey
        self.purple = purple
new_color = colors(black= "Black", white= "White", yellow= "Yellow" , red= "Red", orange= "Orange", grey= "Grey", purple= "Purple")
print("colors are " + new_color.black, new_color.white,new_color.yellow,new_color.red,new_color.orange,new_color.grey,new_color.purple)



class car_info:
    def __init__(self, car_name, exact_model):
        self.car_name= car_name
        self.exact_model= exact_model
p2 = car_info(car_name = "lamborghini", exact_model = "sian")
print(p2.car_name, p2.exact_model)




