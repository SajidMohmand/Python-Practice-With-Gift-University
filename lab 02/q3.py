'''Miles Per Gallon
Drivers are concerned with the mileage obtained by their automobiles. One driver has kept track
of several tankfuls of gasoline by recording miles driven and gallons used for each tankful. Develop
a sentinel-controlled-repetition script that prompts the user to input the miles driven and gallons
used for each tankful. The script should calculate and display the miles per gallon obtained for
each tankful. After processing all input information, the script should calculate and display the
combined miles per gallon obtained for all tankfuls (that is, total miles driven divided by total
gallons used).
• Enter the gallons used (-1 to end): 12.8
• Enter the miles driven: 287
• The miles/gallon for this tank was 22.421875
• Enter the gallons used (-1 to end): 10.3
• Enter the miles driven: 200
• The miles/gallon for this tank was 19.417475
• Enter the gallons used (-1 to end): 5
• Enter the miles driven: 120
• The miles/gallon for this tank was 24.000000
• Enter the gallons used (-1 to end): -1
• The overall average miles/gallon was 21.601423'''


def helper():


    gallons = float(input("Enter the gallon use : "))
    miles = float(input("Enter the miles driven : "))

    miles_per_gallon = miles/gallons

    print("The miles/gallon for this tank was ",miles_per_gallon)


