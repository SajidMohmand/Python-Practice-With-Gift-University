'''
Cash Register
This exercise assumes that you have created the RetailItem class for Programming Exercise 2.
Create a CashRegister class that can be used with the RetailItem class. The CashRegister class
should be able to internally keep a list of RetailItem objects. The class should have the following
methods:
• A method named purchase_item that accepts a RetailItem object as an argument. Each
time the purchase_item method is called, the RetailItem object that is passed as an argument should be added to the list.
• A method named get_total that returns the total price of all the RetailItem objects stored
in the CashRegister object’s internal list.
8
• A method named show_items that displays data about the RetailItem objects stored in the
CashRegister object’s internal list.
• A method named clear that should clear the CashRegister object’s internal list.
Demonstrate the CashRegister class in a program that allows the user to select several items for
purchase. When the user is ready to check out, the program should display a list of all the items
he or she has selected for purchase, as well as the total price.
9.4 Employee and ProductionWorker Classes
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
the object and then use the object’s accessor methods to retrieve it and display it on the screen.
'''
class RetailItem:

    def __init__(self,item_desc,units_in, price):
        self.__item_desc = item_desc
        self.__units_in = units_in
        self.price = price


    def __str__(self):
        return "{}\t{}\t{}".format(self.__item_desc,self.__units_in,self.price)


class  CashRegister:

    def __init__(self):
        self.__retail_list = [RetailItem('Jacket',12,59.7)]

    def purchase_item(self,obj):
        list.append(obj)
    def get_total(self):

        total = sum(item.price for item in self.__retail_list)
        return total
    def show_items(self):
        if not self.__retail_list:
            print("!No item found")
            return
        for obj in self.__retail_list:
            print(obj)
    def clear(self):
        self.__retail_list.clear()



cr = CashRegister()
cr.show_items()
print(cr.get_total())
