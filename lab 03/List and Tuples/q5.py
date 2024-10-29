''' World Series Champions
You are given a dataset file named WorldSeriesWinners.txt. This file contains a chronological
list of the World Series winning teams from 1903 through 2009. (The first line in the file is the
name of the team that won in 1903, and the last line is the name of the team that won in 2009.
Note that the World Series was not played in 1904 or 1994.) Write a program that lets the user
enter the name of a team and then displays the number of times that team has won the World
Series in the time period from 1903 through 2009.
'''

def laodData(filename):

    with open(filename, 'r') as file:
        return [line.strip() for line in file.readlines()]
    

x = input("Enter team name : ")

teams = laodData("WorldSeriesWinners.txt")

print("Number of times that team has won the World : ",teams.count(x))
    
