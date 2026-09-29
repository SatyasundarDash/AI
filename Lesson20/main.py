import requests

url = "https://opentdb.com/api.php?amount=5&category=18&difficulty=easy&type=multiple" # Fetch 5 questions

# send GET req to fetch trivia questions

response = requests.get(url)

if (response.status_code == 200):
    trivia_data = response.json()
    score: int = 0

    for i, question_data in enumerate(trivia_data["results"]):
        print(f"Question {i + 1}: {question_data['question']}")

        options = question_data['incorrect_answers'] + [question_data['correct_answer']]
        options = sorted(options)

        for j, option in enumerate(options):
            print(f"{j + 1}, {option}")

        userAnswer = input("Your answer (1/2/3/4): ")
        if (options[int(userAnswer) - 1] == question_data["correct_answer"]):
            print("That's correct!"); score += 1
        else:
            print(f"Wrong! The correct answer was {question_data['correct_answer']}")
        print("\n")

    print(f"Your final score: {score}/{len(trivia_data['results'])}")

else:
    print("Failed to retrieve answer from trivia.")
