#!/usr/bin/python3
"""Define a Rectangle that inherits from Base"""


from models.base import Base


class Rectangle(Base):
    """Represents a class Rectangle that inherits from class Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes the rectangle"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
