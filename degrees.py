# Muhammad Haroon Nasir
# 06/09/25
# Problem 5: A program to convert radians to degrees for a user inputted value. Prints user inputted value as well as the calculated value in degrees
# using the degrees function in the math module

import math

# Ask user for input
radians = float(input("Enter a value in radians: "))

# Convert to degrees
degrees = math.degrees(radians)

# Print results
print(f"Radians entered: {radians}")
print(f"Converted to degrees: {degrees}")