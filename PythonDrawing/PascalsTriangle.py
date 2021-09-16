# Creating Digital Representation of Pascal's Triangle
from math import factorial
# User input to determine number of rows of Pascal's Triangle
row_count = int(input("How many rows of Pascal's Triangle do you want to print out: "))

# For loops to create drawing
for i in range(row_count):
    # Creating Spacing
    for j in range(row_count-i+1):
        print(end=" ")

    # Calculating Triangle Values
    for j in range(i+1):
        # Double front slash is equivalent to flooring a dividend
        print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")

    # Creating new line
    print()
