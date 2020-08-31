while True:
    name = input("Hello, what is your name? (type 'end' to finish the list): ")
    if name.lower() == 'end':
        break
    with open('chapter_10/10-04/guest_book.txt', 'a') as file_object:
        file_object.write(f'{name} has visited.\n')
    print(f'Thank your for visiting us, {name}!\n')
