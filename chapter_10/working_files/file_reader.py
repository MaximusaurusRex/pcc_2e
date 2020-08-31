

filename = 'text_files/pi_digits.txt'

# with open('pi_digits.txt') as file_object:
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

#     contents = file_object.read()
# print(contents.rstrip())
