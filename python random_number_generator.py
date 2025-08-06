import random

# Generate a random number between 1 and 100
number = random.randint(1, 100)

print(f"Your random number is: {number}")

# If number is above 90, show a lucky message
if number > 90:
    print(" This is your lucky number! ")
