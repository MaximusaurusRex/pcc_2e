name = input("What is your name? ")

with open('chapter_10/10-03/guests.txt', 'w') as file_object:
    file_object.write(name)
