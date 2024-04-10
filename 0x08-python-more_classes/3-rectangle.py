#!/usr/bin/python3
"""3. String representation"""


class Rectangle:
    """Class Rectangle that defines a rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize rectangle with given width and height."""
        self.height = height
        self.width = width

    @property
    def height(self):
        """Retrieve the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """Retrieve the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """Compute the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Compute the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return a string representation of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ""

        rectangle = "#" * self.__width + "\n"
        rectangle += ("#" + " " * (self.__width - 2) + "#\n") * (self.__height - 2)
        rectangle += "#" * self.__width

        return rectangle

    def __repr__(self):
        """Return a string representation of the rectangle object."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Print a message when the rectangle object is deleted."""
        print("Bye rectangle...")


if __name__ == "__main__":
    r1 = Rectangle(4, 2)
    print("Area: {} - Perimeter: {}".format(r1.area(), r1.perimeter()))
    print(r1)

    r2 = Rectangle(10, 3)
    print("Area: {} - Perimeter: {}".format(r2.area(), r2.perimeter()))
    print(r2)
