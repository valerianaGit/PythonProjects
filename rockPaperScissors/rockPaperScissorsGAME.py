# Randomisation and python lists 
import random
import randomizer
print("Welcome to the Rock, Paper, Scissors Game!")
input("Which do you choose? Type 0 for rock, 1 for Paper or 2 for Scissors.\n")
random_integer = random.randint(0, 2)
print(random_integer)
print(randomizer.favorite_number)