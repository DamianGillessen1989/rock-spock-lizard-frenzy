import random

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
    """
    Provides detailed feedback on the outcome of a game round.
    Args:
        player_choice (str): The player's choice
        (e.g., "Rock", "Spock", "Paper", "Lizard", "Scissors").
        comp_choice (str): The computer's choice
        (e.g., "Rock", "Spock", "Paper", "Lizard", "Scissors").
        outcome (str): The outcome of the round ("tie", "player", "computer").
    Returns:
        str: A detailed feedback message explaining the outcome.
    """
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
        return ("Player wins!\n" +
                win_scenarios.get((player_choice, comp_choice), ""))
    else:
        return ("Computer wins!\n" +
                win_scenarios.get((comp_choice, player_choice), ""))


def game_mechanics(player_choice, player_score, computer_score):
    """
    Executes a round of the Rock-Paper-Scissors-Lizard-Spock game.
    Args:
        player_choice (str): The player's choice
        (e.g., "Rock", "Spock", "Paper", "Lizard", "Scissors").
        player_score (int): The current score of the player.
        computer_score (int): The current score of the computer.
    Returns:
        tuple: The updated scores for the player and computer.
    """
    print()
    print("Player chooses", player_choice.capitalize())
    player_number = name_to_number(player_choice)
    if player_number == -1:
        print("Invalid player choice. Game cannot proceed.")
        return player_score, computer_score

    comp_number = random.randrange(0, 5)
    comp_choice = number_to_name(comp_number)
    print("Computer chooses", comp_choice)

    diff = (comp_number - player_number) % 5

    if diff == 0:
        outcome = "tie"
        print("It's a tie! xxx")
    elif diff in [1, 2]:
        outcome = "computer"
        computer_score += 1
        print("Computer wins! xxx")
        print(random.choice(taunts))
    else:
        outcome = "player"
        player_score += 1
        print("Player wins! xxx")
        print(random.choice(encouragements))

    feedback = detailed_feedback(player_choice, comp_choice, outcome)
    print(feedback)

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

        print("Welcome to Rock-Paper-Scissors-Lizard-Spock!")
        rounds = input("How many rounds would you like to play? Best of: ")

        while not rounds.isdigit():
            print("Please choose a number.")
            rounds = input("How many rounds would you like to play? Best of: ")

        rounds = int(rounds)

        for _ in range(rounds):
            player_choice = input("\nEnter your choice "
                                  "(Rock, Spock, Paper, Lizard, Scissors)"
                                  " or type 'exit' to quit the game: "
                                  ).strip().lower()
            if player_choice in ['exit', 'quit']:
                print("\nThank you for playing Rock, Paper, Scissors, "
                      "Lizard, Spock.\n" "\nIf you want to check out my other "
                      "work visit: https://github.com/DamianGillessen1989\n"
                      "\nLive long, and Prosper.\n")
                return
            if player_choice in choices:
                player_score, computer_score = game_mechanics(
                    player_choice, player_score, computer_score)
            else:
                print("Invalid input. Please enter a valid choice ")
                print("like 'Spock'. And check your spelling!")

            print("\nCurrent Scores - Player: {}, Computer: {}".format(
                player_score, computer_score))

        print("\nFinal Scores - Player: {}, Computer: {}".format(
            player_score, computer_score))
        if player_score > computer_score:
            print("Congratulations! You won the game!")
        elif player_score < computer_score:
            print("Computer wins the game! Better luck next time!")
        else:
            print("It's a tie game! Well played!")

        play_again = input("Do you want to play again? "
                           "(yes/no): ").strip().lower()
        if play_again not in ['yes', 'y']:
            break

    print("\nThank you for playing Rock, Paper, Scissors, Lizard, Spock.\n"
          "\nIf you want to check out my other work visit: "
          "https://github.com/DamianGillessen1989\n"
          "\nLive long, and Prosper.\n")


if __name__ == "__main__":
    main()
