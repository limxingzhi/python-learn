random_number = 68
running = True

while running: # or running == True
    guess = int(input('Enter a integer: '))

    if guess == random_number:
        print('you got it right')
        running = False
    elif guess < random_number:
        print('you gonna go a little higher')
    else:
        print('you gonna go a little lower')
else:
    print('while else is here')
