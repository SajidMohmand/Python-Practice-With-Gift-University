'''9.1 Sum of Digits in a String
Write a program that asks the user to enter a series of single-digit numbers with nothing separating
them. The program should display the sum of all the single digit numbers in the string. For
example, if the user enters 2514, the method should return 12, which is the sum of 2, 5, 1, and 4.'''

def sum(str):
    if str.isdigit():
        sum = 0
        for c in str:
            sum += int(c)
        return sum
    return "!invalid input"





str = "2514"
print(sum(str))