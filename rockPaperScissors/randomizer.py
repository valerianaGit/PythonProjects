favorite_number = 3.1456
import random
# heads or tails game based on a random number 
print("Welcome to the Heads or tails Game! ")
random_number = random.randint(1,2)
if random_number == 1:
    print("Heads" + " Your random number was 1")
elif random_number == 2:
    print("Tails" + " Your random number was 2")
#====================================================================================
states_of_america = ["Alabama", "Arkansas", "Alaska", "Delaware", "Connecticut"]
print(states_of_america[1])
print(states_of_america[-1])#start counting from the end of the list, using a negative integer
states_of_america[1] = "Georgia" #change the item at that index
states_of_america.append("Michigan")#add to the end of the list
#====================================================================================
# Randomize who will pay the bill 
list_of_friends = ["Branden", "Jimothy", "Karen", "Jordan Belfort"]
random_friend = random.randint(0,3)
print("the random friend is at index " + str(random_friend))
print(list_of_friends[random_friend])
#====================================================================================
# Randomize who will pay the bill 
random_friend_using_choice = random.choice(list_of_friends)
print(random_friend_using_choice)