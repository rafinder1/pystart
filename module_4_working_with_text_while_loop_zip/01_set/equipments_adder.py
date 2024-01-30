equipments = {"shoes"}

for _ in range(3):
    equipment = input("Give me a equipment: ")

    if equipment in equipments:
        print(f"You have {equipment} in equipments")

    equipments.add(equipment)

print(equipments)
