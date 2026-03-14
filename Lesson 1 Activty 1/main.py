from time import sleep
print("Hello! I am an AI bot, what's your name? : ")

name = input()

print(f"Nice to meet you , {name}")

print("How are you feeling today? (good/bad): ")
mood = input().lower()

if mood == "good":
    print("I'm glad to hear that!")
elif mood == "bad":
    print("I'm sorry to hear that, hope things get better soon.")
else:
    print("I see. Sometimes, it's hard to put feelings into words.")

question = input("What other language do you speak? ")
print(f"Oh nice! You speak {question}!")

question2 = input("I have one more question, do you like programming? yes/no: ")
if question2 == "Yes" or question2 == "Yes".lower():
    print("That's great to hear! Programming is a really fun thing to do.")
elif question2 == "No":
    print("It's okay, but you should try programming, it's fun! :)")
else:
    print("Sorry, I didn't get you..")

sleep(1)
print(f"It was nice chatting with you {name}. Goodbye! :D")
