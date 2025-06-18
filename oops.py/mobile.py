class Mobile:
    def __init__(self,P,C,B):
        self.Price=P
        self.Color=C
        self.Brand=B
        print("object is created")
    def Set_color(self):
        self.Color="pink"
    def Get_details(self):
        print(f"price: {self.Price}")
        print(f"color:{self.Color}")
        print(f"Brand:{self.Brand}")
m1=Mobile(20000,'green','samsung')
m1.Get_details()
print("******after updating:*******")
m1.Set_color()
m1.Get_details()