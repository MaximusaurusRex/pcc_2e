favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")


new_pollers = ['eric', 'john', 'sarah', 'michael', 'edward']

for name in new_pollers:
    print(name.title())

    if name in favorite_languages.keys():
        print(f'\tThank you {name.title()} for taking our poll.')
    else:
        print(f'\t{name.title()}, please take our poll.')
