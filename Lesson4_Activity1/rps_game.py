# rock-paper-scissors game with AI:
import random
from colorama import Fore, init

init(autoreset=True)


def get_player() -> str:
    a = input("Play again? (y/n): ")
    if a == "y": game()
    elif a == "n": print("Goodbye!")
    else: print("Please type y or n.")


def game():
    print(f"""{Fore.BLUE}
=============================
    ROCK-PAPER-SCISSORS
=============================
""")

    options = [
        "rock", 
        "paper",
        "scissors"
    ]
    pScore = 0 
    aScore = 0

    plyr_choice = str(input(f"{Fore.GREEN}What is your choice? (rock, paper, scissors): ")).lower()

    ai_choice = random.choice(options)

    if plyr_choice == "rock" and ai_choice == options[0]:
        print(f"{Fore.LIGHTCYAN_EX}AI chose: {ai_choice}. It's a tie!")
        get_player()
    if plyr_choice == "rock" and ai_choice == options[1]:
        aScore += 1; print(f"{Fore.LIGHTRED_EX}AI chose: {ai_choice}. AI won! Score: {aScore}")
        get_player()
    if plyr_choice == "rock" and ai_choice == options[2]:
        pScore += 1; print(f"{Fore.LIGHTGREEN_EX}AI chose: {ai_choice}. Player won! Score: {pScore}")
        get_player()

    if plyr_choice == "paper" and ai_choice == options[0]:
        pScore += 1; print(f"{Fore.LIGHTGREEN_EX}AI chose: {ai_choice}. Player won! Score: {pScore}")
        get_player()
    if plyr_choice == "paper" and ai_choice == options[1]:
        print(f"{Fore.LIGHTCYAN_EX}AI chose: {ai_choice}. It's a tie!")
        get_player()
    if plyr_choice == "paper" and ai_choice == options[2]:
        aScore += 1; print(f"{Fore.LIGHTRED_EX}AI chose: {ai_choice}. AI won! Score: {aScore}")
        get_player()

    if plyr_choice == "scissors" and ai_choice == options[0]:
        aScore += 1; print(f"{Fore.LIGHTRED_EX}AI chose: {ai_choice}. AI won! Score: {aScore}")
        get_player()
    if plyr_choice == "scissors" and ai_choice == options[1]:
        pScore += 1; print(f"{Fore.LIGHTGREEN_EX}AI chose: {ai_choice}. Player won! Score: {pScore}")
        get_player()
    if plyr_choice == "scissors" and ai_choice == options[2]:
        print(f"{Fore.CYAN}AI chose: {ai_choice}. It's a tie!")
        get_player()

game()
