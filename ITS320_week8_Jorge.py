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
        self.admins: list[Admin] = []   #This is the admins for the School Registration System, that is of class Admin
        self.students: list[Student] = []
        self.courses: list[Course] = []
    
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
    #This is for understanding ++++++++++++++++++++++++++++++
    def addCourseAction(self,user):
        #check if user has permission
        if not user.has_permission("add_course"):
            print("Access denined")
            return
        #TODO enter the course to append onto this
        self.courses.append(course)
        print("Appended to courses -Delete this.")

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

    def login(self): #Identifies if it is user or admin
        user_id = input ("Enter ID: ")
        password = input("Enter Password: ") #TODO must finish the password matches the user id
        #TODO must find a way to implement on how to look for user_id in self.admins and students
        for director in self.admins:
            if user_id == director.id:
                print("found exit out")
                self.admin_menu(director)
                return director
        for learner in self.students:
            if user_id == learner.id:
                print("found student exit out")
                self.student_menu(learner)
                return learner
        else:
            print("Invalid Password")
            return None
    
    def admin_menu(self,admin: type[Admin]):
        while True:
            print("1. Add new Course")
            print("2. Remove Course")
            print("3. Update Course details")
            print("4. Search for courses by Title or Course ID")
            print("5. List all Courses")
            print("6. List all students registerd for a specific course")
            print("7. List all Courses for a specific Student")
            print("8. List all student IDs and Password")
            print("9. Exit")
            choice = input("select an option: ")

            if choice == '1':
                print("TODO")
            elif choice == '2':
                print("TODO")
            elif choice == '3':
                print("TODO")
            elif choice == '4':
                print("TODO")
            elif choice == '5':
                print("TODO")
            elif choice == '6':
                print("TODO")
            elif choice == '7':
                print("TODO")
            elif choice == '8':
                print("TODO")
            elif choice == '9':
                break
            else:
                print("Invalid choice, Please try again.")
        print("Leaving the admin menu")

    def student_menu(self,user: type[Student]):
        while True:
            print("1. Register for Course")
            print("2. Drop Course")
            print("3. List all Courses")
            print("4. List all Enrolled Courses")
            print("5. Exit")
            choice = input("select an option: ")

            if choice == '1':
                print("TODO")
            elif choice == '2':
                print("TODO")
            elif choice == '3':
                print("TODO")
            elif choice == '4':
                print("TODO")
            elif choice == '5':
                break
            else:
                print("Invalid choice, Please try again.")        
        print("Leaving the student Menu")

class Course:
    def __init__(self, ti, id, cr, ca, desc):
        self.title = ti
        self.id = id
        self.credit = cr 
        self.capacity = ca
        self.description = desc
        self.stuID = [] #adds id to see who is enrolled

class Permissions:
    ADD_COURSE = "add_course"
    REMOVE_COURSE = "remove_course"
    VIEW_COURSE = "view_course"
    ENROLL_COURSE = "enroll_course"

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

class User(Person):
    def __init__(self,fName,lName,ID,pWord):
        Person.__init__(self,fName, lName)
        self.id = ID
        self.password = pWord
        self.permissions = set()

    def has_permission(self, permission):
        return permission in self.permissions    

class Admin(User):
    def __init__(self,fname,lname,ID, pWord):
        User.__init__(self,fname,lname,ID, pWord)
        self.permissions.update({
            Permissions.ADD_COURSE,
            Permissions.REMOVE_COURSE,
            Permissions.VIEW_COURSE
        })

class Student(User):
    def __init__(self,fname,lname,ID, pWord):
        User.__init__(self,fname,lname,ID,pWord)
        self.permissions.update({
            Permissions.VIEW_COURSE,
            Permissions.ENROLL_COURSE
        })
        self.registered_course = []

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
    ("George","Leyva","12345","98765"),
    ("Liam","Smith","LiaSm95","owU9-A3WD"),
    ("Olivia","Taylor","OliTa01","25le-C87z"),
    ("Oliver","White","OliWh05","0glu-zi1D"),
    ("Valerie","Gomez","EmiLe02","vcnJ-Gl98"),
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
print("Have a nice day.")









