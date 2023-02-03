person = {
    'name': 'Moses Nielsen',
    'pass_w': '6878'
}


pin = person.get('pass_w')
limit = 3
# guess = 0
counter = 0
while counter < limit:
    counter += 1
    password = str(input('Enter your Pin: '))
    if pin == password:
        print(f"Correct password on {counter} attempt(s)")
        print(f'Welcome Sir {person.get("name")}')
        break
    else:
        if counter == limit:
            print(f'Sorry, you entered incorrect pin {counter} times, try again after 30 seconds')
        else:
            print('incorrect Pin, Try again!')
            print(f'you have {limit-counter} attempt(s) remaining!')
