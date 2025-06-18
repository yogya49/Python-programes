class GrandFather:
    def __init__(self):
        pass
    #Method overriding
    #@staticmethod
    def Properties(self):
        print("100 acers of land")
class Father(GrandFather):
    def __init__(self):
        super.__init__()
    @staticmethod
    def Properties():
        print("50 acers of land")
class YourSelf(Father):
    def __init__(self):
        super.__init__()
    def Properties():
        print("10 acers of land")
GrandFather.Properties()
Father.Properties()
YourSelf.Properties
    
