"""Sales Tax
Write a program that will ask the user to enter the amount of a purchase. The program should then
compute the state and county sales tax. Assume the state sales tax is 5 percent and the county
sales tax is 2.5 percent. The program should display the following: * The amount of the purchase
* The state sales tax * The county sales tax * The total sales tax * and the total of the sale (which
is the sum of the amount of purchase plus the total sales tax)."""

a_purchase = float(input("Enter amount of purchase: "))

state_sales_tax = (5/100) * a_purchase
county_sales_tax = (2.5/100) * a_purchase

print("the amount of purchase: ",a_purchase)
print("the state sales tax : ", state_sales_tax)
print("The county sales tax : ", county_sales_tax)
print("Total sales tax : ",state_sales_tax+county_sales_tax)
print("The total of the sales: ",(state_sales_tax+county_sales_tax)+a_purchase)