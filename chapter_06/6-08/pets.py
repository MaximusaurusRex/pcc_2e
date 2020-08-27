pets = [{'type': 'cat', 'name': 'Rufus', 'owner': 'John'},
        {'type': 'dog', 'name': 'Domino', 'owner': 'Terry'},
        {'type': 'alligator', 'name': 'Portia', 'owner': 'Michael'},
        {'type': 'squirrel', 'name': 'Killer', 'owner': 'Graham'},
        {'type': 'mongoose', 'name': 'Peep', 'owner': 'Eric'}]

for pet in pets:
    print(
        f"{pet['owner']} has a pet {pet['type']} and its name is {pet['name']}.")
