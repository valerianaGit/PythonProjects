favorite_number = 3.1456
import random
# heads or tails game based on a random number 
print("Welcome to the Heads or tails Game! ")
random_number = random.randint(1,2)
if random_number == 1:
    print("Heads" + " Your random number was 1")
elif random_number == 2:
    print("Tails" + " Your random number was 2")