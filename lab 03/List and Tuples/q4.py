'''Population Data
You are provided a dataset file named USPopulation.txt. The file contains the midyear population of the United States, in thousands, during the years 1950 through 1990. The first line in
the file contains the population for 1950, the second line contains the population for 1951, and so
forth.
Write a program that reads the file’s contents into a list. The program should display the following
data:
• The average annual change in population during the time period
• The year with the greatest increase in population during the time period
• The year with the smallest increase in population during the time period'''


def readFile(filename):

    with open(filename, 'r') as file:

        return [line.strip() for line in file.readlines()]


data = readFile('USPopulation.txt') 
data = [int(a) for a in data]

max_population = max(data)
min_population = min(data)
print('The average annual change in population : ',sum(data)/len(data))
print('The year with the greatest increase in population : ',max_population)
print('The year with the smallest increase in population : ',min_population)
