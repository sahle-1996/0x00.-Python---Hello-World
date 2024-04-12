#!/usr/bin/python3
"""Tests for the text_indentation function."""

import doctest

def test_text_indentation():
    """
    Test cases for text_indentation function.
    >>> text_indentation("Hello. How are you?")
    Hello.
    
    How are you?
    
    >>> text_indentation("This is a test sentence.")
    This is a test sentence.
    
    >>> text_indentation("A question? Sure.")
    A question?
    
    Sure.
    
    >>> text_indentation("Multiple?? Periods... Here!")
    Multiple?
    
    Periods...
    
    Here!
    """

if __name__ == "__main__":
    doctest.testmod()
