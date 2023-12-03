import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        return "You win!"
    else:
        return "You lose!"

def display_choices(user_choice, computer_choice):
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

# Initialize scores
user_score = 0
computer_score = 0

# Main game loop
while True:
    print("\nRock-Paper-Scissors Game")
    print("Choose: rock, paper, or scissors")
    
    # User input
    user_choice = input("Your choice: ").lower()
    
    # Validate user input
    if user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        continue
    
    # Computer selection
    computer_choice = random.choice(["rock", "paper", "scissors"])
    
    # Determine the winner and display choices
    result = determine_winner(user_choice, computer_choice)
    display_choices(user_choice, computer_choice)
    print(result)
    
    # Update scores
    if "win" in result:
        user_score += 1
    elif "lose" in result:
        computer_score += 1
    
    # Display scores
    print(f"\nScores - You: {user_score}, Computer: {computer_score}")
    
    # Ask the user if they want to play again
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        break

print("Thanks for playing!")