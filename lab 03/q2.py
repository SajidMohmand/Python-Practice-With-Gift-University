'''Average Rainfall
Write a program that uses nested loops to collect data and calculate the average rainfall over a
period of years. The program should first ask for the number of years. The outer loop will iterate
once for each year. The inner loop will iterate twelve times, once for each month. Each iteration
of the inner loop will ask the user for the inches of rainfall for that month. After all iterations, the
program should display the number of months, the total inches of rainfall, and the average rainfall
per month for the entire period'''

def rainFallCal(years):

    total_inches = 0.0
    for year in range(years):
        for month in range(12):
            inches = float(input(f"Enter The inches of rainfall for month {month+1} : "))
            total_inches += inches
        
    return total_inches

years = int(input("Enter the no of years : "))
inches = rainFallCal(years)

print("Total Number of months : ",years*12)
print("Total inches of rainfall : ",inches)
print("The average rainfall per month for the entire period : ", round(inches/(years*12)))
