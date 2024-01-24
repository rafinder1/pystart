### Operator : to cut

### `name[start:end:step]`

### Example

```python
numbers = tuple(range(1, 101))
print(numbers[:10])  # -> The first ten elements tuple
print(numbers[-10:])  # -> The last ten elements tuple
print(numbers[::2])  # -> Only odd elements
print(numbers[::-2])  # -> Only even elements (descending)
```