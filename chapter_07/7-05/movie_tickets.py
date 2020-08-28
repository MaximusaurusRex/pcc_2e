age = int(input('What is your age? '))
if age < 3:
    print('Your ticket will be free.')
elif age < 12:
    print('Your ticket will be $12.')
else:
    print('Your ticket will be $15.')
