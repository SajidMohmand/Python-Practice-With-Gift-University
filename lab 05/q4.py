''' Person and Customer Classes
Write a class named Person with data attributes for a person’s name, address, and telephone
number. Next, write a class named Customer that is a subclass of the Person class. The Customer
class should have a data attribute for a customer number and a Boolean data attribute indicating
whether the customer wishes to be on a mailing list. Demonstrate an instance of the Customer
class in a simple program.'''


class Person:

    def __init__(self,name,address,telephone):
        self.__name = name
        self.__address = address
        self.__telephone = telephone

    def set_name(self,name):
        self.__name = name
    def set_address(self,address):
        self.__address = address
    def set_telephone(self,telephone):
        self.__telephone = telephone
    
    def get_name(self):
        return self.__name
    def get_address(self):
        return self.__address
    def get_telephone(self):
        return self.__telephone
    

class Customer(Person):

    def __init__(self,name,address,telephone,customer_no,wish):
    
        Person.__init__(self,name,address,telephone)
        self.__customer_no = customer_no
        self.__wish = wish
    
    def get_cusNo(self):
        return self.__customer_no
    def get_wish(self):
        return self.__wish
    
    def set_cusNo(self,cusNo):
        self.__customer_no = cusNo
    def set_wish(self,wish):
        self.__wish = wish
    

c1 = Customer("sajid","Gujranwala Pakisan","03*********",2114,True)



print("Customer name : ",c1.get_name())
print("Customer address : ",c1.get_address())
print("Customer telephone : ",c1.get_telephone())
print("Customer customer no : ",c1.get_cusNo())
print("Customer wish : ",c1.get_wish())



