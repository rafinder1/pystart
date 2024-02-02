### Walrus (Python 3.9)

#### Without walrus
```
>>> a=3
>>> a
3
```

#### With walrus
```
>>> (a:=3)
3
>>> a
3
```

### Example

```python
counter = 0
while counter <= 10:
    counter += 1

i = 0
while (i := i + 1) < 10:
    print(i)

n = int(input())
if n % 2 == 0:
    print(f'Number {n} is even')

if (n:=int(input())) % 2 == 0:
    print(f'Number {n} is even')
```

