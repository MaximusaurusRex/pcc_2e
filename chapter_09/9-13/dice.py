from random import randint


class Die:

    def __int__(self, sides=6):
        self.sides = 6

    def roll_6_sided_dice(self):
        print(randint(1, 6))

    def roll_10_sided_dice(self):
        print(randint(1, 10))

    def roll_20_sided_dice(self):
        print(randint(1, 20))


dice_game = Die()

print('\n~~~6 SIDED DICE RESULTS~~~')
for i in range(1, 11):
    print(f'Roll #{i}: ', end='')
    dice_game.roll_6_sided_dice()

print('\n~~~10 SIDED DICE RESULTS~~~')
for i in range(1, 11):
    print(f'Roll #{i}: ', end='')
    dice_game.roll_10_sided_dice()

print('\n~~~20 SIDED DICE RESULTS~~~')
for i in range(1, 11):
    print(f'Roll #{i}: ', end='')
    dice_game.roll_20_sided_dice()
