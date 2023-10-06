import random


# Function to determine the round winner
def determine_round_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
            (user_choice == "scissors" and computer_choice == "paper") or \
            (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"


# Function to display the result and update scores
def display_result(user_choice, computer_choice, result, user_score, computer_score):
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    if result == "user":
        print("You win this round!")
        user_score += 1
    elif result == "computer":
        print("Computer wins this round!")
        computer_score += 1
    else:
        print("It's a tie!")

    return user_score, computer_score


# Function to play a round of the game
def play_round():
    user_score = 0
    computer_score = 0
    rounds_played = 0

    while True:
        print("\nRound", rounds_played + 1)

        # Prompt the user to choose
        user_choice = input("Choose rock, paper, or scissors: ").lower()

        # Generate a random choice for the computer
        choices = ["rock", "paper", "scissors"]
        computer_choice = random.choice(choices)

        # Determine the winner for the round
        result = determine_round_winner(user_choice, computer_choice)

        # Display the result and update scores
        user_score, computer_score = display_result(user_choice, computer_choice, result, user_score, computer_score)

        rounds_played += 1

        # Ask if the user wants to play another round
        play_again = input("Do you want to play another round? (yes/no): ").lower()
        if play_again != "yes":
            break

    print("\nGame Over!")
    print(f"User's score: {user_score}, Computer's score: {computer_score}")


# Main game loop
print("Welcome to Rock-Paper-Scissors Game!")
while True:
    play_round()
    restart = input("Do you want to play another game? (yes/no): ").lower()
    if restart != "yes":
        print("Thanks for playing! Goodbye.")
        break
