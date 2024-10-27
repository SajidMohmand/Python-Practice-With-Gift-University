''' Ocean Level
Assuming the ocean’s level is currently rising at about 1.6 millimeters per year, create an application
that displays the number of millimeters that the ocean will have risen each year for the next 25
years'''

# Define the rise rate of the ocean level in millimeters per year
rise_rate_per_year = 1.6
years = 25

print("Year\tOcean Level Rise (mm)")
print("-----------------------------")

# Loop through each year from 1 to 25
for year in range(1, years + 1):
    # Calculate the total rise for each year
    rise = rise_rate_per_year * year
    # Display the year and corresponding ocean level rise
    print(f"{year}\t{rise:.2f} mm")
