'''name="saniya"
id=20
def welcome():
    print("you are welcome to my team",name)
welcome()
class UserInfo:
    def putData(self):
        self.name=input("Enter your name")
        self.id=int(input("Enter your id"))
        self.salary=float(input("Enter your salary"))
    def display(self):
        print("UserName:",self.name)
        print("User Id:",self.id)
        print("User Salary:",self.salary)
obj=UserInfo()
obj.putData()
obj.display()'''
'''class Student:
    def __init__(self,name,age,grade):
        """
        initializes the student object.
        """
        self.name = name
        self.age = age
        self.grade = grade
    def display_info(self):
        """
        display the student's information.
        """
        print(f"Name: {self.name},age: {self.age}, Grade: {self.grade}")
        print("Nme:",self.name,"Age:",self.age)
#creating objects
student1 = Student("Alice",14,"9th")
student2 = Student("bob",15,"10th")

#Accessing object methods
student1.display_info()
student2.display_info()'''

#WAP to print bookdata as title,year,author,etc with class and object concept.
    
class book():
    def __init__(self,title,year,author):
        self.title = title
        self.year = year
        self.author = author
    def display_data(self):
        print(f"Title: {self.title},age: {self.year}, author: {self.author}")
book1= book("peer e kamil",2024,"umera ahmed")
book2= book("aabe hayat",2023,"nemra ahmed")

book1.display_data()
book2.display_data()
