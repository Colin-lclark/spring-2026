# Note 15

## Puzzle

A for each loop can always be transformed into a while loop.  For example,
consider the following for each loop:

```python
for i in range(10):
    statement1
    statement2
    ...
```

It can be rewritten as a while loop as follows:

```python
i = 0
while i < 10:
    statement1
    statement2
    ...
    i += 1
```

It appears we can simply copy, as is, the body of the for each loop into the
while loop and add the update to the index variable to complete the
transformation.  Can you think of any cases where this simple transformation
will *not* work?
