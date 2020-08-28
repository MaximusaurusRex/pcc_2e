def sandwich_maker(*items):
    print('\nMaking sandwich with the following:')
    for item in items:
        print(f'- {item}')


sandwich_maker('bacon', 'lettuce', 'tomato')
sandwich_maker('butter')
sandwich_maker('peanut butter', 'strawberry jam', 'banana',
               'chocolate chips', 'sprinkles', 'cream cheese frosting')
