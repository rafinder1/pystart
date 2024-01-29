### Features of good Dictionary

#### `key` and `value`

#### keys are most often `string`, they can be any `immutable` object: `int`, `float`, `str`, `tuple`

#### To declare, you use bracket `{}`
#### Use function `dict()` 
```python
dict(first_name = "Rafal")
{"first_name":"Rafal"}
```

### MUTABLE!! - you can append, remove arguments

#### Use method .get()
```python
character = dict(first_name = "rafal")
print(character["age"]) # Out -> KeyError: 'age'
character.get("age") # Out -> None
character.get("age", 21) # Out -> Default value: 21, do not added to dict, but only returned
```

#### Use method .update()
```python
character = dict(first_name="rafal")
params = {"run": 10, "shoot": 9}
character.update(params)
```

#### Iteration
```python
capitals = {"Poland": "Warsaw", "Germany": "Berlin", "France": "Paris"}
for country in capitals:
    print(country)
    print(capitals[country])

for country, capital in capitals.items():
    print(country)
    print(capital)
```