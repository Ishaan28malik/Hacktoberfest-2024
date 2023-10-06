import random

def get_user_choice():
    """Get user choice and validate it."""
    while True:
        user_choice = input("Enter 'r' for Rock, 'p' for Paper, or 's' for Scissors: ").lower()
        if user_choice in ['r', 'p', 's']:
            if user_choice == 'r':
                return 'rock'
            elif user_choice == 'p':
                return 'paper'
            else:
                return 'scissors'
        else:
            print("Invalid choice. Please enter 'r' for Rock, 'p' for Paper, or 's' for Scissors.")

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    return computer_choice

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    print("Welcome to Rock-Paper-Scissors game!")
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        print(determine_winner(user_choice, computer_choice))
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
