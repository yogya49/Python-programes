'''you have attended a skill devlopment training program for 15 days on python program for 15 days on python programming langauge'''
#Task:::::
'''write s python program to give detailed report of 15 days python training which includes
---> 1.DAY
---> 2.TOPICS COVERED
---> 3.EFFECIENCY(rate of effeciency and grip of topics learnt on scale of 5)
---> 4.Number of assignment questions solved
---> 5.Ratings achived on hacker rank for that particular day
---> 6.Certifications completed(including name of certificated)
---> 7.Duration of class
---> 8.Rate of session on scale of 5 where
       i)Being worst
       ii)Being bad
       iii)being average
       iv)being good
       v)being best'''
class Python_report():
    def __init__(self,day,topics, covered,effeciency,no_que_solved,ratings,certifications,duration,rating):
        self.Day=day
        self.Topics=topics
        self.Covered=covered
        self.Effeciency=effeciency
        self.Solved=no_que_solved
        self.Ratings=ratings
        self.Certifications=certifications
        self.Duration=duration
        self.Rating=rating
def Details(self):
    print(f"for the day is:{self.Day}")
    print(f"the topics  are {self.Topics}")
    print(f"the topics covered are {self.Covered}")
    print(f"the number of questions solved are:{self.Solved}")
    print(f"the effeciency is:{self.Effeciency}")
    print(f"ratings from 1to5 the students gave {self.Ratings}")
    print(f"certificatons are:{self.Certifications}")
    print(f"Time taken{self.Duration}")
    print(f"rating for scale of 5 {self.Rating}")
    print("-----------------------------------------------------------")
p1 = Python_report("Day 1", "Python Basics", "variables, data types", "High", 15, 4, "None", "2h", "8/10")
p2 = Python_report("Day 2", "Operators", "arithmetic, logical", "Medium", 12, 3, "None", "2h", "7/10")
p3 = Python_report("Day 3", "Control Flow", "if, else, elif", "High", 18, 5, "None", "2.5h", "9/10")
p4 = Python_report("Day 4", "Loops", "for, while", "Very High", 25, 5, "None", "3h", "10/10")
p5 = Python_report("Day 5", "Functions", "def, return, parameters", "High", 20, 5, "Python Fundamentals", "3h", "9/10")
p6 = Python_report("Day 6", "Strings", "slicing, methods", "Medium", 15, 4, "None", "2h", "7.5/10")
p7 = Python_report("Day 7", "Lists", "append, insert, pop", "Medium", 14, 4, "None", "2h", "7/10")
p8 = Python_report("Day 8", "Tuples & Sets", "immutability, operations", "Medium", 13, 4, "None", "2h", "7/10")
p9 = Python_report("Day 9", "Dictionaries", "keys, values, loops", "High", 19, 4, "None", "2.5h", "8.5/10")
p10 = Python_report("Day 10", "OOP - Part 1", "class, object", "Very High", 22, 5, "OOP Basics", "3h", "9/10")
p11 = Python_report("Day 11", "OOP - Part 2", "init, self, methods", "Very High", 25, 5, "OOP Intermediate", "3h", "9.5/10")
p12 = Python_report("Day 12", "Inheritance", "single, multiple", "High", 20, 5, "OOP Advanced", "3h", "9/10")
p13 = Python_report("Day 13", "File Handling", "read, write", "High", 18, 4, "File Handling Certificate", "2.5h", "8.5/10")
p14 = Python_report("Day 14", "Exception Handling", "try, except", "Medium", 16, 4, "None", "2h", "7.5/10")
p15 = Python_report("Day 15", "Project Work", "mini Python project", "Very High", 30, 5, "Project Completion", "4h", "10/10")
Details(p1)

Details(p2)
Details(p3)
Details(p4)
Details(p5)
Details(p6)
Details(p7)
Details(p8)
Details(p9)
Details(p10)
Details(p11)
Details(p12)
Details(p14)
Details(p15)




    
        
    
    