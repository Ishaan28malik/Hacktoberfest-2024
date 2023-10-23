import random

def play_rock_paper_scissors():
  """Plays a game of rock paper scissors.

  Returns:
    A string indicating the winner of the game, or "Tie" if the game is a tie.
  """

  # Get the user's choice.
  user_choice = input("Rock, paper, or scissors? ")

  # Validate the user's choice.
  if user_choice not in ["rock", "paper", "scissors"]:
    raise ValueError("Invalid choice.")

  # Generate the computer's choice.
  computer_choice = random.choice(["rock", "paper", "scissors"])

  # Determine the winner.
  if user_choice == computer_choice:
    return "Tie"
  elif user_choice == "rock" and computer_choice == "scissors":
    return "You win!"
  elif user_choice == "paper" and computer_choice == "rock":
    return "You win!"
  elif user_choice == "scissors" and computer_choice == "paper":
    return "You win!"
  else:
    return "Computer wins!"


# Play the game.
winner = play_rock_paper_scissors()

# Print the winner.
print(winner)
