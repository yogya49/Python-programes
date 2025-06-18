'''object---->States of an objects represents the properties or attributes (represents through data member)
       \ 
       Behaviour of an objects represents the functionality /work done by object (Functions/methods)'''
class Employee():
    def __init__(self,empname,empid,designation,salary,deptname):
        self.Empname=empname
        self.Empid=empid
        self.Designation=designation
        self.Salary=salary
        self.Department=deptname
def Display_details(self):
    print(f"Employee name:{self.Empname}")
    print(f"Employee id:{self.Empid}")
    print(f"Employees designation:{self.Designation}")
    print(f"Employees salary{self.Salary}")
    print(f"Employee DeptName:{self.Department}")
E1=Employee("scott","EMP123","Data analyst","2500","deployment team")
E2=Employee("yogya",'EMP345',"data analystt","20000","bioinformatician")
Display_details(E1)
print("----------------------------------------")
Display_details(E2)