random_number = 68
running = True

while running: # or running == True
    guess = input('Enter a integer: ')

    if guess == 'break':
        break
    
    guess = int(guess)

    if guess == random_number:
        print('you got it right')
        running = False
    elif guess < random_number:
        print('you gonna go a little higher')
        continue
    else:
        print('you gonna go a little lower')
        continue

    print('gratz, you will not reach here if you got the wrong number')
else:
    print('while else done')
