import random

def name_to_number(name):
    name = name.lower()
    if name == "rock":
        return 0
    elif name == "spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        return -1

def number_to_name(number):
    if number == 0:
        return "Rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "Paper"
    elif number == 3:
        return "Lizard"
    elif number == 4:
        return "Scissors"
    else:
        return "Invalid Input"

def detailed_feedback(player_choice, comp_choice, outcome):
    win_scenarios = {
        ("rock", "scissors"): "Rock crushes Scissors!",
        ("rock", "lizard"): "Rock crushes Lizard!",
        ("spock", "scissors"): "Spock smashes Scissors!",
        ("spock", "rock"): "Spock vaporizes Rock!",
        ("paper", "rock"): "Paper covers Rock!",
        ("paper", "spock"): "Paper disproves Spock!",
        ("lizard", "spock"): "Lizard poisons Spock!",
        ("lizard", "paper"): "Lizard eats Paper!",
        ("scissors", "paper"): "Scissors cuts Paper!",
        ("scissors", "lizard"): "Scissors decapitates Lizard!"
    }
    if outcome == "tie":
        return "Both chose {}.".format(player_choice)
    elif outcome == "player":
        return "Player wins! " + win_scenarios.get((player_choice, comp_choice), "")
    else:
        return "Computer wins! " + win_scenarios.get((comp_choice, player_choice), "")

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

        print("\nCurrent Scores - Player: {}, Computer: {}".format(player_score, computer_score))

    print("Final Scores - Player: {}, Computer: {}".format(player_score, computer_score))
    if player_score > computer_score:
        print("Congratulations! You won the game!")
    elif player_score < computer_score:
        print("Computer wins the game! Better luck next time!")
    else:
        print("It's a tie game! Well played!")

if __name__ == "__main__":
    main()
