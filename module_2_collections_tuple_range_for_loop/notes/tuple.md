### Features of good tuple

#### To declare, you use bracket
#### Use function tuple(), `Ex. tuple(range(0,3)) -> (0, 1, 2)`
#### Indexing -> `Ex. name[0]`
#### The order is preserved (Kolejność jest zachowana)
### IMMUTABLE!!


#### Example:
```
personal_info = "Rafał", "Protasiuk"
children = (1, 2, 3)
cities = ("Gdynia",)
```

### You do not do that: (IT IS WRONG!!!!!)
```
children[0] = 10
```
#### If you create tuple with one element, you must add comma, because it will not be tuple.

#### If you want to get on element you use `[index]`

#### These things you can do with tuple:
```
(1, 2, 3) * 3 = (1, 2, 3, 1, 2, 3, 1, 2, 3)

a = (1, 2, 3)
b = (4, 5, 6)
a += b
a = (1, 2, 3, 4, 5, 6) (Została utworzona nowa tupla pod zmieną `a`)
```

#### Unpacking tuple
```
first_name, _, last_name = 'Cyprian', 'Kamil', 'Norwid'
```
###### use `_` if you do not use variable (it is convention)

#### Operator IN
```
animal = 'Frog', 'Pig', 'Cow'
'Pig' in animal -> True
```