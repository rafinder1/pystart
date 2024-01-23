numbers = 1, 2, 3, 4
for i in reversed(numbers):
    print(numbers[:i])

for counter in reversed(range(1, 5)):
    for digit in range(1, counter + 1):
        print(digit, end=' ')
    print('')
