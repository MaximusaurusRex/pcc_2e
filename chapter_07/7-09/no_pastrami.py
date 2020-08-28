sandwich_orders = ['dagwood', 'pastrami', 'bacon',
                   'pastrami', 'grilled cheese',
                   'chicken', 'pastrami', 'tuna']
finished_sandwiches = []
sandwich = ''

print('The deli has run out of pastrami.\n')

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f'I made you a {current_sandwich} sandwich.')
    finished_sandwiches.append(current_sandwich)

print('\nSandwiches made:')
for sandwich in finished_sandwiches:
    print(sandwich)
