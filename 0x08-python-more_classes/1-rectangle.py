#!/usr/bin/python3
"""A class that defines a rectangle"""


class Rectangle:
    """An empty class that represents a rectangle"""
    def __init__(self, width=0, height=0):
        if width < 0:
            raise ValueError(message="width must be >= 0")
        elif type(width) != int:
            raise TypeError("width must be an integer")
        else:
            self.__width = width
        if height < 0:
            raise ValueError("height must be >= 0")
        elif type(height) != int:
            raise TypeError(message="height must be an integer")
        else:
            self.__height = height

    @property
    def width(self):
        """retrieves width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

    @property
    def height(self):
        """retrieves height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
