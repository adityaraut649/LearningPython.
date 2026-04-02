# Python program to demonstrate Inheritance

# Employee Class
class Employee:
 
   
    def __init__(self, empname, emppage, empsalary, emprole):
        self.empname = empname
        self.emppage = emppage
        self.empsalary = empsalary
        self.emprole = emprole

    
    def display(self):
        print(f"Name: {self.empname}")
        print(f"Page: {self.emppage}")
        print(f"Salary: {self.empsalary}")
        print(f"Role: {self.emprole}")

    def work(self):
        print(f"Working: {self.empname}")


    def project(self , projectname):
        print(f"Project: {self.empname} is working on {projectname}")


# Developer Class
class Developer(Employee):

    def  work(self):
        print("Develoer is working")


    def project(self, projectname):
        print(f"Developer is working on {projectname}")


# QA Class
class QA(Employee):


    def work(self):
        print("QA is working")

    def project(self, projectname):
        print(f"QA is working on {projectname}")



# Creating Objects
dev = Developer("Dev1", "Dev Page", 10000, "Developer")
QA1 = QA("QA1", "QA Page", 10000, "QA")

# Calling Methods
print("----------------")
dev.display()
dev.work()
dev.project("Project1")


print("----------------")
QA1.display()
QA1.work()
QA1.project("Project1")
