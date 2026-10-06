import requests

url = "https://uselessfacts.jsph.pl/api/v2/facts/random?language=en"

def get_random_technology_fact():
    response = requests.get(url)
    if (response.status_code == 200):
        factData = response.json()
        print(f"Did you know? {factData['text']}")
    else: print("Failed to fetch fact.")

while True:
    userInput = input("Press [Enter] to get a random technology fact or press [Q] to quit...")
    if (userInput.lower() == 'q'):
        break
    get_random_technology_fact()

