import random

random_number = random.randint(1, 100)

print("Start Game")
print("Guess number: (number range 1 - 100)")
number_attempts = 0
while True:
    user_number = int(input("Give me number: "))

    number_attempts += 1
    if user_number > random_number:
        print("Too big. Try again!")
    elif user_number < random_number:
        print("Too small. Try again!")
    else:
        print("You win!")
        print(f"You need {number_attempts} numbers.")
        break
