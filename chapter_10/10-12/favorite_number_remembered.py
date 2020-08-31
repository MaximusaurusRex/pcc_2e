import json

filename = 'chapter_10/10-11/fav_num.json'

try:
    with open(filename) as f:
        fav_num = json.load(f)
except FileNotFoundError:
    fav_num = input('What is your favorite number?: ')
    with open(filename, 'w') as f:
        json.dump(fav_num, f)
else:
    print(f"I know your favorite number! It's {fav_num}")
