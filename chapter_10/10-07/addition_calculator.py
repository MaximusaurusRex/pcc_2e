print('Double digit calculator')
print("(enter 'q' to quit)")

while True:
    two_numbers = input('Enter two numbers and I will add them up: ')

    try:
        num_1 = int(two_numbers[0])
    except ValueError:
        print("That's not a number...")

    try:
        num_2 = int(two_numbers[1])
    except ValueError:
        print("That's not a number...")
    except IndexError:
        print("Where's the second number?\n")

    if len(two_numbers) > 2:
        print("Woah, that's too many numbers. I'll just add up those first two numbers.")

    try:
        print(f"The answer is {num_1 + num_2}\n")
    except (ValueError, NameError):
        print("Something went wrong. Try your equation again, with numbers this time...\n")
    except IndexError:
        print("Where's the second number?\n")
