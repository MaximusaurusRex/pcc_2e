cities_dict = {'Osaka':   {'country': 'Japan',
                           'population': '2,668,586',
                           'fact': 'The Osaka Kaiyukan Aquarium is the second largest aquarium in the world.'},
               'Chicago': {'country': 'USA',
                           'population': '2,695,598',
                           'fact': 'The name Chicago was first recorded in 1688, where it appears as Chigagou, an Algonquian word meaning “onion field.”'},
               'Toronto': {'country': 'Canada',
                           'population': '2,731,571',
                           'fact': 'Toronto Pearson International Airport is the busiest airport in Canada. In 2015, 41 million travellers passed through the airport.'}}

for city, info in cities_dict.items():
    print(f'''The estimated population in {city}, located in {info['country']} is {info['population']} people.
Also, here's an interesting fact: {info['fact']}
''')
