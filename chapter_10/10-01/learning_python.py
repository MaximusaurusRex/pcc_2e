another_list = ''

with open('chapter_10/10-01/learning_text.txt') as file_object:
    lines = file_object.readlines()
    for line in lines:
        another_list += line

print(lines)

print('\n~~~~~~~~~~~~~~~~~~~~')

for line in lines:
    print(line.strip())

print('\n~~~~~~~~~~~~~~~~~~~~')

print(another_list)
