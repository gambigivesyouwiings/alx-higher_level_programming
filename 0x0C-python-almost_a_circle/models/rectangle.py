#!/usr/bin/python3

#from model.base import Base

class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base. __nb_objects


class Rectangle(Base):
    """ This is the rect class 
    Methods: __init__, check_type, area
    """
    @staticmethod
    def check_type(attribute, input):
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
        """I'm the 'width' property."""
        return self.__width

    @width.setter
    def width(self, value):
        if not Rectangle.check_type("width", input=value):
            self.__width = value

    @property
    def height(self):
        """I'm the 'height' property."""
        return self.__height

    @height.setter
    def height(self, value):
        if not Rectangle.check_type("height", input=value):
            self.__height = value

    @property
    def x(self):
        """I'm the 'x' property."""
        return self.__x

    @x.setter
    def x(self, value):
        if not Rectangle.check_type("x", input=value):
            self.__x = value

    @property
    def y(self):
        """I'm the 'y' property """
        return self.__y

    @y.setter
    def y(self, value):
        if not Rectangle.check_type("y", input=value):
            self.__y = value

    def area(self):
        ans = self.__width * self.__height
        return ans

    def display(self):
        for item in range(0, self.__height):
            for num in range(0, self.__width):
                print("#", end="")
            print("")

    def __str__(self):
        """
            returns a string formart of the rectangle
        """
        return(f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}")

    def update(self, *args, **kwargs):
        """ sets instance attributes to new values """

        if len(args) == 0:
            for key,value in kwargs.items:
                self.__setatr__(key, value)
        else:
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            except IndexError:
                pass


if __name__ == "__main__":

    r1 = Rectangle(4, 6)
    r1.display()

    print("---")

    r1 = Rectangle(2, 2)
    r1.display()

    r1 = Rectangle(4, 6, 2, 1, 12)
    print(r1)

    r2 = Rectangle(5, 5, 1)
    print(r2)

    r1 = Rectangle(10, 10, 10, 10)
    print(r1)

    r1.update(89)
    print(r1)

    r1.update(89, 2)
    print(r1)

    r1.update(89, 2, 3)
    print(r1)

    r1.update(89, 2, 3, 4)
    print(r1)

    r1.update(89, 2, 3, 4, 5)
    print(r1)
