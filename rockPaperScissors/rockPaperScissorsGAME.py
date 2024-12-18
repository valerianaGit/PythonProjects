# Randomisation and python lists 
import random
#import randomizer
print("Welcome to the Rock, Paper, Scissors Game!")
your_choice_int = input("Which do you choose? Type rock, Paper or Scissors.\n").lower() #returns a string
def rock_paper_scissors_func(your_choice_int):
    if your_choice_int == "rock":
        print(" Your choice was rock")
    elif your_choice_int == "paper":
        print("Your choice was paper")
    elif your_choice_int == "scissors":
        print("Your choice was scissors")
    else:
        print("That was not a choice, you silly bug, your input was " + your_choice_int)
random_int = random.randint(0, 2)
print("The computer chose " + str(random_int))
# who wins? 
# rock beats scissors, scissors beats paper, paper covers rock
def who_wins_algo(your_choice_int, random_int):
    if your_choice_int == 0 and random_int == 2:
        print(" You win Rock beats Scissors")
    if your_choice_int == 2 and random_int == 1:
        print(" You win scissors beats paper")
    if your_choice_int == 1 and random_int == 0:
        print(" You win paper covers rock")
#print(randomizer.favorite_number) => you can call from other files
rock_paper_scissors_func(your_choice_int)
who_wins_algo(your_choice_int, random_int)
#==================================================================================== Better option for code 

print("RELOADED Rock, Paper, Scissors Game!")
choices = ["rock", "paper", "scissors"]

def get_computer_choice():
    return random.choice(choices)

def get_user_choice():
    user_choice = input("Enter rock, paper, or scissors: ").lower()
    while user_choice not in choices:
        user_choice = input("Invalid choice. Please enter rock, paper, or scissors: ").lower()
    return user_choice

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    computer_choice = get_computer_choice()
    user_choice = get_user_choice()
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    print(determine_winner(user_choice, computer_choice))

if __name__ == "__main__":
    play_game()

