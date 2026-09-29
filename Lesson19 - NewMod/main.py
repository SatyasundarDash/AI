import requests


url = "https://official-joke-api.appspot.com/random_joke"
running = True
# send GET req


# req codes: 
"""
    200 = Successful!
    404 = Data not found.
    500 = Server side errors.

"""
while running:
    response = requests.get(url)

    if (response.status_code == 200):
        joke_data = response.json()
        print(f"Joke: {joke_data['setup']} - {joke_data['punchline']}")
        print(response.json())
    else:
        print("FAILED TO RETRIEVE JOKE.")

    a = input("Do you want another joke? (y/n)")
    if (a != "y"):
        break





    

