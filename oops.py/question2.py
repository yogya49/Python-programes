'''write a python program to create a mobile class and declare the states of mobile as colour,price,brand,seris,vertion,features
storage,battery,ram,processor create 10 objects and initilize using constructor print the details of the individual object
using function'''
class Mobile():
    def __init__(self,color,price,brand,seris,version,features,storage,battery,ram,processor):
        print("objects are cteated.....")
        self.Color=color
        self.Price=price
        self.Brand=brand
        self.Seris=seris
        self.Version=version
        self.Features=features
        self.Storage=storage
        self.Battery=battery
        self.Ram=ram
        self.Processor=processor
def display_details(self):
    print(f"the colour of mobile is--->{self.Color}") 
    print(f"the price of mobile is--->{self.Price}") 
    print(f"the Brand of mobile is--->{self.Brand}") 
    print(f"the seris of mobile is--->{self.Seris}")
    print(f"the features of mobile is--->{self.Features}")
    print(f"the version of mobile is--->{self.Version}") 
    print(f"the Storage of mobile is--->{self.Storage}") 
    print(f"the Battery of mobile is--->{self.Battery}")
    print(f"the ram of mobile is--->{self.Ram}")
    print(f"the Processor of mobile is--->{self.Processor}")
M1=Mobile("bule","20000","redmi","Note","11A","good screen","128GB","120MaH","16GB","snapdragon")
m2 = Mobile("Black", "15000", "Realme", "Narzo", "50A", "HD+", "64GB", "6000mAh", "4GB", "MediaTek")
m3 = Mobile("White", "25000", "Samsung", "Galaxy", "M14", "FHD+", "128GB", "6000mAh", "6GB", "Exynos")
m4 = Mobile("Silver", "55000", "Apple", "iPhone", "13", "Retina", "128GB", "3200mAh", "4GB", "A15 Bionic")
m5 = Mobile("Green", "22000", "Motorola", "G", "73", "FHD+ OLED", "128GB", "5000mAh", "8GB", "Dimensity 930")
m6 = Mobile("Grey", "18000", "Infinix", "Zero", "5G", "LCD", "128GB", "5000mAh", "6GB", "Dimensity 920")
m7 = Mobile("Purple", "27000", "Vivo", "T", "1 5G", "IPS LCD", "128GB", "5000mAh", "8GB", "Snapdragon 695")
m8 = Mobile("Gold", "30000", "OnePlus", "Nord", "CE 3 Lite", "FHD+ LCD", "256GB", "5000mAh", "8GB", "Snapdragon 695")
m9 = Mobile("Pink", "13000", "Lava", "Blaze", "5G", "HD+", "64GB", "5000mAh", "4GB", "MediaTek Dimensity")
m10 = Mobile("Orange", "16000", "POCO", "M", "4 Pro", "FHD+ LCD", "128GB", "5000mAh", "6GB", "Snapdragon 695")
display_details(M1)
print("--------------------------------------------------------------------------------------------------------")
display_details(m2)
print("--------------------------------------------------------------------------------------------------------")
display_details(m3)
print("--------------------------------------------------------------------------------------------------------")
display_details(m4)
print("--------------------------------------------------------------------------------------------------------")
display_details(m5)
print("--------------------------------------------------------------------------------------------------------")
display_details(m6)
print("--------------------------------------------------------------------------------------------------------")
display_details(m7)
print("--------------------------------------------------------------------------------------------------------")
display_details(m8)
print("--------------------------------------------------------------------------------------------------------")
display_details(m9)
print("--------------------------------------------------------------------------------------------------------")
display_details(m10)
      
        