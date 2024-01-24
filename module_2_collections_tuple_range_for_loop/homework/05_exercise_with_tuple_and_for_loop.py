# Prepare a tuple storing the name, surname and age of the person. Then
# display this data as:
# First Name: John
# Last Name: Smith
# Age: 40

person_info = "John", "Smith", 40
abstract_info = "First Name", "Last Name", "Age"

# Declare tuples as a=((1,2,3), (4,5,6), (7,8,9)) and then
# traversing them using a for loop display:

for i in range(len(person_info)):
    print(f"{abstract_info[i]}: {person_info[i]}")

a = ((1, 2, 3), (4, 5, 6), (7, 8, 9))

for element in a:
    print(f"{element[0]} + {element[1]} + {element[2]} = {sum(element)}")
