"""
𝗤𝘂𝗲𝘀𝘁𝗶𝗼𝗻:
Write the 𝐂𝐒𝐄𝐒𝐭𝐮𝐝𝐞𝐧𝐭 class derived from 𝐒𝐭𝐮𝐝𝐞𝐧𝐭 class with the required methods to give the following outputs as shown.
[𝐇𝐢𝐧𝐭𝐬:
Each course has 3 credits.
𝐆𝐏𝐀 = sum( per course grade * per course credit) / sum(credit attended in that semester)
𝐆𝐫𝐚𝐝𝐢𝐧𝐠 𝐩𝐨𝐥𝐢𝐜𝐲   mark>=85: 4.0 ; 80<=mark<=84: 3.3;70<=mark<=79:3.0 ;65<=mark<=69: 2.3; 57<=mark<=64:2.0 ; 55<=mark<=56:1.3; 50<=mark<=54:1.0; >50:0.0]
"""

"""
############################
Name: Bob
ID: 20301018
Current semester: Fall 2020
############################
Name: Carol
ID: 16301814
Current semester: Fall 2020
############################
Name: Anny
ID: 18201234
Current semester: Fall 2020
############################
----------------------------
Bob has taken 3 courses.
CSE111: 3.3
CSE230: 3.0
CSE260: 4.0
grades of Bob is: 3.43
----------------------------
Carol has taken 4 courses.
CSE470: 2.0
CSE422: 2.3
CSE460: 3.0
CSE461: 4.0
grades of Carol is: 2.83
----------------------------
Anny has taken 3 courses.
CSE340: 0.0
CSE321: 4.0
CSE370: 4.0
grades of Anny is: 2.67
"""


class Student:
    def __init__(self,name,ID):
        self.name = name
        self.ID = ID
    def Details(self):
        return "Name: "+self.name+"\n"+"ID: "+self.ID+"\n"

#Write your code here
class CSEStudent(Student):
    def __init__(self,name,ID,semester):
        super().__init__(name,ID)
        self.semester=semester
        self.courses=[]
        self.scores=[]
        self.grades=[]
        self.gpa=0
    def Details(self):
        return super().Details()+"Current semester: "+self.semester
    def showgrades(self):
        self.calgpa()
        self.calcgpa()
        total=0
        print(self.name,"has taken",len(self.courses),"courses.")
        for a in range(len(self.courses)):
            print(str(self.courses[a])+": "+str(self.grades[a]))
            total+=self.grades[a]
        self.gpa=total/len(self.courses)
        print("GPA of Anny is:",round(self.gpa,2))
    def calgpa(self):
        for a in self.scores:
            if a<50:
                self.grades.append(0.0)
            elif a<=54:
                self.grades.append(1.0)
            elif a<=56:
                self.grades.append(1.3)
            elif a<=64:
                self.grades.append(2.0)
            elif a<=69:
                self.grades.append(2.3)
            elif a<=79:
                self.grades.append(3.0)
            elif a<=84:
                self.grades.append(3.3)
            else:
                self.grades.append(4.0)
    def calcgpa(self):
        pass
    def addCourseWithMarks(self,*args):
        for a in range(0,len(args),2):
            self.courses.append(args[a])
            self.scores.append(args[a+1])
            
Bob = CSEStudent("Bob","20301018","Fall 2020")
Carol = CSEStudent("Carol","16301814","Fall 2020")
Anny = CSEStudent("Anny","18201234","Fall 2020")
print("############################")
print(Bob.Details())
print("############################")
print(Carol.Details())
print("############################")
print(Anny.Details())
print("############################")
Bob.addCourseWithMarks("CSE111",83.5,"CSE230",73.0,"CSE260",92.5)
Carol.addCourseWithMarks("CSE470",62.5,"CSE422",69.0,"CSE460",76.5,"CSE461",87.0)
Anny.addCourseWithMarks("CSE340",45.5,"CSE321",95.0,"CSE370",91.0)
print("----------------------------")
Bob.showgrades()
print("----------------------------")
Carol.showgrades()
print("----------------------------")
Anny.showgrades()