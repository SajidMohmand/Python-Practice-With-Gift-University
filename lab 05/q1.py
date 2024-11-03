'''9.1 Employee Class
Write a class named Employee that holds the following data about an employee in attributes: name,
ID number, department, and job title.
Once you have written the class, write a program that creates three Employee objects to hold the
following data:
Name ID Number Department Job Title
Susan Meyers 47899 Accounting Vice President
Mark Jones 39119 IT Programmer
Joy Rogers 81774 Manufacturing Engineer
he program should store this data in the three objects and then display the data for each employee
on the screen.'''

class Employee:

    def __init__(self,name,id,dept,job):
        self.__name = name
        self.__id = id
        self.__dept = dept
        self.__job = job
    
    def __str__(self):
        return "{}\t{}\t{}\t{}".format(self.__name,self.__id,self.__dept,self.__job)
    

emp1 = Employee('Susan Meyers', 47899,'Accounting','Vice President')
emp2 = Employee('Mark Jones', 39119,'IT','Programmer')
emp3 = Employee('Joy Rogers', 81774,'Manufacturing','Engineer')

print("Name\tID\tDepartment\tJob Title")
print(emp1)
print(emp2)
print(emp3)