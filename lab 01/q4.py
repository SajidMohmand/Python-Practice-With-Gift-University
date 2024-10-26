'''Male and Female Percentages
Write a program that asks the user for the number of males and the number of females registered
in a class. The program should display the percentage of males and females in the class.
Hint: Suppose there are 8 males and 12 females in a class. There are 20 students in the class. The
percentage of males can be calculated as 8 4 20 5 0.4, or 40%. The percentage of females can be
calculated as 12 4 20 5 0.6, or 60%.'''

males = float(input("Enter number of males : "))
females = float(input("Enter number of females : "))

total_students = males + females
per_males = (males /total_students) * 100
per_females = (females /total_students) * 100

print("total students in class : ",total_students)
print("Percentage of males : ",per_males)
print("Percentage of females : ",per_females)
