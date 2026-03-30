# Note 25

## Classes

### Initializers

During our last lecture, we saw that we could add a special function, called
`__init__`, to our class definition to specify how a new instance of that class
should be initialized.

```python
class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
```

### Methods

Functions defined in a `class` are often referred to as *methods*. We just saw
one such method, that is, `__init__`.

### Defining methods

Methods are defined exactly like regular functions, but with two differences:

* methods are defined inside a class, and
* methods have an extra first argument `self`.

Let's add a new method.

```python
class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def conjugate(self):
        return Complex(self.real, -self.imag)
```

### Magic methods

We just say how to define initializers to give your instance variables initial
value. The name of an initializer method follows a strict convention: it must be
`__init__`, including the double underscores on both ends.

Python specifies several other special names for methods that many classes will
have. Because these methods cause certain things to happen automatically, they
are sometimes called magic methods.

#### String representation

There are at least two times when Python might try to convert an object to a
string:

* When you pass the object to the `str` function, which calls the magic method `__str__`.
* When you pass the object to the `repr` function, which calls the magic method `__repr__`. This happens automatically when displaying the object in the interactive interpreter.

You *could* define these two methods differently if, for example, you wanted a concise representation for printing but a detailed one for debugging. Since
you'll usually want them to the be the same, by default `__str__` just calls `__repr__`. This means that **if you only want to define one, define
`__repr__`**.

#### Equality

Unless you define an appropriate method (`__eq__`), two distinct objects are
considered different even if their contents match.

#### Put it all together

```python
class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __repr__(self):
        return repr(self.real) + ' + ' + repr(self.imag) + 'i'

    def __eq__(self, other):
        return self.real == other.real and self.imag == other.imag

    def conjugate(self):
        return Complex(self.real, -self.imag)
```

### Activity

Define a class for circles that takes a radius as an argument and defines the
area and circumference methods with the obvious meanings.
