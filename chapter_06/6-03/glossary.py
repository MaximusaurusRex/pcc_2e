progwds = {'variable': 'Containers for storing data values.',
           'booleans': 'Represent one of two values: True or False.',
           'list': 'A collection which is ordered and changeable. Allows duplicate members.',
           'tuple': 'A collection which is ordered and unchangeable. Allows duplicate members.',
           'dictionary': 'A collection which is unordered, changeable and indexed. No duplicate members.'}

print(f'''
Python Programming Terms\n
Variable:
\t{progwds.get('variable')}
Booleans:
\t{progwds.get('booleans')}
List:
\t{progwds.get('list')}
Tuple:
\t{progwds.get('tuple')}
Dictionary:
\t{progwds.get('dictionary')}
''')
