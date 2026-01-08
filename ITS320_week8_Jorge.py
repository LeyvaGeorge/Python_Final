""" School Registration System"""
"""
1.User Authentication:
Implement a basic login system with predefined usernames and passwords for students and administrators. 
Use the ID “admin” for the Administrator, with password “password”.
2.Course Management:
Course Management by Admin:
- Add new courses.
- Remove courses.
- Update course details (like title, description, credits, capacity).- 
- Search for courses by title or course ID.
Student Course Registration:
- Allow students to register for courses.
- Allow students to drop courses.
3.Reports:
ADMIN:
- List all students registered for a specific course.
- List all courses for which a specific student registered.
- List of all student IDs and passwords.
STUDENTS:
- List all courses for which this student registered.
BOTH:
- List all courses (showing if each is still full or not.)
4.Additional Features:
- Implement capacity limits for courses and prevent registration if the course is full.

"""
# ==========  CLASSES  ==========
class University:
    def __init__(self):
        self.admins = []   #This is the admins for the School Registration System
        self.students = []
        self.courses = []
    
    def addAdmins(self, adm_to_add):
        if isinstance(adm_to_add, Admin):
            self.admins.append(adm_to_add)
        else:
            print("Error: You can only enroll valid Admin objects")
    def addStu(self, stu_to_add):
        if isinstance(stu_to_add, Student):
            self.students.append(stu_to_add)
        else:
            print("Error: You can only enroll valid student objects.")

    def addCourse(self,course_to_add):
        if isinstance(course_to_add, Course):
            self.courses.append(course_to_add)
        else:
            print("Error: You can only enroll valid Course objects.")
    
    def printCourses(self):
        for index in self.courses:
            print(f"Title:{index.title}")
            print(f"ID:{index.id}")
            print(f"Credit:{index.credit}")
            print(f"Capacity:{index.capacity}")
            print(f"Description:{index.description}")
    #this is the menu 
    def start(self):
        """The main entry point for the program."""
        while True:
            print("1. Login")
            print("2. Exit")
            choice = input("Select an option: ")
            
            if choice == "1":
                self.login()
            elif choice == '2':
                print("Goodbye!")
                break
            else:
                print("Invalid choice, please try again.")
    #TODO
    def login(self):
        user_id = input ("Enter ID: ")
        password = input("Enter Password: ")
        print(user_id, " ", password)

class Course:
    def __init__(self, ti, id, cr, ca,desc):
        self.title = ti
        self.id = id
        self.credit = cr 
        self.capacity = ca
        self.description = desc
        self.stuID = [] #adds id to see who is enrolled

class Person:
    def __init__(self,fName,lName):
        self.f_name = fName
        self.l_name = lName

    def getFirstName(self):
        return self.f_name
    
    def getLastName(self):
        return self.l_name
    
    def getName(self):
        str = self.f_name + ' ' + self.l_name
        return str
    
class Admin(Person):
    def __init__(self,fname,lname,ID, Pword):
        Person.__init__(self,fname,lname)
        self.admin_ID = ID
        self.admin_Password = Pword
    
    def getId(self):
        return self.admin_ID
    
    def getPassword(self):
        return self.admin_Password

class Student(Person):
    def __init__(self,fname,lname,id, password):
        Person.__init__(self,fname,lname)
        self.id = id
        self.password = password
        self.reg_course = []

# ========== FUNCTION  ==========
# ==========   SETUP   ==========
#List of classes to add to the management system
catalog = [
    ("Intro Art","AR100",3, 30,"Develop skiils to successfully draw the human form." ),
    ("English 101","EN101",3, 25,"Students receive instruction in academic reading and writing, including writing processes, effective use of language, analytical thinking, and the foundations of academic research."),
    ("Algebra","MA105",3, 30,"This course covers graphing of polynomial, rational and transcendental functions." ),
    ("Calculus","MA135",3, 25,"This course covers functions and their graphs, including exponential and logarithmic functions."),
    ("Anatomy & Physiology","AP102",5,20,"This course is the first in a two part series covering the topics of the chemical, cellular, and tissue levels of organization"),
    ("Beginning Guitar","MU054",1, 5,"This course offers individual guitar instruction to students who have little or no previous training.")
]
#Creates a list of students to add to the management system
students = [
    ("Liam","Smith","LiaSm95","owU9-A3WD"),
    ("Olivia","Taylor","OliTa01","25le-C87z"),
    ("Oliver","White","OliWh05","0glu-zi1D"),
    ("Emily","Leyva","EmiLe02","vcnJ-Gl98"),
    ("Levi","Clark","LevCl90","WZ7o-n5QJ"),
    ("Isabella","Ferrero","IsaFe03","SDg9-DT9l"),
    ("William","Young","WilYo97","J38D-NXN3"),
    ("Ava","King","AvaKi99","QX1I-sswP"),
    ("James","Green","JamGr06","4b9Y-beOD"),
    ("Sofia","Collins","SofCo02","yxam-Iy1u")
]
#Creates and Administrator with ID and password
administrator = Admin("Renee","Carroll","admin","password")

#Instatiate the Main Management System
CSUglobal = University()
#Adds courses to the Management System
for title, id, credit, capacity, description in catalog:
    classroom = Course(title, id, credit, capacity, description)
    CSUglobal.addCourse(classroom)
#Adds students to the Management System
for first,last, identifier, secret in students:
    body = Student(first,last,identifier,secret)
    CSUglobal.addStu(body)
#Adds the single Admin with Name, ID, password
CSUglobal.addAdmins(administrator)

# ==========   MAIN    ==========
print("\n --- Welcome to the School Registration System ---")
CSUglobal.start()
print("Have a nice day")








    #Ask for user login
# user = input("User:")
# pWord = input("Password:")

#     #Menu for Student or Admin
# if user == administrator.admin_ID and pWord == administrator.admin_Password:
#     name = administrator.getName()
#     print(f"Welcome Administrator {name}")
#     #TODO
#     #function for admin
#     #Exit Menu
    
# else:
#     print("No file was found!")