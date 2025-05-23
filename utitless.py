import random

def generate_greeting():
    greetings = [
        "Привет!",
        "Здравствуйте!",
        "Добрый день!",
        "Приветствую вас!",
        "Хорошего дня!"
    ]
    return random.choice(greetings)
