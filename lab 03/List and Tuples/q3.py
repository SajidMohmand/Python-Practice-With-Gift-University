'''Name Search
You are provided two dataset files:
• GirlNames.txt—This file contains a list of the 200 most popular names given to girls born
in the United States from the year 2000 through 2009.
• BoyNames.txt—This file contains a list of the 200 most popular names given to boys born
in the United States from the year 2000 through 2009.
Write a program that reads the contents of the two files into two separate lists. The user should
be able to enter a boy’s name, a girl’s name, or both, and the application will display messages
indicating whether the names were among the most popular.'''


def load_names(filename):
    """Load names from a given file and return as a list."""
    with open(filename, 'r') as file:
        return [line.strip() for line in file.readlines()]

girl_names = load_names('GirlNames.txt')
boy_names = load_names('BoyNames.txt')

girl_name_input = input("Enter a girl's name (or leave blank if none): ").strip()
boy_name_input = input("Enter a boy's name (or leave blank if none): ").strip()

if girl_name_input:
    if girl_name_input in girl_names:
        print(f"{girl_name_input} is among the most popular girl names.")
    else:
        print(f"{girl_name_input} is NOT among the most popular girl names.")
    
if boy_name_input:
    if boy_name_input in boy_names:
        print(f"{boy_name_input} is among the most popular boy names.")
    else:
        print(f"{boy_name_input} is NOT among the most popular boy names.")


