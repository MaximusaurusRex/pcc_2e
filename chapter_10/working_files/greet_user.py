import json

filename = 'chapter_10/working_files/username.json'
with open(filename) as f:
    username = json.load(f)
    print(f"Welcome back, {username}!")
