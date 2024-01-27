persons = [
    {
        'id': 1,
        'job_title': 'junior developer',
        'name': 'John',
        'programming_language': ['python']
    },
    {
        'id': 2,
        'job_title': 'senior developer',
        'name': 'Mark',
        'programming_language': ['python', 'php']
    },
    {
        'id': 3,
        'job_title': 'stuff developer',
        'name': 'Alex',
        'programming_language': ['php', 'javascript', 'python']
    },
    {
        'id': 4,
        'job_title': 'junior developer',
        'name': 'Bart',
        'programming_language': ['javascript', 'php']
    },
    {
        'id': 5,
        'job_title': 'senior developer',
        'name': 'Carl',
        'programming_language': ['javascript', 'python']
    },
    {
        'id': 6,
        'job_title': 'junior developer',
        'name': 'Martha',
        'programming_language': ['javascript', 'php']
    }
]

language_counter = {}

for person in persons:
    for program in (person['programming_language']):

        param_program = language_counter.get(program, {})
        param_program['quantity'] = param_program.get('quantity', 0) + 1

        list_names = param_program.get('names', [])
        list_names.append(person['name'])
        param_program['names'] = list_names

        language_counter[program] = param_program

print(language_counter)