import random

available_options = ('r', 'p', 's')
user = input("Give me r/p/s (rock/paper/scissor): ")

computer = random.choice(available_options)

if user == computer:
    print("Draw")
    quit()
if user == 'p':
    if computer == 'r':
        print('You Win')
    else:
        print('You Lose')
elif user == 'r':
    if computer == 'p':
        print('You Lose')
    else:
        print('You Win')
else:
    if computer == 'r':
        print('You Lose')
    else:
        print('You Win')

print(f'AI have {computer}')