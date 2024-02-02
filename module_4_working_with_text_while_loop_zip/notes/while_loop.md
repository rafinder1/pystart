## while - construction

### 1. Important keyword
### `break` - stop loop
### `continue` - next iteration

### 2. Examples
```python
counter = 0
while counter <= 10:
    counter += 1

counter = 0
while True:
    counter += 1
    if counter == 10:
        break
```


````python
bus_capacity = 100
passengers_in_bus = 0

while bus_capacity >= passengers_in_bus:
    passengers_in_bus += int(input("How many people entered: "))

print("Bus start")
````