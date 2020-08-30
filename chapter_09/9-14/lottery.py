from random import randint
list_nums = [6, 9, 5, 8, 1, 3, 4, 7, 2, 0, 'N', 'X', 'R', 'A', 'L']
winning_nums = []

for i in range(1, 5):
    n = randint(1, 15)
    winning_nums.append(list_nums[n])

print("This week's winning digits are: ", end='')
for i in winning_nums:
    print(f'{i}', end='')
