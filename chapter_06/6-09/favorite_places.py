favoritePlaces = {'Eric': ['Japan', 'Korea'],
                  'Michael': ['Cuba', 'Barbados', 'Dominican Republic'],
                  'John': ['Russia']}

for person, places in favoritePlaces.items():
    print(f"\n{person}'s favorite places to visit:")
    for place in places:
        print(place)
