import requests


url = "https://official-joke-api.appspot.com/random_joke"
running = True
# send GET req

response = requests.get(url)

if (response.status_code == 200):
    joke_data = response.json()
    print(f"Joke: {joke_data['setup']} - {joke_data['punchline']}")
else:
    print("FAILED TO RETRIEVE JOKE.")

    

