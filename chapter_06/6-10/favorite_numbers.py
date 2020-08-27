favnums = {'Eric': [16, 73, 592],
           'John': [35, 78],
           'Terry': [3, 2, 1],
           'Michael': [150, 1, 692453],
           'Graham': [69, 96, 1337]}

for person, nums in favnums.items():
    print(f"\n{person}'s favorite numbers:")
    for num in nums:
        print(num)
