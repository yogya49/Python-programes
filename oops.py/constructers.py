#Constructor
'''-->Python supports a special type of method called constructor for initilizing the instance variable of a class
   --> A class constructor ,if defined is called whenever a program creats an object of that class
   -->A constructor is called only once at the time of creating an instance
   --> If two instances are created for a class, the constructor will be called once for instance'''
# A)Parameterized constructor
'''--> parameterized constructor are ones which have parameters (other than self)
        defined __init__ method's parameter list.
   --> This type of constructor can take arguments from the user.'''
# B)Non-parameterized constructor
'''--> It is also known as default parameter constructor only peranthesis will be there--->()
   --> The __init__ method includes a single parameter self
   --> No other  parameters are present in __init__ 's parameter list
   --> consequently,This constructor takes no arguments while creating a new object
   --> Non-parametarized constructors assign default values to attribute of a class'''
# The __init__() Method
'''-->This method is a magic method(dunder method) which can use to initilize variables for classes(Objects)
   -->Every calss has __init__ a25nd this is excuted when we instantiate the class
   -->You can also use method to do anything you want to do when the object is created'''
#Self
'''-->Self is a default variable thet contains the memory adress of the current object
   -->This variable is used to create object of a class ,the object name contains the memory location of the object
   -->this memory location is internally passed to self,as self knows the memory adress of the object method because the first argument 
   always the object reference'''
class Student():
    def __init__(self):
        print("hey!..i am the constructor of student class")
        print("I will be automatically invoked when the object is created")
s1=Student()
s2=Student()   
s3=Student()
s4=Student() 

#Calling the constructor
class Employee():
    def __init__(self):
        print("employee class constructor has been called.....")
E1=Employee()
E2=Employee()        