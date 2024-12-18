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