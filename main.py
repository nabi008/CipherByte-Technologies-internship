import random

def get_user_choice():
    user_input = input("Enter choice (rock, paper, or scissors): ").lower()
    while user_input not in ['rock', 'paper', 'scissors']:
        print("Invalid choice! Please try again.")
        user_input = input("Enter choice (rock, paper, or scissors): ").lower()
    return user_input

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "User wins!"
    else:
        return "Computer wins!"

def rock_paper_scissors_game():
    play_again = 'yes'
    while play_again.lower() == 'yes':
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"User choice: {user_choice}")
        print(f"Computer choice: {computer_choice}")
        result = determine_winner(user_choice, computer_choice)
        print(result)
        play_again = input("Do you want to play again? (yes/no): ")

if __name__ == "__main__":
    rock_paper_scissors_game()
