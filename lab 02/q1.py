'''Mass and Weight
Scientists measure an object’s mass in kilograms and its weight in newtons. If you know the amount
of mass of an object in kilograms, you can calculate its weight in newtons with the following formula:
**
weight = mass * 3 9.8
** Write a program that asks the user to enter an object’s mass, and then calculates its weight. If
the object weighs more than 500 newtons, display a message indicating that it is too heavy. If the
object weighs less than 100 newtons, display a message indicating that it is too light.'''

def weightCalculator(mass):
    weight = mass * 39.8

    if weight > 500:
        print("too heavy")
    elif weight < 100:
        print("too light")
    else:
        print("you fit bro...")


a = float(input("Enter an object mass: "))

weightCalculator(a)
