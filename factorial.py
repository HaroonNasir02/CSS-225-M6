# Muhammad Haroon Nasir
# 06/09/25
# Problem 6: Uses a for statement to calculate the factorial of a user input value. Prints the for loop calculation
# as well as the calculated value using the factorial function in the math module

import math

# Ask user for input
n = int(input("Enter a number: "))

# Calculate factorial using a for loop
fact = 1
for i in range(1, n + 1):
    fact *= i

# Calculate factorial using math module
math_fact = math.factorial(n)

# Print results
print(f"Factorial (calculated with loop): {fact}")
print(f"Factorial (using math.factorial): {math_fact}")