#Constructor overloading -->With in the same class hvaving multliple constructors with same name but different signature
#by using self we can overcome variable shadowing and can initilize memory of a variable
#class is a user defined datatype
'''Write a python program to create a employee class  and declare the states and create 5 objects using different constructors'''
class Employee():
    def __init__(self,empname,empid,depname,job,salary,location):
        self.empname=empname
        self.empid=empid
        self.depname=depname
        self.job=job
        self.salary=salary
        self.location=location
        print("i am a 6 parametraized constructor")
    def __init__(self,empname,empid,depname,job):
        self.empname=empname
        self.empid=empid
        self.depname=depname
        self.job=job
        print("i am a 5 parametraized constructor")
    def __init__(self,empname,empid,depname):
        self.empname=empname
        self.empid=empid
        self.depname=depname     
        print("i am a 4 parametraized constructor")
    def __init__():    
        print("i am a zero parametraized constructor")
emp1=Employee('jbes',234,'eded','ded',23444,'dededdf') 
emp2=Employee('bes',34,'ded','ed',3444) 
emp3=Employee('es',24,'ed','dd') 
emp4=Employee()   
Employee.emp1()
Employee.emp2()
Employee.emp3()
Employee.emp4()        