pin = 6878
limit = 3
guess = 0
counter = 0
while counter < limit:
    counter += 1

    password = int(input('Enter your Pin: '))
    if pin == password:
        print(f"Correct password on {counter} attempt(s)")
        break
    else:
        if counter == limit:
            print('Sorry, you enter incorrect pin 3 times, try again after 30 seconds')
        else:
            print('incorrect Pin, Try again!')
            print(f'you {limit-counter} attempt(s) remaining!')
