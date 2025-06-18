'''senario
you had participated in a colloge level coding fest which was there for 6 days'''
#Task
'''write a python program to give the final report which includes
1)Activities for the day including timeline
2)number of teams/paticipants for the day
3)project_names
4)Technologies used
5)PPT demonistrations given
6)winner of the day
7)Runner up of the day
8)Best performer of the day
9)Host of the program for that day'''
class coding_fest():
    def __init__(self,day,host,activities,paticipants,project_names,technologies,winner,ppt,runner,best_performer):
        self.Day=day
        self.Host=host
        self.Activities=activities
        self.Paticipants=paticipants
        self.Project_names=project_names
        self.Technologies=technologies
        self.Winner=winner
        self.PPT=ppt
        self.Runner=runner
        self.Best_performer=best_performer
    def details(self):
        print(f"for :{self.Day}")
        print(f"The host for this day is{self.Host}")    
        print(f"Activities that are conducted on that day are:{self.Activities}") 
        print(f"The paticipants are{self.Paticipants}")  
        print(f"The projet_names are{self.Project_names}")
        print(f"The technologies used are:{self.Technologies}")
        print(f"The winner is :{self.Winner}")
        print(f"power point presentations presented by the students are:{self.PPT}")
        print(f"The Runner of this fest is :{self.Runner}")
        print(f"The best_performer of the fest:{self.Best_performer}")
        print("----------------------------------------------")
n=int(input("how many events days you are going to conduct an event::"))
events=[]
for i in range(n):
    print(f"\nEnter the details of n{i+1}:")
    Day=input("Enter day:")
    Host=input("enter the name of the host:")
    Activities=input("enter activies that are conducted on that day:")
    Paticipants=input("enter paticipants:")
    Project_names=input("enter the names of the project:")
    Technologies=input("Technologies used for this project are:")
    PPT=input("Name of the presentation is:")
    Best_performer=input("Best_performer of the fest is:")
    Winner=input("winner of this fest is:")
    Runner=input("Runner of the fest is:")
event=coding_fest(Day,Host,Activities,Paticipants,Project_names,Technologies,PPT,Best_performer,Winner,Runner)    
events.append(event)
print("################# ALL ABOUT TODAY'S EVENT #################")
for e in events:
    e.details()