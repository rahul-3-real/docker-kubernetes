from random import randint

min_number = int(input("Please enter a minimum number: "))
max_number = int(input("Please enter a maximum number: "))


if max_number < min_number:
    print("Invalid input - shutting down...")
else:
    rnd_number = randint(min_number, max_number)
    print(f"The random number between {min_number} and {max_number} is: {rnd_number}")
