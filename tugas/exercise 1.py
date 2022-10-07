import random
choose_number = random.randint(1,100)

tries = 0
while tries == 0:
    guess = int(input('guess a number from 1-100: '))

    if guess < choose_number:
        print('The guess was too low')
    
    elif guess > choose_number:
        print('the guess was too high')
    
    else:
        print('that\'s correct!')
        print(f'The number is {choose_number}')
        break