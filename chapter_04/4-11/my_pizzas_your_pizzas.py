pizzas = ['pepperoni', 'canadian', 'hawaiian', 'three cheese']
friend_pizzas = pizzas[:]
pizzas.append('pineapple')
friend_pizzas.append('the works')
print(
    f"Hello, yes this is Domino's pizza, we sell the following: {friend_pizzas}")
print("Okay that's great but I'm looking for:")
for pizza in pizzas:
    print(pizza)
