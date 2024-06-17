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
