# Note 04

## Puzzle

What is the result of `round(1.5)`? What is the result of `round(2.5)`? Can you
justify this behavior?

## Unit testing

Unit testing checks individual parts of a program (typically individual
functions). It is not meant to be exhaustive. Instead, it is meant to run
quickly (so it can be run often) and to catch obvious mistakes (e.g., off-by-one
mistakes). For instance, unit tests would check corner cases (e.g., division by
zero, access the first element, access the last element, etc.).

To make it even easier to do unit testing, most languages offer multiple
frameworks. We will be using `pytest`.
