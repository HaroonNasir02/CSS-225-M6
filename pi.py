# Muhammad Haroon Nasir
# 06/09/25
# Problem 4: A program to compute the approximation of pi and then print that value as well as the value of math.pi from the math module

import math

# Number of terms in the approximation of pi. Increase for higher accuracy
terms = 10000

pi = 0

# For loop that adds each term to our approximation
for k in range(terms):
    # (-1) ** k) alternates between 1 and -1, since the series adds a term then subtracts a term and alternate like that
    pi += ((-1) ** k) / (2 * k + 1)

pi *= 4  # multiply series sum by 4

# Print both values
print(f"Approximation of pi: {pi}")
print(f"Value of math.pi: {math.pi}")