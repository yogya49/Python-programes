#write a python program to print alphabets using recyrsive function
def Alphabets(ch):
    if ch>=ord('A') and ch<=ord('Z'):
        print(chr(ch))
        return Alphabets(ch+1)
ch=65
Alphabets(ch)
print("----------------------------")
#reverse order
def Alphabets(ch):
    if ch>=ord('A') and ch<=ord('Z'):
        print(chr(ch))
        return Alphabets(ch+1)
ch=65
print("Reverse order")
Alphabets(ch)
print("----------------------------")