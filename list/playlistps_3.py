size=int(input("enter how many songs u want::"))
songs=[]
for i in range(size):
    temp=input()
    songs.append(temp)
print(songs)
print(songs[::-1])