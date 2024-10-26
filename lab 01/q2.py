'''Tip, Tax and Total
Write a program that calculates the total amount of a meal purchased at a restaurant. The program
should ask the user to enter the charge for the food, and then calculate the amount of a 18 percent
tip and 7 percent sales tax. Display each of these amounts and the total'''

charge_food = float(input("Enter charge for food : "))

tip = (18/100) * charge_food
sales_tx = (7/100) * charge_food

print("tip : ", tip)
print("sales tax : ",sales_tx)
