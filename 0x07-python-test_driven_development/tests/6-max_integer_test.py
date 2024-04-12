def test_max_integer():
    """
    Test cases for the max_integer function.

    >>> max_integer([1, 2, 3, 4, 5])
    5

    >>> max_integer([-5, -4, -3, -2, -1])
    -1

    >>> max_integer([])
    None

    >>> max_integer([10])
    10

    >>> max_integer([0, 0, 0, 0])
    0

    >>> max_integer(["a", "b", "c"])
    Traceback (most recent call last):
        ...
    TypeError: '>' not supported between instances of 'str' and 'int'
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()
