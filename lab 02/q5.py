'''Shipping Charges
The Fast Freight Shipping Company charges the following rates:
Weight of Package Rate per Pound (Dollar)
2 pounds or less 1.50
Over 2 pounds but not more than 6 pounds 3.00
Over 6 pounds but not more than 10 pounds 4.00
Over 10 pounds 4.75
Write a program that asks the user to enter the weight of a package and then displays the shipping
charges'''


def helper(p):
    if p < 0:
        return "!invalid input"

    if p <= 2:
        return p*1.50
    elif p <=6:
        return p*3
    elif p <=10:
        return p*4
    else:
        return p*4.75
    
         

pounds = float(input("Enter the weight of a package : "))

charges = helper(pounds)
print("Shipping charges : ",charges)