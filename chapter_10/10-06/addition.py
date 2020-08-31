two_numbers = input('Enter two numbers and I will add them up: ')

if len(two_numbers) > 2:
    print("Woah, that's too many numbers. I'll just add up those first two numbers.")

try:
    print(f"The answer is {int(two_numbers[0]) + int(two_numbers[1])}")
except ValueError:
    print("Something went wrong up there, try your equation again, with numbers this time...")
except IndexError:
    print("Where's the second number?")
