'''Inheritance:::It is the process of aquaring the properties of one class into another
---->Super class:The class which gives properties to another classis known as super class/base class/parent class
---->sub class:The class which aquires the properties of another class'''
#single level inheritance
'''vehicle(super class)--->car(sub class)
   vehicle(super class)-->Bike(subclass,super class)-->superbike(sub class)'''
'''                                          VEHICLE
                                                 |
                            -------------------------------------------
                            |           |          |         |        |
                            Bike       Car        Bus       Auto      cycle
                            
                            
                            c programming
                                 /\
                                /  \
                               /    \
                             java   c++     
                               \     /
                                \   /
                                 \ /
                                 python
#Single level inheritance                              '''
class Vehicle:
    def __init__(self):
      print("i am a vehicle class constructor")
    @staticmethod #This is used when we want to define method inside class,does not need to acess self and class
    def start():
        print("vehicle is started")
class Car(Vehicle):    
    def __init__(self):
        super().__init__()
        print("i am the Car class constructor")
    @staticmethod
    def start():
        print("car is started")
class Bike(Vehicle):
    def __init__(self):
        super().__init__()
        print("my nme befsj")
    @staticmethod
    def start():
        print("hfrkuw")
c1=Bike()


          