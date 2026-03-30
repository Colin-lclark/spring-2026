# Note 26

## Optional arguments

Python provides the means to mark a function argument as optional. To do so you
must supply a default value. You indicate the default value by following the
argument name with the assignment operator and an expression (see an example in
the class definition below).

## Operator overloading

An operator that behaves differently depending on the types of its operands is
said to be *overloaded*.

Python provides the programmer the means to overload most of its operators.
Here is a subset of these overloadable operators along with the corresponding
magic methods that would need to be defined.

Operator | Magic method
-|-
`==`     | `__eq__(self, other)`
`!=`     | `__ne__(self, other)`
`+`      | `__add__(self, other)`
`-`      | `__sub__(self, other)`
`*`      | `__mul__(self, other)`
`/`      | `__truediv__(self, other)`
