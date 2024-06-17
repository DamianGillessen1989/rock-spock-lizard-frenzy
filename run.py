import random

def main():
    print("Welcome to Rock-Paper-Scissors-Lizard-Spock!")
    
    player_score = 0
    computer_score = 0
    
    rounds = int(input("How many rounds would you like to play? Best of: "))
    
    choices = ["rock", "spock", "paper", "lizard", "scissors"]

    for _ in range(rounds):
        player_choice = input("\nEnter your choice (rock, spock, paper, lizard, scissors) or type 'exit' to quit the game: ").strip().lower()
        
        if player_choice == 'exit':
            break
        
        if player_choice in choices:
            # Game logic will go here
            pass
        else:
            print("Invalid input. Please enter a valid choice like 'Spock'.")
            print("And check your spelling!")

        # Print current scores
        print("\nCurrent Scores - Player: {}, Computer: {}".format(player_score, computer_score))

    # Final scores and result
    print("Final Scores - Player: {}, Computer: {}".format(player_score, computer_score))
    if player_score > computer_score:
        print("Congratulations! You won the game!")
    elif player_score < computer_score:
        print("Computer wins the game! Better luck next time!")
    else:
        print("It's a tie game! Well played!")

if __name__ == "__main__":
    main()
