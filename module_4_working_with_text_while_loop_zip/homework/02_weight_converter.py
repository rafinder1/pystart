print("Welcome in Converter!")
print("In this Converter you can changed unit: kilograms (kg), pounds (ib) and ounces (oz)")

convert_from = input("Decide from convert (use above symbols): ").lower()

convert_to = input("Decide to convert (use above symbols): ").lower()

weight = float(input("Give weight: "))
print(convert_from, convert_to, weight)
match convert_from:
    case 'kg':
        result = weight * 2.2062 if convert_to == 'ib' else weight * 35.274

    case 'ib':
        result = weight / 2.2062 if convert_to == 'kg' else weight / 35.274

    case 'oz':
        result = weight / 35.274 if convert_to == 'kg' else weight * 16

    case _:
        print("Wrong unit")
        result = 0
        quit()

print(f"Result: {weight} {convert_from} is equal {result} {convert_to}")
