while True:
    ans = input("Why do you like programming? (type 'end' to give up): ")
    if ans.lower() == 'end':
        break
    with open('chapter_10/10-05/responses.txt', 'a') as file_object:
        file_object.write(f'{ans}\n')
