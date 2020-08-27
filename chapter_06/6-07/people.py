people = [{'first_name': 'Edward',
           'last_name': 'Snowden',
           'age': 27,
           'city': 'Tokyo'},

          {'first_name': 'Kevin',
           'last_name': 'Mitnick',
           'age': 32,
           'city': 'Raleigh'},

          {'first_name': 'Brian',
           'last_name': 'Krebs',
           'age': 48,
           'city': 'New York City'}]

for person in people:
    print(f'''
    First name: {person.get('first_name')}
    Last name: {person.get('last_name')}
    Age: {person.get('age')}
    City: {person.get('city')}
    ''')
