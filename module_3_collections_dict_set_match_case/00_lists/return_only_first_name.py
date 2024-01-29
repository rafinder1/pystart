names = "Adam Mickiewicz, Adam Asnyk, Zbigniew Niecacki"
names = names.split(' ')
first_name = []

for i in range(0, len(names), 2):
    if names[i] not in first_name:
        first_name.append(names[i])

first_name.sort(reverse=True)

print(f"Unique names: {', '.join(first_name)}")