# Pair Project #3: Sudoku Solver

This is a pair programming project. Work with your assigned partner. Only one
of you has to turn it in, but make sure you don't both think the other one was
doing it.

## Overview

You will complete a program to solve Sudoku puzzles. If you are not familiar
with this type of puzzle, you can try some online.

I have provided the following files:

* [`sudoku.py`](./sudoku.py), a skeleton of the main program
* [`sudoku_test.py`](./sudoku_test.py), a pytest file for sudoku
* [`sudoku1.txt`](./sudoku1.txt), a sample puzzle

Your job is simply to complete `sudoku.py`. Do not modify any of the other
files.

## Hints

Run all of the tests first. They should all fail.

Work through the tests in the order in which they appear in `sudoku_test.py`.
Figure out which functions you need to complete to get each one to pass. Pass
each test before moving on to the next one.

As you write each function, consider calling one or more of the previous
functions. That's why they're there!

Note that `create_squares` takes a single parameter called `diagram`. That
parameter is followed by an assignment (`= None`). This is called a parameter
with a default. It gives the caller the option to call this function without any
argument in which case the parameter is assigned the default value that is the
result of the evaluation of the expression that follows the assignment operator.
If the caller passes a value to the function, then that value supersedes the
default value.

## What to hand in

Hand in your your version of `sudoku.py`.

Include the names of both participants in a comment at the top of your code (if
one person didn't contribute, don't include their name).
