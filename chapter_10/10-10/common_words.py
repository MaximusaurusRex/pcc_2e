def common_words(filename, word):
    """Count the amount of common words in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        pass
    else:
        line_count = 0
        for line in lines:
            line_count += line.lower().count(word)
        print(
            f'The word "{word}" appears {line_count} times in {filename[len(filepath):]}.')


filepath = 'chapter_10/10-10/'
filenames = [f'{filepath}cities.txt', f'{filepath}frankenstein.txt',
             f'{filepath}sherlock.txt', f'{filepath}prejudice.txt',
             f'{filepath}jekyll.txt']

word = "the"

for filename in filenames:
    common_words(filename, word)
