##### I C O M P L E T E  C O D E #####

class Student:
     studentCount = 0
     database = {}
     def __init__(self,name,department,admissionSemester):
         self.name = name
         self.dept = department
         self.adSem = admissionSemester
     def __str__(self):
         return "Name:{}\nDepartment:{}\nAdmission Semester:{}".format(self.name,self.dept,self.adSem)

#Write your code here
class CSEStudent(Student):
    def __init__(self,name,department,admissionSemester,cgpa=0.0,creditsCompleted=0.0):
        super().__init__(name,department,admissionSemester)
        CSEStudent.studentCount+=1
        self.cgpa=cgpa
        self.creditsCompleted=creditsCompleted
        self.studentID = self.admissionSemester[-2:]
        CSEStudent.database[]=[]
    def __str__(self):


    def createStudent(a,b,c,d=0.0,e=0.0):
        x=CSEStudent(a,b,c,d,e)
        return x


print("Number of Students:",Student.studentCount)
print("Student database:",Student.database)
s1 = CSEStudent("Adam","CSE","Fall 2020",3.94,12.0)
print("------Details of the student------")
print(s1)
print("#################################")
s2 = CSEStudent("Jenny","CSE","Spring 2021")
print("------Details of the student------")
print(s2)
print("#################################")
s3 = CSEStudent.createStudent("Robert","CSE","Summer 2020",3.78,24.0)
print("------Details of the student------")
print(s3)
print("#################################")
print("Number of Students:",Student.studentCount)
print("Student database:",Student.database)
"""
Output:
Number of Students: 0
Student database: {}
------Details of the student------
Student ID:202011
Name:Adam
Department:CSE
Admission Semester:Fall 2020
CGPA:3.94
Credits Completed:12.0
#################################
------Details of the student------
Student ID:211012
Name:Jenny
Department:CSE
Admission Semester:Spring 2021
CGPA:0.0
Credits Completed:0.0
#################################
------Details of the student------
Student ID:203013
Name:Robert
Department:CSE
Admission Semester:Summer 2020
CGPA:3.78
Credits Completed:24.0
#################################
Number of Students: 3
Student database: {'202011': ['Adam', 'CSE', 3.94, 12.0], '211012':  
['Jenny', 'CSE', 0.0, 0.0], '203013': ['Robert', 'CSE', 3.78, 24.0]}
"""