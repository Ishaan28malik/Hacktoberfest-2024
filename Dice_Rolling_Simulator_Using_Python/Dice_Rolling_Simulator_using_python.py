import random

def roll_dice():
    return random.randint(1, 6)

def main():
    while True:
        try:
            num_rolls = int(input("How many times would you like to roll the dice? "))
            if num_rolls <= 0:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    for _ in range(num_rolls):
        result = roll_dice()
        print(f"You rolled a {result}")

if __name__ == "__main__":
    main()