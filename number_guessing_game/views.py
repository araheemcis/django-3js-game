from django.shortcuts import render
from random import randint


def index(request):
    number = randint(0, 999)
    attempts = 0
    max_attempts = 10
    hint_text = ""


    if request.method == 'POST':
        guess = int(request.POST['guess'])
        attempts += 1

        if guess == number:
            hint_text = f"Congratulations! You guessed the number in {attempts} attempts."

        elif attempts == max_attempts:
            hint_text = f"Sorry, you have used up all your attempts. The number was {number}."

        elif guess < number:
            hint_text = "The number is greater than your guess. Try again."