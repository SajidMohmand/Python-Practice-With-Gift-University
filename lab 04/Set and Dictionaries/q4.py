''' Shopping Cart
In this exercise you are going to build a shopping cart using python dictionary.Create and initializes
an empty dict attribute named items.
Create a method add_item that requires item_name, quantity, price and total arguments. This
method should add the cost of the added items to the current value of total. It should also add
an entry to the items dict such that the key is the item_name and the value is the quantity of the
item.
Create a method remove_item that requires similar arguments as add_item. It should remove
items that have been added to the shopping cart and are not required. This method should deduct
the cost of the removed items from the current total and also update the items dict accordingly.
Create a method checkout that takes in cash_paid and returns the value of balance from the
payment. If cash_paid is not enough to cover the total, return “Cash paid not enough”.
'''

items = {}
total = 0

def add_item(name,quantity,price,total):
    total += quantity*price
    if name in items:
        items[name] = items[name]+quantity
    else:  
        items[name] = quantity

def remove_item(name,quantity,price,total):
    if name in items.keys():
        total -= quantity*price
        if total < 0:total=0

        q = items.get(name)
        q = q-quantity
        if q < 0:
            items.pop(name)
        else:
            items[name] = q

def checkOut(cash_paid):
    if cash_paid > total:
        cash_paid -= total
    else:
        print("!Cash paid not enough") 

    return cash_paid



add_item("pen",3,10,0)
# remove_item("pen",2,10,0)
print(items)
print(total)