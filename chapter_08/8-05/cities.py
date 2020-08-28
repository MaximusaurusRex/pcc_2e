def describe_city(name, country='Canada'):
    print(f'{name.title()} is in {country.title()}.')


describe_city('london', 'england')
describe_city('toronto')
describe_city('reykjavik', 'iceland')
