import random

number = random.randint(1, 10)

attempts = int(input("Enter the number of attempts: "))
counter = 0
remaining_attempts = attempts

while attempts > 0:
    attempts -= 1
    counter += 1
    guess = int(input('Guess the number: '))

    if number == guess:
        print(f'The number I was thinking of was {number}, you won! \nYou guessed it in {counter} attempts. Your total score is: {100 - (100/remaining_attempts * (counter-1))}')
        break
    elif number > guess:
        print('Higher')
    elif number < guess:
        print("Lower")
else:
    print(f'You ran out of attempts, you lost. The number was: {number}')