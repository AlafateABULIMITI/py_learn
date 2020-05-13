# Built-in Function

`abs(x)`: Return the absolute value of a number.

```python
>>> abs(-1)
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

>>> all([1, 2, 3, 4])
True
>>> all([1, -2, 3, 4])
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

>>> any([1, -2, -3, -4])
True
>>> any([-1, -2, -3, -4])
False
```

`bin(x)`: Convert an integer number to a binary string prefixed with “0b”.

```python
>>> bin(3)
'0b11'
>>> bin(-10)
'-0b1010
```

`callable(object)`: Return `True` if the object argument appears callable, `False` if not.

`chr(i)`: Return the string representing a character whose Unicode code point is the integer `i`.

```python
>>> chr(97)
a
>>> chr(8364)
€
```

`divmod(a, b)`: Take two (non complex) numbers as arguments and return a pair of numbers consisting of their quotient and remainder when using integer division.

`enumerate(iterable, start=0)`: Return an enumerate object.

```python
>>> seasons = ['Spring', 'Summer', 'Fall', 'Winter']
>>> list(enumerate(seasons))
[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
>>> list(enumerate(seasons, start=1))
[(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]
```

`filter(function, iterable)`: Construct an iterator from those elements of iterable for which function returns true. iterable may be either a sequence, a container which supports iteration, or an iterator. If function is `None`, the identity function is assumed, that is, all elements of iterable that are false are removed.

```python
def is_odd(n):
    return n % 2 == 1

newlist = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(newlist)

>>> [1, 3, 5, 7, 9]
```

`class float([x])`: Return a floating point number constructed from a number or string x.

`class frozenset([iterable])`: immutable set.

`getattr(object, name[, default])`: Returns the value of the object naming attribute.

`globals()`: Returns a dictionary of global variables.

`hash()`: hash() is used to get the hash value of an object (string or value, etc.).

```python
>>>hash('test')
2314058222102390712
>>> hash(1)
1
>>> hash(str([1,2,3]))
1335416675971793195
>>> hash(str(sorted({'1':1})))
7666464346782421378
>>>
```

`hex(x)`: Convert integers to lowercase hexadecimal strings prefixed with "0x".

```python
>>> hex(255)
'0xff'
>>> hex(-42)
'-0x2a'
```

`id(object)`: Returns the object's "identified value". This value is an integer that is guaranteed to be unique and constant during the life of this object. Two objects whose lifetimes do not overlap may have the same `id()` value.

```python
>>> b = 1
>>> id(b)
140588731085608
```