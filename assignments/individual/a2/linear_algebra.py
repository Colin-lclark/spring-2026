"""A linear algebra module.

This is a collection of functions dealing with vectors and matrices.
"""

__author__ = 'Colin Sheehan'

import math

def vmagnitude(v : list[float]) -> float:
    """Returns the magnitude of the vector v (which may be of any
    length).

    This is found by adding up the squares of all of the elements of v
    and taking the square root of the total.
    """
    magnitude = 0
    for point in v:
        magnitude += point**2
    
    return math.sqrt(magnitude)


def vsum(v : list[float], w : list[float]) -> list[float]:
    """Returns the sum of vectors v and w.

    This is a vector of the same length, each of whose elements is the
    sum of the corresponding elements in v and w.
    """
    vsum = []
    index = 0
    while(index < len(v)):
        vsum.append(v[index]+w[index])
        index += 1
    return vsum

def vdifference(v : list[float], w : list[float]) -> list[float]:
    """Returns the difference between vectors v and w.

    This is a vector of the same length, each of whose elements is the
    difference between the corresponding elements in v and w.
    """
    vdif = []
    index = 0
    while(index < len(v)):
        vdif.append(v[index]-w[index])
        index += 1
    return vdif

def velementwise_product(v : list[float], w : list[float]) -> list[float]:
    """Returns the element-wise between vectors v and w.

    This is a vector of the same length, each of whose elements is the
    product of the corresponding elements in v and w.
    """
    vprod = []
    index = 0
    while(index < len(v)):
        vprod.append(v[index]*w[index])
        index += 1
    return vprod

def vdot_product(v : list[float], w : list[float]) -> float:
    """Returns the dot product of vectors v and w.

    This is the sum of the products of the corresponding elements.
    """
    vprod = velementwise_product(v, w)
    vdot = 0
    for product in vprod:
        vdot += product
    return vdot

def mdimensions(m : list[list[float]]) -> list[int]:
    """Returns, as an array of two elements, the dimensions of matrix m."""
    return [len(m), len(m[0])]

def msum(m : list[list[float]], n : list[list[float]]) -> list[list[float]]:
    """Returns the element-wise sum of matrices m and n."""
    msum = []
    row = 0
    while row < len(m):
        msum.append([])
        column = 0
        while column < len(m[row]):
            msum[row].append(m[row][column] + n[row][column])
            column += 1
        row += 1
    return msum      

def melementwise_product(m : list[list[float]], n : list[list[float]]) -> list[list[float]]:
    """Returns the element-wise product of matrices m and n."""
    mprod = []
    row = 0
    while row < len(m):
        mprod.append([])
        column = 0
        while column < len(n[row]):
            mprod[row].append(m[row][column] * n[row][column])
            column += 1
        row += 1
    return mprod

def mtranspose(m : list[list[float]]) -> list[list[float]]:
    """Returns the transpose of m, that is, a matrix where element i, j
    is element j, i from m.
    """
    msum = []
    row = 0
    while row < len(m[0]):
        msum.append([])
        column = 0
        while column < len(m):
            msum[row].append(m[column][row])
            column += 1
        row += 1
    return msum


def mproduct(m : list[list[float]], n : list[list[float]]) -> list[list[float]]:
    """Returns the matrix product of m and n.

    (Search the web for a definition.)
    """
    mprod = []
    row = 0
    while row < len(m):
        mprod.append([])
        column = 0
        while column < len(n[0]):
            index = 0
            product = 0
            while index < len(n):
                product += m[row][index] * n[index][column]
                index += 1
            mprod[row].append(product)
            column += 1
        row += 1
    return mprod