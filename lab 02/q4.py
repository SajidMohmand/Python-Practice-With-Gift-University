'''Software Sales
A software company sells a package that retails for $99. Quantity discounts are given according to
the following table:
5
Quantity Discount
10–19 10%
20–49 20%
50–99 30%
100 or more 40%
Write a program that asks the user to enter the number of packages purchased. The program
should then display the amount of the discount (if any) and the total amount of the purchase after
the discount.'''



def helper(pkg):
    if pkg <= 19:
        return pkg*10/100
    elif pkg <= 49:
        return pkg*20/100
    elif pkg <= 99:
        return pkg*30/100
    elif pkg > 99:
        return pkg*40/100

pkg = int(input("Enter the number of packages purchased : "))
discount = helper(pkg)
actual_amount = pkg*99
total_amount = discount - actual_amount

print("Amount of discount : ",discount)
print("Amount After discount : ",total_amount)
