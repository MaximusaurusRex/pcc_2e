places = {}

while True:
    name = input('\nHello, what is your name? ')
    place = input(
        f'Hi, {name}! If you could visit one place in the world, where would you go? ')
    query = input(
        'Awesome. Would you like to allow someone else eo enter our poll? ')
    places[name] = place
    if query == 'no':
        break

for name, place in places.items():
    print(f'{name} would like to go to {place}.')
