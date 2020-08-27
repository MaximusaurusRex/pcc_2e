riverdict = {'nile': 'egypt', 'yangtze': 'china', 'mississippi': 'america'}

for river, country in riverdict.items():
    print(f'The {river.title()} river runs through {country.title()}.')

print('\nRiver names:')
for river in riverdict.keys():
    print(river)

print('\nCountry names:')
for country in riverdict.values():
    print(country)
