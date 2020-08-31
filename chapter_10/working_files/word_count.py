def count_words(filename):
    """Count the approx number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        # print(f"Sorry, the file {filename[len(filepath):]} does not exist.")
        pass
    else:
        # Count the approx number of words in the file
        words = contents.split()
        num_words = len(words)
        print(
            f"The file {filename[len(filepath):]} has about {num_words} words.")


filepath = 'chapter_10/working_files/'
filenames = [f'{filepath}alice.txt', f'{filepath}siddharta.txt',
             f'{filepath}moby_dick.txt', f'{filepath}little_women.txt']
for filename in filenames:
    count_words(filename)
