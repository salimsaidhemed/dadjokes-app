import random

def get_random_joke():
    with open("jokes.txt", "r", encoding="utf-8") as f:
        jokes = [line.strip() for line in f if line.strip()]
    return random.choice(jokes)
