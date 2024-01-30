equipments = []

for _ in range(3):
    equipment = input("Give me a equipment: ")

    if equipment in equipments:
        print(f"You have {equipment} in equipments")

    equipments.append(equipment)

print(equipments)

unique_equipments = set(equipments)
print(unique_equipments)
