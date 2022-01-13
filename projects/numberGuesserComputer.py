import random


def numberguesser(x):
    low = 1
    high = x
    feedback = ''

    while feedback != 'c':
        number = random.randint(low, high)
        feedback = input(f"if {number} is high(H) or low(L) or Correct (C) ??: ").lower()
        if feedback == "h":
            high = number-1

        elif feedback == 'l':
            low = number+1

    print(f"Marvelous!!, You have guessed the correct number {number} !!!")

numberguesser(100)
#
#


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Sorry, guess again. Too low.')
        elif guess > random_number:
            print('Sorry, guess again. Too high.')

    print(f'Yay, congrats. You have guessed the number {random_number} correctly!!')



