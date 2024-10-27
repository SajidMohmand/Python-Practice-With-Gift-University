''' Pennies for Pay
Write a program that calculates the amount of money a person would earn over a period of time
if his or her salary is one penny the first day, two pennies the second day, and continues to double
each day. The program should ask the user for the number of days. Display a table showing what
the salary was for each day, and then show the total pay at the end of the period. The output
should be displayed in a dollar amount, not the number of pennies'''

def penniesCal(days):

    print("\tDays\tSalary")
    sal = 1
    for day in range(1,days+1):
        print(f"\t{day}\t{sal}")
        sal = sal*2
    return sal

days = int(input("Enter total days : "))

tot_salary = penniesCal(days)
print(f"\tTotal\t{tot_salary}")