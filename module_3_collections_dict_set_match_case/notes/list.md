### Features of good list

#### To declare, you use bracket `[]`

#### Use function list(), `Ex. list(range(0,3)) -> [0, 1, 2]`

#### Indexing -> `Ex. name[0]`

#### The order is preserved (Kolejność jest zachowana)

### MUTABLE!! - you can append, remove arguments

#### Example:
```python
fruit = ['mango', 'apple']
fruit[0] = 'orange'
fruit.append('banana')

fruit.remove("apple")
del fruit[1]

instrument = 'Guitar'
instrument = list(instrument)
instrument = ''.join(instrument)
```

#### Methods list:
```python
first_name = ["Jan", "Jack", "Nina", "Nel"]

# Adds a new item to the end of the list
first_name.append("Cristiano")

# Adds a new element at position 1
first_name.insert(1, "Ronaldo")

# Removing the last name and assigning it to a variable
last_first_name = first_name.pop()

# Removing the second name and assigning it to a variable
second_name = first_name.pop(1)

# Clears the list
first_name.clear()
```

```python
names = ['Asia', 'Basia', 'Wojtek', 'Krysia']

# Returns a new sorted list -> function
sorted(names)

# Returns nothing, sorts the original list -> method
names.sort(reverse=True)
```

### Adding and Multiplying lists

```python
# Out: ['python', 'C++', 'Java', 'python', 'C++', 'Java', 'python', 'C++', 'Java']
["python", "C++", "Java"] * 3

# Out: ['Gdynia', 'Warsaw', 'Berlin', 'Paris', 'Madrid']
["Gdynia", "Warsaw", "Berlin"] + ["Paris", "Madrid"]
```

### Iteration from two lists

```python
countries = ['Poland', 'Germany', 'France']
capitals = ['Warsaw', 'Berlin', 'Paris']

print("Country - Capital")
for country, capital in zip(countries, capitals):
    print(country, '-', capital)
```