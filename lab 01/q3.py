'''Ingredient Adjuster
A cookie recipe calls for the following ingredients: * 1.5 cups of sugar * 1 cup of butter * 2.75 cups
of flour
The recipe produces 48 cookies with this amount of the ingredients. Write a program that asks
the user how many cookies he or she wants to make, and then displays the number of cups of each
ingredient needed for the specified number of cookies.'''

sugar_per_cookie = 1.5/48
butter_per_cookie = 1/48
flour_per_cookie = 2.75/48

user_cookie = float(input("Enter cookie in number: "))

print("Total cookie : ",user_cookie)
print("sugar needed : ",sugar_per_cookie*user_cookie)
print("butter needed : ",butter_per_cookie*user_cookie)
print("flour needed : ",flour_per_cookie*user_cookie)