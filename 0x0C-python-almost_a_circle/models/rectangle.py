#!/usr/bin/python3
"""
    contains class Rectangle which implements Base.
"""
from models.base import Base


class Rectangle(Base):
    """ This is the rect class
        methods: __init__, check_type, area
    """
    @staticmethod
    def check_type(attribute, input):
        """ Checks if inputs to an attribute meets requirements
            returns: True if exception """

        if type(input) != int:
            raise TypeError(f"{attribute} must be an integer")
            return True
        if attribute in ("x", "y") and input < 0:
            raise ValueError(f"{attribute} must be >= 0")
            return True
        if attribute in ("width", "height") and input <= 0:
            raise ValueError(f"{attribute} must be > 0")
            return True

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializes instance """

        super().__init__(id)
        if not Rectangle.check_type("width", input=width):
            self.__width = width
        if not Rectangle.check_type("height", input=height):
            self.__height = height
        if not Rectangle.check_type("x", input=x):
            self.__x = x
        if not Rectangle.check_type("y", input=y):
            self.__y = y

    @property
    def width(self):
        """I'm the 'width' property.
            Returns: width"""
        return self.__width

    @width.setter
    def width(self, value):
        """ I am the setter """
        if not Rectangle.check_type("width", input=value):
            self.__width = value

    @property
    def height(self):
        """I'm the 'height' property.
            returns setter """
        return self.__height

    @height.setter
    def height(self, value):
        """ Height setter """
        if not Rectangle.check_type("height", input=value):
            self.__height = value

    @property
    def x(self):
        """I'm the 'x' property.
        returns: x"""
        return self.__x

    @x.setter
    def x(self, value):
        """ x.setter method """
        if not Rectangle.check_type("x", input=value):
            self.__x = value

    @property
    def y(self):
        """I'm the 'y' property """
        return self.__y

    @y.setter
    def y(self, value):
        """ I'm the  setter """
        if not Rectangle.check_type("y", input=value):
            self.__y = value

    def area(self):
        """
            contains class Rectangle which implements Base.
        """
        ans = self.__width * self.__height
        return ans

    def display(self):
        """
            prints to stdout the Rectangle instance with '#'
        """
        for item in range(0, self.__height):
            for num in range(0, self.__width):
                print("#", end="")
            print("")

    def __str__(self):
        """
            returns a string formart of the rectangle
        """
        return (f"[Rectangle] {self.id}) {self.__x}/" +
                f"{self.__y} - {self.__width}/{self.__height}")

    def update(self, *args, **kwargs):
        """ sets instance attributes to new values """

        if len(args) == 0:
            for key, value in kwargs.items():
                self.__setattr__(key, value)
        else:
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            except IndexError:
                pass

    def to_dictionary(self):
        """ returns: A dictionary representation of the instance """

        return {"id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y}
