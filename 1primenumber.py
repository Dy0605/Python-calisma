number = int(input('Please enter a number: '))

divide = number

while divide > 2:
    divide -= 1
    
    if number % divide == 0:
        print(f'the number is not a prime number because {divide} it is divisible by the number .')
        #break
else:
    print(f'{number} is a prime number.')