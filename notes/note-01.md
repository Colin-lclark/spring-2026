# Note 01

Welcome to CS 172!

## A snippet of a Python program

```python
# --- If 1/1/1980 is Day 1, and today is Day d counting from there,
# --- determine the Year y of today.
y = 1980
while d > 365:
    if leapYear(y):
        if d > 366:
            d = d - 366
            y = y + 1
    else:
        d = d - 365
        y = y + 1
# Today is in Year y
```

Activities:

* Study the snippet on your own. Can you make sense of it? Could you have
  guessed what it is doing if you had only known about C? What are the important
  components of this code?

* Share your answers with your neighbor.

* Share with your neighbor at least one aspect of Python that is similar to C
  and one aspect where it is different.

* Convince your neighbor that this snippet is implementing correctly/incorrectly
  its intentions described in the comments.

* Individually, think about the kinds of strategies you would use to convince
  yourself that this snippet is doing what it is intending to do.
  
* Share your thoughts with your neighbor.
