import json

filename = 'chapter_10/10-11/fav_num.json'
with open(filename) as f:
    fav_num = json.load(f)

print(f"I know your favorite number! It's {fav_num}")
