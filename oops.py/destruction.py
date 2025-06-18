'''static Methods--->Static methods are used when some processing is related to class but does not need the class or instances
to perform any work'''
class Mobile:
    def __init__(self):
        print("Object is created")
    @classmethod    #-->with in the class method                                          
    @staticmethod   #-->single copy for the entire class
    def display(self):
        print("i am a class method")
        print("I will work irrespective of object creation")
Mobile.display()
M1=Mobile
M1.display()