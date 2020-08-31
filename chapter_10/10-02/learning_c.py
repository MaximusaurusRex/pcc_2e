another_list = ''

with open('chapter_10/10-01/learning_text.txt') as file_object:
    lines = file_object.readlines()
    for line in lines:
        another_list += line.replace('Python', 'JavaScript')

print(another_list)
