import math, sys, unicodedata
from collections import Counter
from samples import SAMPLES

THRESHOLD = 0.15


# hindi and japanese require UTF-8 on the screen
if (hasattr(sys.stdout, "reconfigure")):
    sys.stdout.reconfigure(encoding="utf-8")

def charTrigrams(text):
    cleaned = []
    for ch in text.lower():
        if (ch.isalpha() or unicodedata.category(ch).startswith("M")): cleaned.append(ch)
        else: cleaned.append(" ")

    padded = " " + " ".join("".join(cleaned).split()) + " "
    return Counter(padded[i:i + 3] for i in range(len(padded) - 2))


# 2nd Step:
PROFILES = {language: charTrigrams(text) for language, text in SAMPLES.items()}

# Step 3

def cosine(p, q):
    dot = sum(p[gram] * q[gram] for gram in p if gram in q)
    size_p = math.sqrt(sum(count * count for count in p.values()))
    size_q = math.sqrt(sum(count * count for count in q.values()))
    if (size_p == 0 or size_q == 0):
        return 0.0
    return dot / (size_p * size_q)

# Step 4:

def rankLanguages(text):
    mystery = charTrigrams(text)
    scores = {}
    for language, profile in PROFILES.items():
        scores[language] = cosine(mystery, profile)
    return sorted(scores.items(), key=lambda pair: pair[1], reverse=True)

def detect(text):
    ranking = rankLanguages(text)
    if (not ranking):
        return "Unknown"
    best_langauge, best_score = ranking[0]
    if (best_score < THRESHOLD):
        return "Unknown"
    return best_langauge

def clues(text, language, n=6):
    if (language not in PROFILES):
        return []
    mystery = charTrigrams(text)
    shared = Counter({g: c * PROFILES[language][g] for g, c in mystery.items() if g in PROFILES[language]})
    return [g for g, _ in shared.most_common(n)]

CASE_FILES = [
("The library is closed on Sundays but the café is open.", "English"),
("¿Dónde está la estación de tren? Necesito comprar un billete.", "Spanish"),
("Ieri sera abbiamo mangiato una pizza buonissima con gli amici.", "Italian"),
("Je voudrais un croissant et un chocolat chaud, s'il vous plaît.", "French"),
("Ich habe heute keine Zeit, weil ich für die Prüfung lernen muss.", "German"),
("आज मौसम बहुत अच्छा है, चलो बाहर घूमने चलते हैं।", "Hindi"),
("Yaar aaj bahut garmi hai, chalo ice cream khaane chalte hain.", "Hinglish"),

]

COLD_CASES = [
    "pizza",
    "Hola!", 
    "la pasta è buona", 
    "Kal meeting hai, please don't be late",
    "12345", 
    "こんにちは、元気ですか"
]

def play():
    you = detective = 0
    print("Read each message and type your guess (e.g. French). Then see what the detective says.\n")
    for number, (text, answer) in enumerate(CASE_FILES, 1):
        print(f"Case {number}: {text}")
        guess = input("     Your guess: ").strip().title()
        found = detect(text)
        you += guess == answer
        detective += found == answer
        print(f"   Detective: {found}     Answer: {answer}    Clues: {clues(text, found)}\n")
        print(f"Final score - You: {you}/{len(CASE_FILES)}    Detective: {detective}/{len(CASE_FILES)}")

if (__name__ == "__main__"):
    play()
    print("\nCold cases:")
    for text in COLD_CASES:
        top_two = ", ".join(f"{lang} {score:.2f}" for lang, score in rankLanguages(text)[:2])
        print(f"    {text!r:<42} -> {detect(text):<9} (top two: {top_two})")

    print("\nInterrogation room: type any text ('quit' to stop).")
    while True:
        text = input("\n> ")
        if (text.strip().lower() == "quit"):
            break
        for langauge, score in rankLanguages(text):
            print(f"   {langauge:<9} {'#' * round(score * 30):<30}")
