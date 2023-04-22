#!/usr/bin/python3
"""
    contains class Square which implements classes Rectangle & Base.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        """ initializes the instance fromthe inherited class"""
        super().__init__(x=x, y=y, width=size, height=size, id=id)

    def __str__(self):
        """ returns: a string representation for the object """
        return(f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}")

    @property
    def size(self):
        """ returns: private size attribute, by getter method """
        return super().width

    @size.setter
    """ I am the size setter method """
    def size(self, value):
        if not super().check_type("width", value):
            Rectangle.width = value
        if not super().check_type("height", value):
            Rectangle.height = value

    def update(self, *args, **kwargs):
        """
            assigns key/value argument to attributes
            kwargs is skipped if args is not empty
            Args:
                *args -  variable number of no-keyword args
                **kwargs - variable number of keyworded args
        """
        super().update(*args, **kwargs)

        try:
            self.height = self.size
            self.x = args[2]
            self.y = args[3]

        except IndexError:
            pass

    def to_dictionary(self):
        """ returns dictionary representation of instance """

        return {'id': getattr(self, "id"),
                'size': getattr(self, "width"),
                'x': getattr(self, "x"),
                'y': getattr(self, "y")}
