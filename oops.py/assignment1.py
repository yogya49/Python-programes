'''write a python program to create a product class declare the class as product name,productid,price,GST,manifacture date,expire date 
create 5 objects initilize using parametors,constructors and acess the the method using instructor method,declare mutated method set
product name,id of 6 properties and change the values of their proprties using detected method'''
class Product:
    def __init__(self,Name,id,price,gst,manifacture,date,expiredate):
        self.ProductName=Name
        self.ID=id
        self.Price=price
        self.GST=gst
        self.Manifacture=manifacture
        self.Date=date
        self.Expire=expiredate
    def Get_details(self):
        print(f"name of the product is: {self.ProductName}")
        print(f"The id is:{self.ID}")
        print(f"price is:{self.Price}")
        print(f"Gst:{self.GST}")
        print(f"manifacture:{self.Manifacture}")  
        print(f"date:{self.Date}")   
        print(f"expire date:{self.Expire}")
    def set_changes(self):
        self.Price="30000"
M1=Product('samsung','123abc','20000','18 percent','22-april-2025','12-august','22-april-2030')
M1.Get_details()
print("***After updating***")
M1.set_changes()
M1.Get_details
