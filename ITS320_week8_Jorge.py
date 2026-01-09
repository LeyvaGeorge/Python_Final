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
    def removeCourse(self,course_to_remove):
        if isinstance(course_to_remove, Course):
            try:
                self.courses.remove(course_to_remove)
            except:
                print("Fix removeCourse() to remove a valid course")
        else:
            print("Error: You can only remove a valid Course object. ")
        

    def printCourses(self):
        for index in self.courses:
            print(f"Title:{index.title}")
            print(f"ID:{index.id}")
            print(f"Credit:{index.credit}")
            print(f"Capacity:{index.capacity}")
            print(f"Description:{index.description}")
    
    def findcourse(self):
        while True:
            print("1. Search by Title")
            print("2. Search by ID")
            ans = input("Input: ")
            if ans == '1':
                ans = input("Title: ")
                for index in self.courses:
                    if ans == index.title:
                        return index
                print("Did not find course by Title")
                return None
            elif ans == '2':
                ans = input("ID: ")
                for index in self.courses:
                    if ans == index.id:
                        return index
                print("Did not find Course by Index")
                return None
            else:
                print("Must be either 1 or 2")

    def editCourse(self, singleCourse: type[Course] ):
        if not singleCourse:
            print("the argument was empty")
            raise Exception ("The course was empty or None. In editCourse()")
        while True:
            print("Choose what to change:")
            print("1.Title")
            print("2.ID")
            print("3. Credit")
            print("4. Capacity")
            print("5. Description")
            print("6. Back")
            ans = input("Input:")
            if ans == '1':
                ans = input("New Title: ")
                singleCourse.title = ans
                break
            elif ans == '2':
                ans = input("New ID: ")
                singleCourse.id = ans
                break
            elif ans == '3':
                ans = int(input("New Credit: "))
                singleCourse.credit = ans
                break
            elif ans == '4':
                ans = int(input("New Capacity: "))
                singleCourse.capacity = ans
                break
            elif ans == '5':
                ans = input("New Description")
                singleCourse.description = ans
                break
            elif  ans == '6':
                break
            else:
                print("The input was not valid")

    def printCourse(self,singleCourse : type[Course]):
        if not singleCourse:
            print("The argument was empty")
            raise Exception ('The course was empty or None. in printCourse()')
        print(f"Title: {singleCourse.title}")
        print(f"ID:{singleCourse.id}")
        print(f"Credit:{singleCourse.credit}")
        print(f"Capacity:{singleCourse.capacity}")
        print(f"Description:{singleCourse.description}")

    #Prints all the student in the course
    def printStudentsCourse(self):
        courseId = input("Course ID: ")             #Get course ID
        for index in self.courses:                  #Loops in courses
            if courseId == index.id:                #Matches courses to typed in course
                self.printCourse(index)             #Prints current course
                print("The Number of student in", courseId , "of this ",len(index.stuID)) 
                for i in range(len(index.stuID)):   #checks the length of course's students registered
                    for names in self.students:     #Loops in Students
                        if names.id == index.stuID[i]:          #matches Student to course's student registered list
                            print(f"Name: {names.getName()}")   #prints out Student Name
                    print(f"ID: {index.stuID[i]}")              #Prints out student ID
                    #length of studId print name and ID
    
    def printCoursesforStudent(self):
        #Find Student
        studentIdentification = input("Student ID: ")
        for i in range(len(self.students)):
            if studentIdentification == self.students[i].get_id():
                for courseName in self.students[i].registered_course:
                    for indexCourse in self.courses:
                        if courseName == indexCourse.id:
                            print(f"Title: {indexCourse.title}")
                            print(f"ID: {indexCourse.id}")
                    
                break
        #Print Courses that they are enrolled in
        
    #Prints all of students information
    def printStu(self):
        for i in range(len(self.students)):
            print("\nName: ",self.students[i].getName())
            print("ID: ", self.students[i].get_id())
            print("Password: ", self.students[i].get_password())
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
                
                self.admin_menu(director)
                return director
        for learner in self.students:
            if user_id == learner.id:
                print("found student exit out around line 178")
                self.student_menu(learner)
                return learner
        else:
            print("Invalid Password")
            return None
    
    def admin_menu(self,admin: type[Admin]):
        while True:
            print(f"\n {admin.getName()} Admin Menu")
            print("1. Add new Course")
            print("2. Remove Course")
            print("3. Update Course details")
            print("4. Search for course")
            print("5. List all Courses")
            print("6. List all students registerd for a specific course")
            print("7. List all Courses for a specific Student")
            print("8. List all student IDs and Password")
            print("9. Exit")
            choice = input("select an option: ")

            #Adds a new course to courses attributes
            if choice == '1':
                print("\nAdding New Course")
                newTitle = input("Title: ")
                newID = input("ID: ")
                newCredit = int(input("Credit: "))
                newCapacity = int(input("Capacity: "))
                newDescription = input("Description: ")

                newCourse = Course(newTitle,newID,newCredit,newCapacity,newDescription)
                self.addCourse(newCourse)
                print("New Course was added")
            #Removes course based of ID
            elif choice == '2':
                print("Removing an Existing Course")
                unwanted = input("ID: ")
                for index in self.courses:
                    if index.id == unwanted:
                        self.removeCourse(index)
            #Update course information Title, ID, capacity, description
            elif choice == '3':
                print("Updating course information.")
                foundCourse = self.findcourse()
                self.editCourse(foundCourse)
            #Searchs courses by ID or Title
            elif choice == '4':
                print("Finding course.") 
                courseInfo = self.findcourse()  #finds course
                self.printCourse(courseInfo)    #prints course information
                
            #Prints out all Courses
            elif choice == '5':
                print("Print all Courses")
                self.printCourses()
            #List all students for a specific course
            elif choice == '6':
                print("Students in course")
                self.printStudentsCourse()      #prints students in course
            elif choice == '7':
                print("Student Courses")
                self.printCoursesforStudent()
            #Prints all students Name, ID, Password
            elif choice == '8':
                print("Priting all Student information")
                self.printStu()
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

    #Checks to see if capacity is full
    def has_space(self):
        return len(self.stuID) < self.capacity
    
    def add_student(self, student_ID):
        if self.has_space():
            self.stuID.append(student_ID)
            self.capacity -= 1
            return True #needed for Course to add to check that it was added onto course
        return False
    
    def has_student(self, student_ID):
        #Checks to see if student is in this course
        pass

    def remove_student(self, student_ID):
        #Must remove student from current course if match +1 to capacity
        pass

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

    def get_password(self):
        return self.password
    def get_id(self):
        return self.id
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

    def register_for_course(self, course : type[Course]):
        if course.add_student(self.id):
            self.registered_course.append(course.id)
            print(f"{self.getName()} successfully registered for {course.title}")
        else:
            print(f"Registration failed: {course.title} is full.")

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
#Adding george to IntroArt and Calculus
CSUglobal.students[0].register_for_course(CSUglobal.courses[0])
CSUglobal.students[0].register_for_course(CSUglobal.courses[3])
CSUglobal.students[1].register_for_course(CSUglobal.courses[0])
# ==========   MAIN    ==========
print("\n --- Welcome to the School Registration System ---")
CSUglobal.start()
print("Have a nice day.")









