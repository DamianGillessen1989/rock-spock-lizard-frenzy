# This code is based on the code by EricPPeterson on GitHub

import random
import os

encouragements = [
    "Great job!",
    "You're on fire!",
    "Keep it up!",
    "You're unstoppable!",
    "Well played!"
]

taunts = [
    "Better luck next time, loser!",
    "Oh, did that hurt?",
    "Is that all you've got?",
    "Try harder, you might win someday!",
    "Pathetic effort, really."
]


def name_to_number(name):
    """
    Converts a choice name to its corresponding number.
    Args:
        name (str): The name of the choice
        (e.g., "Rock", "Spock", "Paper", "Lizard", "Scissors").
    Returns:
        int: The corresponding number for the choice,
        or -1 if the input is invalid.
    """
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
    """
    Converts a choice number to its corresponding name.
    Args:
        number (int): The number of the choice (0 to 4).
    Returns:
        str: The corresponding name for the choice,
        or "Invalid Input" if the input is invalid.
    """
    if number == 0:
        return 'Rock'
    elif number == 1:
        return 'Spock'
    elif number == 2:
        return 'Paper'
    elif number == 3:
        return 'Lizard'
    elif number == 4:
        return 'Scissors'
    else:
        return 'Invalid Input'


win_scenarios = {
    (0, 4): "Rock crushes Scissors!",
    (0, 3): "Rock crushes Lizard!",
    (1, 4): "Spock smashes Scissors!",
    (1, 0): "Spock vaporizes Rock!",
    (2, 0): "Paper covers Rock!",
    (2, 1): "Paper disproves Spock!",
    (3, 1): "Lizard poisons Spock!",
    (3, 2): "Lizard eats Paper!",
    (4, 2): "Scissors cuts Paper!",
    (4, 3): "Scissors decapitates Lizard!",
    # Adding reverse scenarios for the computer's win
    (4, 0): "Rock crushes Scissors!",
    (3, 0): "Rock crushes Lizard!",
    (4, 1): "Spock smashes Scissors!",
    (0, 1): "Spock vaporizes Rock!",
    (0, 2): "Paper covers Rock!",
    (1, 2): "Paper disproves Spock!",
    (1, 3): "Lizard poisons Spock!",
    (2, 3): "Lizard eats Paper!",
    (2, 4): "Scissors cuts Paper!",
    (3, 4): "Scissors decapitates Lizard!"
}


def detailed_feedback(player_choice, comp_choice, outcome):
    """
    Provides detailed feedback on the outcome of a game round.
    Args:
        player_choice (str): The player's choice
        (e.g., "Rock", "Spock", "Paper", "Lizard", "Scissors").
        comp_choice (str): The computer's choice
        (e.g., "Rock", "Spock", "Paper", "Lizard", "Scissors").
        outcome (str): The outcome of the round ("tie",
                       "player", or "computer").
    Returns:
        str: A detailed feedback message explaining the outcome.
    """
    if outcome == 'tie':
        return f'Both chose {player_choice.capitalize()}.'
    elif outcome == 'player':
        return win_scenarios[
            (name_to_number(player_choice), name_to_number(comp_choice))
        ]
    elif outcome == 'computer':
        return win_scenarios[
            (name_to_number(comp_choice), name_to_number(player_choice))
        ]
    else:
        return 'Error: Invalid outcome.'


def game_mechanics(player_choice, player_score, computer_score):
    """
    Executes a round of the Rock-Paper-Scissors-Lizard-Spock game.
    Args:
        player_choice (str): The player's choice
            ("Rock", "Spock",
           "Paper","Lizard","Scissors").
                player_score(int) : The current score of the player.
                computer_score(int) : The current score of the computer.
    Returns:
        tuple: The updated scores for the player and computer.
    """
    player_choice = player_choice.strip().lower()

    print()
    print("\nPlayer chooses", player_choice.capitalize())
    player_number = name_to_number(player_choice)

    if player_number == -1:
        print("Invalid player choice. Game cannot proceed.\n")
        return player_score, computer_score

    comp_number = random.randrange(0, 5)
    comp_choice = number_to_name(comp_number)

    print("\nComputer chooses", comp_choice),

    diff = (comp_number - player_number) % 5

    result_message = ""

    if diff == 0:
        outcome = "tie"
        print("\nIt's a tie!\n\n")
    elif diff in [1, 2]:
        outcome = "computer"
        computer_score += 1
        print("\nComputer wins!\n\n")
        print(random.choice(taunts), "\n")
    else:
        outcome = "player"
        player_score += 1
        print("\n\nPlayer wins!\n\n")
        print(random.choice(encouragements), "\n")

    result_message = detailed_feedback(player_choice, comp_choice, outcome)
    print(result_message)

    return player_score, computer_score


def main():
    """
    The main function to run the Rock-Paper-Scissors-Lizard-Spock game.
    Prompts the user to enter the number of rounds and manages the game flow.
    """
    while True:
        choices = ["rock", "spock", "paper", "lizard", "scissors"]
        player_score = 0
        computer_score = 0

        print("Welcome to Rock-Paper-Scissors-Lizard-Spock!\n")
        rounds = input("How many rounds would you like to play? "
                       "Type a number and hit enter. Best of: ")

        while not rounds.isdigit() or not (1 <= int(rounds) <= 25):
            print("Please enter a number between 1 and 25.\n")
            rounds = input("How many rounds would you like to play? "
                           "Type a number and hit enter. Best of: ")

        rounds = int(rounds)
        required_wins = (rounds // 2) + 1

        while player_score < required_wins and computer_score < required_wins:
            player_choice = input(
                "\nEnter your choice (Rock, Spock, Paper, Lizard, Scissors) "
                "and hit enter. Or type 'exit' to quit the game: "
            ).strip().lower()
            os.system('cls' if os.name == 'nt' else 'clear')
            if player_choice in ['exit', 'quit']:
                print(
                    "\nThank you for playing my Rock, Paper, Scissors, Lizard,"
                    " Spock game.\n\nIf you want to check out some of my other"
                    " work visit: https://github.com/DamianGillessen1989\n\n"
                    "Live long, and Prosper 🖖\n"
                )
                return
            if player_choice in choices:
                player_score, computer_score = game_mechanics(
                    player_choice, player_score, computer_score
                )
            else:
                print(
                    "Invalid input. Please enter a valid choice like 'Spock'. "
                    "And check your spelling!\n"
                )

            print(
                "\nCurrent Scores - Player: {}, Computer: {}\n".format(
                    player_score, computer_score
                )
            )

        print(
            "\nFinal Scores - Player: {}, Computer: {}\n".format(
                player_score, computer_score
            )
        )
        if player_score > computer_score:
            print("Congratulations! You won the game!\n")
        else:
            print("Computer wins the game! Better luck next time!\n")

        while True:
            play_again = input
            ("Do you want to play again? (yes/no): ").strip().lower()
            os.system('cls' if os.name == 'nt' else 'clear')
            if play_again in ['yes', 'y']:
                break
            elif play_again in ['no', 'n']:
                print(
                    "\nThank you for playing my Rock, Paper, Scissors, Lizard,"
                    " Spock game.\n\nIf you want to check out some of my other"
                    " work visit: https://github.com/DamianGillessen1989\n\n"
                    "Live long, and Prosper 🖖\n"
                )
                return
            else:
                print("Please enter 'yes' or 'no'.")


if __name__ == "__main__":
    main()
