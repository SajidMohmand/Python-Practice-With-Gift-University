'''Rainfall Statistics
Design a program that lets the user enter the total rainfall for each of 12 months into a list. The
program should calculate and display the total rainfall for the year, the average monthly rainfall,
and the months with the highest and lowest amounts.'''

def fillarray():
    list = []

    for i in range(1,13):
        list.append(int(input(f"Enter {i} month rainfall : ")))
    return list

print(fillarray())
