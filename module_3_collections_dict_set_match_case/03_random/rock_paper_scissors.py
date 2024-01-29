import random

available_options = ('r', 'p', 's')
user = input("Give me r/p/s (rock/paper/scissor): ")

computer = random.choice(available_options)

if user == computer:
    print("Draw")
    quit()
elif ((user == 'p' and computer == 'r') or
      (user == 's' and computer == 'p') or
      (user == 'r' and computer == 's')):
    print('You Win')
else:
    print('You Lose')

print(f'AI have {computer}')