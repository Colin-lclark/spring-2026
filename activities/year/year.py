def leap_year(y):
    """Return True if y is a leap year."""
    return False

def year(d):
    """If 1/1/1980 is Day 1, and today is Day d counting from there, return the
    Year y of today."""
    y = 1980
    while d > 365:
        if leap_year(y):
            if d > 366:
                d = d - 366
                y = y + 1
        else:
            d = d - 365
            y = y + 1
    return y
