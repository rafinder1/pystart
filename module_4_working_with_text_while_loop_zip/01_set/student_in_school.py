students = {
    ("Piotr", "Kowalczyk"),
    ("Katarzyna", "Mazur"),
    ("Tomasz", "Adamski"),
    ("Agnieszka", "Kaczmarek"),
    ("Krzystof", "Krawczyk")
}

going_on_trip = {
    ("Katarzyna", "Mazur"),
    ("Tomasz", "Adamski"),
    ("Krzystof", "Krawczyk")
}

student_in_school = students - going_on_trip

print(f"Student in School: {student_in_school}")
