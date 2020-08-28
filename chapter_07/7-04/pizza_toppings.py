topping = ''

while topping != 'quit':
    topping = input(
        'What toppings would you like on your pizza?\n(press quit to complete your request) ').lower()
    if topping != 'quit':
        print(f'\n{topping.title()} has been added to your pizza.\n')
