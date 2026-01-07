#Student Course Registration System
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
class Course:
    def __init__(self,title,id,credit,capacity,description):
        self.title 
        self.id 
        self.credit 
        self.capacity
        self.description

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
    def __init__(self,fname,lname):
        Person.__init__(self,fname,lname)
        self.user_name
        self.password
        self.reg_course = []

# ========== FUNCTION  ==========
# ==========   SETUP   ==========
class_list = []
catalog = [
    ("Intro Art","AR100",3, 30,"Develop skiils to successfully draw the human form." ),
    ("English 101","EN101",3, 25,"Students receive instruction in academic reading and writing, including writing processes, effective use of language, analytical thinking, and the foundations of academic research."),
    ("Algebra","MA105",3, 30,"This course covers graphing of polynomial, rational and transcendental functions." ),
    ("Calculus","MA135",3, 25,"This course covers functions and their graphs, including exponential and logarithmic functions."),
    ("Anatomy & Physiology","AP102",5,20,"This course is the first in a two part series covering the topics of the chemical, cellular, and tissue levels of organization"),
    ("Beginning Guitar","MU054",1, 5,"This course offers individual guitar instruction to students who have little or no previous training.")
]
students = [
    ("Liam","Smith","LiaSm95","owU9-A3WD",[]),
    ("Olivia","Taylor","OliTa01","25le-C87z",[]),
    ("Oliver","White","OliWh05","0glu-zi1D",[]),
    ("Emily","Leyva","EmiLe02","vcnJ-Gl98",[]),
    ("Levi","Clark","LevCl90","WZ7o-n5QJ",[]),
    ("Isabella","Ferrero","IsaFe03","SDg9-DT9l",[]),
    ("William","Young","WilYo97","J38D-NXN3",[]),
    ("Ava","King","AvaKi99","QX1I-sswP",[]),
    ("James","Green","JamGr06","4b9Y-beOD",[]),
    ("Sofia","Collins","SofCo02","yxam-Iy1u",[])
]

#Creates and Administrator with ID and password
administrator = Admin("Renee","Carroll","admin","password")

# ==========   MAIN    ==========
print("Welcome to the Registration System")
    #Ask for user login
user = input("User:")
pWord = input("Password:")

print(f"User : {user}\nPassword:{pWord}")
    #Menu for Student or Admin
print(f"{administrator.getName()}")
if user == administrator.admin_ID and pWord == administrator.admin_Password:
    name = administrator.getName()
    print(f"Welcome Administrator {name}")
    #Exit Menu
print("Have a nice day")