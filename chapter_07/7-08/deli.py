sandwich_orders = ['dagwood', 'bacon', 'grilled cheese', 'chicken', 'tuna']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f'I made you a {current_sandwich} sandwich.')
    finished_sandwiches.append(current_sandwich)

print('\nSandwiches made:')
for sandwich in finished_sandwiches:
    print(sandwich)
