# Muhammad Haroon Nasir
# 06/09/25
# Problem 1: Use a for statement and random.randrange to print 10 random integers between 25 and 35

import random

# For loop with 10 iterations
for i in range(10):
    # Selects a random integer between 25 and 35. 36 is excluded
    num = random.randrange(25, 36)
    print(num)