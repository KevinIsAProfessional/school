def power(a, b):
    if b == 0:
        result = 1
    else:
        result = power(a, b - 1) * a
    return result


def square(a):
    """
    >>> square(0)
    0
    >>> square(1)
    1
    >>> square(2)
    4
    """
    return power(a, 2)


def cube(a):
    """
    >>> cube(0)
    0
    >>> cube(1)
    1
    >>> cube(2)
    8
    """
    return power(a, 3)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
