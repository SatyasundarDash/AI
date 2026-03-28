import re, random
from colorama import Fore, init

init(autoreset=True)

destinations = {
    "beaches": ["Bali", "Maldives", "Phuket"],
    "mountains": ["Swiss Alps", "Himalayas", "Rocky Moutains"],
    "cities": ["Tokyo", "Paris", "Delhi"] 
                }

jokes = [
    "Why don't programmers like nature? Too many bugs!",
    "Why did the computer go to the doctor? Because it had a virus!",
    "Why do travelers always feel warm? Because of all their hot spots!"
]

def normalize_input(txt):
    return re.sub(r"\s", " ", txt.strip().lower())

def recommend():
    print(Fore.CYAN + "TravelBot: Beaches, mountains or cities?")
    preference = input(Fore.YELLOW + "You: ")
    preference = normalize_input(preference)

    if preference in destinations:
        suggestion = random.choice(destinations[preference])
        print(Fore.GREEN + f"TravelBot: How about {suggestion}?")
        print(Fore.CYAN + "TravelBot: Do you like it? (Yes/no)")
        ans = input(Fore.YELLOW + "You: ").lower()

        if ans == "yes": print(Fore.GREEN + f"TravelBot: Awesome! Enjoy {suggestion}!")
        elif ans == "no": print(Fore.RED + "TravelBot: Let's try another."); recommend()
        else: print(Fore.RED + "TravelBot: I'll suggest again."); recommend()

    else:
        print(Fore.RED + "TravelBot: Sorry, I don't have that type of destination.")
        recommend()

def packing_tips():
    print(Fore.CYAN + "TravelBot: Where to?")
    location = normalize_input(input(Fore.YELLOW + "You: "))
    print(Fore.CYAN + 'TravelBot: How many days?')
    days = input(Fore.YELLOW + "You: ")

    print(Fore.GREEN + f"TravelBot: Packing tips for {days} days in {location}:")
    print(Fore.GREEN + "- Pack versatile clothes.")
    print(Fore.GREEN + "- Bring chargers/adapters.")
    print(Fore.GREEN + "- Check the weather forecast.")

def joke():
    print(Fore.YELLOW + f"TravelBot: {random.choice(jokes)}")

def help():
    print(Fore.MAGENTA + "\nI can:")
    print(Fore.GREEN + "- Suggest travel spots (say 'recommendation')")
    print(Fore.GREEN + "- Offer packing tips (say 'packing')")
    print(Fore.GREEN + "- Tell a joke (say 'joke')")
    print(Fore.CYAN + "Type 'exit' or 'bye' to end.\n")

def chat():
    print(Fore.CYAN + "Hello! I'm TravelBot.")
    name = input(Fore.YELLOW + "Your name? ")
    print(Fore.GREEN + f"Nice to meet you, {name}!")

    help()

    while True:
        user_input = input(Fore.YELLOW + f"{name}:")
        user_input = normalize_input(user_input)

        if "recommend" in user_input or "suggest" in user_input: recommend()
        elif "pack" in user_input or "packing" in user_input: packing_tips()
        elif "joke" in user_input or "funny" in user_input: joke()
        elif "help" in user_input: help()
        elif "exit" in user_input or "bye" in user_input:
            print(Fore.CYAN + "TravelBot: Safe travels! Goodbye!")
            break
        else: print(Fore.RED + "TravelBot: Could you rephrase?")

if __name__ == "__main__":
    chat()
