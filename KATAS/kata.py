#==================================================================================== if else, while, 
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

#==================================================================================== 
#inputs, strings to ints , and compare some choices in if else statements 
import random

print("Welcome to Python Pizza! Let's work out the bill for your order")
pizza_size_input = input("Size of your pizza? Enter small, medium, or large \n").lower()
print("size input was " + pizza_size_input)

def pizza_size_price_func(size):
    if size == "small":
        return 15
    elif size == "medium":
        return 20
    else:
        return 25

pizza_size_price = pizza_size_price_func(pizza_size_input)
pepperoni_yes_or_no = input("Would you like pepperoni with that? Type yes or no \n").lower()

def pepperoni_price_function(pepperoni_choice, size):
    if size == "small":
        return 2 if pepperoni_choice in ["yes", "y"] else 0
    else:
        return 3 if pepperoni_choice in ["yes", "y"] else 0

pepperoni_upcharge = pepperoni_price_function(pepperoni_yes_or_no, pizza_size_input)
cheese_yes_or_no = input("Add cheese? Type yes or no \n").lower()

def cheese_price_function(cheese_choice):
    return 1 if cheese_choice in ["yes", "y"] else 0

cheese_upcharge = cheese_price_function(cheese_yes_or_no)

print("Pizza size cost is " + str(pizza_size_price))
print("Pepperoni upcharge " + str(pepperoni_upcharge))
print("Cheese upcharge " + str(cheese_upcharge))
pizza_price = str(pizza_size_price + pepperoni_upcharge + cheese_upcharge)
print("Your bill is $" + pizza_price)
