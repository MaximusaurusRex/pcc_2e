filenames = ['chapter_10/10-08/cats.txt', 'chapter_10/10-08/dogs.txt']

for file in filenames:
    try:
        with open(file) as f:
            lines = f.readlines()
        for line in lines:
            print(f'{line.strip()}')
        print()
    except FileNotFoundError:
        pass
