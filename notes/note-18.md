# Note 18

## Puzzle

Compare the execution of

```python
def fac(n):
    if n == 1: return 1
    return n*fac(n - 1)

fac(3)
```

and

```python
def fac2(n):

    def helper(n, a):
        if n == 1: return a
        return helper(n - 1, n*a)

    return helper(n, 1)

fac2(3)
```

Do they produce the same answer? What is the difference?
