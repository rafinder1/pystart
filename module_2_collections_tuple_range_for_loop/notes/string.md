### Features of good tuple

#### To declare, you use apostrophe `''`
#### Use function str(), `Ex. str("something")`
#### Indexing -> `Ex. name[0]`
#### The order is preserved (Kolejność jest zachowana)
### IMMUTABLE!!

#### Useful functions
```python
name = 'PyStart'
name.upper()
name.lower()
name.replace('Start', 'WWW')
name.find('Py') # -> return 0 because find start 'Py' on the first place
name.find('Start') # -> return 2 because find start 'Py' on the first place
```
```python
fruits = 'lemon', 'apple', 'peach', 'melon'
" ".join(fruits)

fruits = 'lemon,apple,peach,melon'
fruits.split(',')
```
```python
string = 'Coding in Python, Python is good decision'
string.count('Python')

string.startswith("Coding")

'a'.isnumeric() # -> False
'a'.isalpha() # -> True
'221'.isnumeric() # -> True
```