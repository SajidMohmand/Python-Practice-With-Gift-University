'''Population
Write a program that predicts the approximate size of a population of organisms. The application
should allow the user to enter the starting number of organisms, the average daily population
increase (as a percentage), and the number of days the organisms will be left to multiply. For
example, assume the user enters the following values:
Starting number of organisms: 2
Average daily increase: 30%
Number of days to multiply: 10
The program should display the following table of data:
Day Approximate Population
1 2
2 2.6
3 3.38
4 4.394
5 5.7122
6 7.42586
7 9.653619
8 12.5497
9 16.31462
10 21.209
'''

def populationCal(s,p,days):

    print("Days\tPopulation")

    sum = s
    for day in range(1,days+1):
        print(f"{day}\t{sum}")
        percentage = p/100 * sum
        sum += percentage

startUpNum = float(input("Starting number of organisms: "))
days = int(input("Number of days to multiply: "))
avg = float(input("Average daily increase: "))
populationCal(startUpNum,avg,days)