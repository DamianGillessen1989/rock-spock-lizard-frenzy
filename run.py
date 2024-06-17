import random

def main():
    print("Welcome to Rock-Paper-Scissors-Lizard-Spock!")
    
    player_score = 0
    computer_score = 0
    
    rounds = int(input("How many rounds would you like to play? Best of: "))
    
    choices = ["rock", "spock", "paper", "lizard", "scissors"]