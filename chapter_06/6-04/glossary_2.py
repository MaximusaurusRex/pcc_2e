progwds = {'variable': 'containers for storing data values.',
           'booleans': 'represent one of two values: True or False.',
           'list': 'a collection which is ordered and changeable. Allows duplicate members.',
           'tuple': 'a collection which is ordered and unchangeable. Allows duplicate members.',
           'dictionary': 'a collection which is unordered, changeable and indexed. No duplicate members.',
           'set': 'a collection which is unordered and unindexed. In Python sets are written with curly brackets.',
           'for loop': 'used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).',
           'function': 'a block of code which only runs when it is called.',
           'module': 'a file containing a set of functions you want to include in your application.',
           'RegEx': 'also called Regular Expression, a sequence of characters that forms a search pattern.', }

print('Python Programming Terms\n')
for k, v in progwds.items():
    print(f'{k.title()}:\n\t{v}')
