import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'chapter_10/working_files/numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)
