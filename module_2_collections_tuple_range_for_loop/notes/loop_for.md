## For loop

#### Example: 
```python
fruits = 'apple', 'banana', 'mango'
for fruit in fruits: # iterate over tuples
    print(fruit)
```

```python
fruits = 'apple', 'banana', 'mango'
for index, fruit in enumerate(fruits): # iterate over tuples with enumerate. We can access to index and elements.
    print(index, fruit)
```

```python
fruits = 'apple', 'banana', 'mango'
for fruit in reversed(fruits): # iterate from end
    print(fruit)
```

```python
fruits = 'apple', 'banana', 'mango'
for fruit in sorted(fruits): # iterate over the sorted list
    print(fruit)
```