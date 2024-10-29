'''Lo Shu Magic Square
The Lo Shu Magic Square is a grid with 3 rows and 3 columns. The Lo Shu Magic Square has the
following properties:
6
• The grid contains the numbers 1 through 9 exactly.
• The sum of each row, each column, and each diagonal all add up to the same number.
In a program you can simulate a magic square using a two-dimensional list. Write a function that
accepts a two-dimensional list as an argument and determines whether the list is a Lo Shu Magic
Square. Test the function in a program'''

def checkLoShuMagicSquare(square):
    nums = [num for row in square for num in row]  # Flatten the 2D list
    if sorted(nums) != list(range(1, 10)):
        return False

    magic_sum = sum(square[0])

    for row in square:
        if sum(row) != magic_sum:
            return False

    for col in range(3):
        if sum(square[row][col] for row in range(3)) != magic_sum:
            return False

    if sum(square[i][i] for i in range(3)) != magic_sum:
        return False

    if sum(square[i][2 - i] for i in range(3)) != magic_sum:
        return False

    return True


sqa = [[4,9,2],[3,5,7],[8,1,6]]
print(checkLoShuMagicSquare(sqa))