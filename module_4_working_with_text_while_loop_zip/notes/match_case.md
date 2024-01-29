### Alternative to `if`

### Example:
```python
x = 10

match x:
    case 0:
        print("x is equal 0")
    case 10 | 20:
        print("x is equal 10 or 20")
    case 30:
        print("x is equal 30")
    case _:
        print("x is not equal: 0, 10, 20, 30")
```

```python
person = ('Jan', "Kowalski")

match person:
    case ('John', 'Doe'):
        print("Hi John Doe")
    case ('Jan', last_name):
        print(f"Hi Jan {last_name}")
    case (first_name, 'Kowalski'):
        print(f"Hi {first_name} Kowalski")
    case _:
        print("I do not know you ...")
```