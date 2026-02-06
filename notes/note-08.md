# Note 08

## Puzzle

What does the expression `[0.0] * 10` evaluate to?

## Tuples

A tuple is an ordered, finite sequence of values. In Python, a tuple is created
as a comma-separated list of values. I recommend enclosing the list with a pair
of parentheses. Tuple share some of the same attributes as arrays. You can
access a specific value by indexing in the tuple and find its arity with `len`.
Finally, a tuple is a form of data collection. Therefore you can use the `for`
loop to iterate over its components.

## Side effects

A function that can change its environment is said to have a side effect. A
function that does not have any side effect (i.e., only returns a value) is said
to be pure.

## Functional decomposition

A long program can be greatly improved by breaking it down into multiple
functions. This discipline has many advantages:

* Redundant code (repeating the same statements in several places) is avoided,
  making the code shorter.
* The structure of the code is made clearer, making the code easier to read and
  write.
* Individual functions can be tested, making the code easier to debug.
* Functions can often be reused to solve other problems.

A well-designed function should do only one thing: either return a value or have
some side effect (modify a data structure in memory, draw something on the
screen, etc.).

## Documentation

It is a good idea to include a docstring at the beginning of each module and
each function. It should describe what the module or function does. By
convention this docstring appears early in the program text.

In your assignment submissions, I'd like you to include a line that identifies
who wrote the solution. Note that this is not a standard convention in Python.

```python
"""A linear algebra module."""

__author__ = 'Jane Doe'

import math

def vmagnitude(v : list[float]) -> float:
    """Returns the magnitude of the vector v (which may be of any length).
    ...
```
