class Employee:
    def __init__(self,empname,empid,designation,salary,depname):
        self.Empname=empname
        self.Empid=empid
        self.Designation=designation
        self.Salary=salary
        self.Department=depname
    def Get_details(self):
        print(f"Employee name: {self.Empname}")
        print(f"Employee id: {self.Empid}")
        print(f"Employees designation: {self.Designation}")
        print(f"Employees salary: {self.Salary}")
        print(f"Employee DeptName: {self.Department}")
E1=Employee("scott","EMP123","Data analyst","2500","deployment team")
E1.Get_details()
        