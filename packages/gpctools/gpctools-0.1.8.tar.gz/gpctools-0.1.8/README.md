# gpctools

A package for common use tools by the Dev team at GP Joule Connect.

## Tools:
. Decorators:
- exectime: decorator that prints the execution time of a function 

. Generic Methods:
- list_get: A simple method similar to dict.get(), but for lists - It either returns the element of the list at index, if index exists, or None.

## Installation:

```bash
pip install gpctools
```

## Usage:
- exectime:
```python
from gpctools.decorators import exectime

@exectime
def function_x():
    """function code"""

# prints to console: exectime: function_x() took [number of seconds, with 3 decimals]s to run.
```

- list_get:
```python
from gpctools.generic import list_get

example_list = [0, 1, 2, 3]

element1 = list_get(example_list, 1)
print(element1)
# prints to console: 1

element4 = list_get(example_list, 4)
print(element4)
# prints to console: None

element5 = list_get(example_list, 5, default="Element not found")
print(element5)
# prints to console: Element not found
```




