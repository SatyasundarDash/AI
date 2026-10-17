import requests

url = "https://official-joke-api.appspot.com/random_joke"

response = requests.get(url)
if (response.status_code == 200):

    jokeData = response.json()

    print(f"Joke: {jokeData['setup']} {jokeData['punchline']}")

else:
    print(f"Failed to retrieve joke. Status code: {response.status_code}")