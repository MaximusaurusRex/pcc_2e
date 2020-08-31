import json

filename = 'chapter_10/working_files/numbers.json'
with open(filename) as f:
    numbers = json.load(f)

print(numbers)
