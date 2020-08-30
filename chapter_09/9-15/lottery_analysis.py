from random import randint

list_nums = [6, 9, 5, 8, 1, 3, 4, 7, 2, 10, 'N', 'X', 'R', 'A', 'L']
my_ticket = [5, 'X', 7, 'R']
loser_count = 0
winning_nums = []

while my_ticket != winning_nums:
    winning_nums = []
    for i in range(1, 5):
        n = randint(1, 14)
        winning_nums.append(list_nums[n])
        loser_count += 1

print(f'''Your prediction: {my_ticket}
Winning ticket: {winning_nums}
Attempts: {loser_count}''')
