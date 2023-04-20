#!/usr/bin/python3

#from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(x=x, y=y, width=size, height=size, id=id)

    def __str__(self):
        return(f"[Square] ({self.id}) {self.x}/{self.y} - {width}")

    @property
    def size(self):
        super().width()

    @size.setter
    def size(self, value):
        super().width(value)
        super().height(value)
