class Graduation:
    def __init__(self):
        print("Buhahahah")
    @staticmethod
    def Graduate():
        print("you are a graduate!!")
    #Second sub class
class Bi(Graduation):
    def __init__(self):
        super().__init__()
        print("Haha")
class ece(Graduation):
    def __init__(self):
        super().__init__()
        print("Hehe")
ece.Graduate()