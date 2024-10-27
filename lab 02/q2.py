# Hot Dogs Cookout Calculator
# Assume that hot dogs come in packages of 10, and hot dog buns come in packages of 8. Write a
# program that calculates the number of packages of hot dogs and the number of packages of hot dog
# buns needed for a cookout, with the minimum amount of leftovers. The program should ask the
# user for the number of people attending the cookout and the number of hot dogs each person will
# be given. The program should display the following details: * The minimum number of packages
# of hot dogs required * The minimum number of packages of hot dog buns required * The number
# of hot dogs that will be left over * The number of hot dog buns that will be left over

import math


def hotdog_calculator(num_people,hot_dogs_per_person):
    
    total_hot_dogs = num_people * hot_dogs_per_person

    hot_dogs_per_package = 10
    buns_per_package = 8

    packages_hot_dogs = math.ceil(total_hot_dogs / hot_dogs_per_package)
    packages_buns = math.ceil(total_hot_dogs / buns_per_package)

    leftover_hot_dogs = (packages_hot_dogs * hot_dogs_per_package) - total_hot_dogs
    leftover_buns = (packages_buns * buns_per_package) - total_hot_dogs

    print(f"\nMinimum number of packages of hot dogs required: {packages_hot_dogs}")
    print(f"Minimum number of packages of hot dog buns required: {packages_buns}")
    print(f"Number of leftover hot dogs: {leftover_hot_dogs}")
    print(f"Number of leftover hot dog buns: {leftover_buns}")



num_people = int(input("Enter the number of people attending the cookout: "))
hot_dogs_per_person = int(input("Enter the number of hot dogs each person will be given: "))
hotdog_calculator(num_people,hot_dogs_per_person)


