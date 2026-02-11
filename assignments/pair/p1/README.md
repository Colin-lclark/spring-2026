# Pair Project #1: Image Edge Detection

This is a pair programming project. Work with your assigned partner. Only one of
you has to turn it in, but make sure you don't both think the other one was
doing it.

In this project, we are going to detect edges in black-and-white JPEG images
using a process known as convolution. This exercise will build upon what we
learned in the previous assignment (i.e., working with matrices). We are also
going to apply functional decomposition, a topic covered in recent readings.

We will test our work with these two files that are in the Public Domain:

* `rose.jpg`
* `llama.jpg`

## Convolution

The term may sound intimidating. Fortunately it is a little bit like matrix
multiplication but somewhat simpler.

From Wikipedia:

> In image processing, a kernel, convolution matrix, or mask is a small matrix
> used for blurring, sharpening, embossing, edge detection, and more. This is
> accomplished by doing a convolution between the kernel and an image. Or more
> simply, when each pixel in the output image is a function of the nearby pixels
> (including itself) in the input image, the kernel is that function.

## Edge detection

For edge detection, we will use the following kernel:

```python
# Edge detection kernel
k = [
    [ -1, -1, -1 ],
    [ -1,  8, -1 ],
    [ -1, -1, -1 ]
]
```

Now consider pixel `p` and its immediate eight neighbors identified with the
first few letters of the alphabet:

```
a b c
d p f
g h i
```

Then the new value of `p` is computed as

```python
k[0][0]*i + k[0][1]*h + k[0][2]*g + k[1][0]*f + ... + k[2][1]*b + k[2][2]*a
```

We may want to experiment with different 3x3 kernels, so write your code
accordingly.

## Image processing

We will be using the Python Imaging Library (PIL) for this assignment.

At the top of your program, you should import the library:

```python
from PIL import Image
```

Here are common operations you can perform on images:

```python
img = Image.open('rose.jpg')  # load an image for processing
(width, height) = img.size    # get the dimensions of the image
new = img.copy()              # make a copy of the original image
new.show()                    # display the new image on the screen
```

Here is how to get and to set pixels in an image:

```python
img.getpixel((i, j))          # get the pixel at coordinate (i, j)
new.putpixel((i, j), p)       # set the pixel at (i, j) to color p
```

For our images, each pixel will be represented as a three-element tuple
encoding the color of the pixel at that position with the RGB color model. In
this model, the red, green, and blue levels are encoded with values in the
range 0 (absence of color) through 255 (full intensity).

## Hints

* Your program should have at least three functions. What could those functions
  be responsible for? Think about the steps in processing a single pixel of the
  image. We will be doing this design exercise in class so I can guide your
  thinking and we can discuss your solutions.

* When processing pixels on the edge of the image, assume "non existing" pixel
  to have a level of 0 (i.e., black).

* The computation of the new pixel value can stray outside the valid RGB range.
  Make sure to handle this condition by selecting the nearest valid level.

* Since all our images are grayscale, the RGB color encoding of all pixels will
  be a set of three identical levels (e.g.,`(188, 188, 188)`). For computation,
  use any one of these levels (e.g., the first one). When setting a new pixel
  value, replicate the new level in a three-element tuple (e.g, `(new_level,
  new_level, new_level)`) that you can then pass to `putpixel` (which expects
  a tuple).

* You may want to create unit tests for some of your functions.

## What to hand in

Hand in your one file `edge.py`.

Include the names of both participants in a comment at the top of your code (if
one person didn't contribute, don't include their name).