# Muhammad Haroon Nasir
# 06/09/25
# Problem 3: Use random.choice to select a day of the week from a list and print that day

import random

# Initializes list with days of the week
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Select a random day
day = random.choice(days)

print(f"Randomly selected day: {day}")