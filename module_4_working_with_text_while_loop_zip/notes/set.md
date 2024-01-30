### Features of good tuple

#### Use function set() and curly brackets

```python
exercise = {1, 2, 1, 2, 3, 4, 5, 4, 3, 2} 
print(type(exercise)) # Out -> <class 'set'>

tuple_number = 1, 2, 1, 2, 3, 4, 5, 4, 3, 2
exercise = set(tuple_number)
print(type(exercise)) # Out -> <class 'set'>
```
### Are disordered (nieuporządkowane)
### Only unique value

#### We can add new values
```python
friends = {'Alex', 'Tom', 'Bart'}
friends.add('Michael')
print(friends)
```


#### Additional operations can be performed
#### - sum of the set
#### - subtraction of the set
#### - part of the common