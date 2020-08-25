guests = ['Ryan Gosling', 'Tom Hanks', 'Chris Farley',
          'Robin Williams', 'George Clooney', 'Jack Nicholson']
print('Unfortunately, this will be a private event. Only two members will be invited.')
print(f"I'm sorry {guests.pop()}, you will have to leave.")
print(f"I'm sorry {guests.pop()}, you will have to leave.")
print(f"I'm sorry {guests.pop()}, you will have to leave.")
print(f"I'm sorry {guests.pop()}, you will have to leave.")
print(f'Welcome to the Oscars, {guests[0]}.')
print(f'Welcome to the Oscars, {guests[1]}.')
del guests[1]
del guests[0]
print(guests)
