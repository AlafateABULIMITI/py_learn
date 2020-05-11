# Built-in Function

`abs(x)`: Return the absolute value of a number.

```python
>> abs(-1)
1
```

`all(iterable)`: if all elements are true in this iterable object(list, set, dict).
source code:

```python
def all(iterable):
    for element in iterable:
        if not element:
            return False
    return True

>> all([1, 2, 3, 4])
True
>> all([1, -2, 3, 4])
False
```

`any(iterable)`: if any element is true in this iterable object(list, set, dict).
source code:

```python
def any(iterable):
    for element in iterable:
        if element:
            return True
    return False

>> any([1, -2, -3, -4])
True
>> any([-1, -2, -3, -4])
False
```
