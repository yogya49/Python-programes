'''Functions/Methods:
Method overloading::With in the same class having multliple methods with same name but different parameters is called method overloading
python is loosely typed
'''
class Mobile():
    def __init__(self):
        print("object is created..!")
def UnlockMobile():
    print("swipe up to unlock your mobile..!")
UnlockMobile()
def UnlockMobile(Password):
    print("Enter password to unlock mobile")
UnlockMobile("xyz")
def UnlockMobile(Pattern):
    print("Enter pattern to unlock mobile")
UnlockMobile('aaa')
    
        