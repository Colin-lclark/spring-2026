# Note 11

## Puzzle

What is the value returned by evaluating the Python expression `3 * 0.1 == 0.3'?

## References

In Python *everything* is a reference.

According to
[wikipedia](https://en.wikipedia.org/wiki/Reference_(computer_science)),
*reference* is

> a value that enables a program to indirectly access a particular datum.

### Immutable types

When say that a type is *immutable* when the following condition is true when a
new value of that type is created:

> The new value is bound to a *fixed* reference for the rest of its lifetime.

### Pitfalls

The following functions do not necessarily do what you expect.

```python
def vsum(v : list[float], w : list[float]) -> list[float]:
    """Returns the sum of vectors v and w."""
    for i in range(len(v)):
        v[i] += w[i]
    return v
```

```python
def create_matrix(n : int, m : int) -> list[list[float]]:
    """Returns an n x m matrix filled with 0.0."""
    row = [0.0]*m
    mat = []
    for i in range(n):
        mat.append(row)
    return mat
```
