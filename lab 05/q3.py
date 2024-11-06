'''Employee and ProductionWorker Classes
Write an Employee class that keeps data attributes for the following pieces of information: *
Employee name * Employee number
Next, write a class named ProductionWorker that is a subclass of the Employee class. The ProductionWorker class should keep data attributes for the following information:
• Shift number (an integer, such as 1, 2, or 3)
• Hourly pay rate
The workday is divided into two shifts: day and night. The shift attribute will hold an integer
value representing the shift that the employee works. The day shift is shift 1 and the night shift is
shift 2. Write the appropriate accessor and mutator methods for each class.
Once you have written the classes, write a program that creates an object of the ProductionWorker
class and prompts the user to enter data for each of the object’s data attributes. Store the data in
the object and then use the object’s accessor methods to retrieve it and display it on the screen'''


class Employee:
    def __init__(self, emp_name, emp_no):
        self.__emp_name = emp_name
        self.__emp_no = emp_no

    # Accessor (getter) methods for Employee
    def get_emp_name(self):
        return self.__emp_name

    def get_emp_no(self):
        return self.__emp_no

    # Mutator (setter) methods for Employee
    def set_emp_name(self, emp_name):
        self.__emp_name = emp_name

    def set_emp_no(self, emp_no):
        self.__emp_no = emp_no


class ProductionWorker(Employee):
    def __init__(self, shift_num, hourly_per_rate, name, no):
        super().__init__(name, no)
        self.__shift_num = shift_num
        self.__hourly_per_rate = hourly_per_rate

    # Accessor (getter) methods for ProductionWorker
    def get_shift_num(self):
        return self.__shift_num

    def get_hourly_per_rate(self):
        return self.__hourly_per_rate

    # Mutator (setter) methods for ProductionWorker
    def set_shift_num(self, shift_num):
        self.__shift_num = shift_num

    def set_hourly_per_rate(self, hourly_per_rate):
        self.__hourly_per_rate = hourly_per_rate




pw1 = ProductionWorker(1,40,"sajid",211370213)


print("Employee name : ",pw1.get_emp_name())
print("Employee Number : ",pw1.get_emp_no())
print("Employee hourly per rate : ",pw1.get_hourly_per_rate())
print("Employee Shift Number : ",pw1.get_shift_num())