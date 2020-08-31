import json

fav_num = input('What is your favorite number?: ')

filename = 'chapter_10/10-11/fav_num.json'
with open(filename, 'w') as f:
    json.dump(fav_num, f)
