'''Budget Analysis
Write a program that asks the user to enter the amount that he or she has budgeted for a month.
A loop should then prompt the user to enter each of his or her expenses for the month and keep
a running total. When the loop finishes, the program should display the amount that the user is
over or under budget.'''


def helper(budget):
    total = 0
    exp = int(input("Enter expense no 1 (press -1 to exit)"))
    count = 2

    while exp != -1:
        total += exp
        exp = int(input(f"Enter expense no {count} (press -1 to exit) : "))
        count +=1


    return total

budget = int(input("Enter the amount that he or she has budgeted for a month : "))
tot = helper(budget)

print("Budget he/she have : ",budget)
print("Total Expenses : ",tot)
if tot <= budget:
    print("Amount is under budget.")
else:
     print("Amount is over budget.")

