#!/usr/bin/python3
"""Rectangle Module."""
from models.base import Base


class Rectangle(Base):
    """Rectangle class, inherited from Base class."""

    def __init__(self, width, height, x=0, y=0, id_num=None):
        """Construct a Rectangle object."""
        super().__init__(id_num)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @staticmethod
    def check_int(val, attr):
        """Check if val is integer."""
        if not isinstance(val, int):
            raise TypeError(f'{attr} must be an integer')

    @property
    def width(self):
        """Get width."""
        return self.__width

    @property
    def height(self):
        """Get height."""
        return self.__height

    @property
    def x(self):
        """Get x."""
        return self.__x

    @property
    def y(self):
        """Get y."""
        return self.__y

    @width.setter
    def width(self, val):
        """Set width."""
        Rectangle.check_int(val, "width")
        if val <= 0:
            raise ValueError("width must be > 0")
        self.__width = val

    @height.setter
    def height(self, val):
        """Set height."""
        Rectangle.check_int(val, "height")
        if val <= 0:
            raise ValueError("height must be > 0")
        self.__height = val

    @x.setter
    def x(self, val):
        """Set x."""
        Rectangle.check_int(val, "x")
        if val < 0:
            raise ValueError("x must be >= 0")
        self.__x = val

    @y.setter
    def y(self, val):
        """Set y."""
        Rectangle.check_int(val, "y")
        if val < 0:
            raise ValueError("y must be >= 0")
        self.__y = val

    def area(self):
        """Compute area of Rectangle."""
        return self.width * self.height

    def display(self):
        """Print Rectangle."""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            for _ in range(self.x):
                print(' ', end='')
            for _ in range(self.width):
                print('#', end='')
            print()

    def __str__(self):
        """Get string representation of Rectangle."""
        return (f'[Rectangle] ({self.id}) {self.x}/{self.y}'
                + f' - {self.width}/{self.height}')

    def update(self, *args, **kwargs):
        """Update Rectangle."""
        if not args:
            if not kwargs:
                return

            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)
        else:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]

    def to_dictionary(self):
        """Convert object dictionary."""
        return {'id': self.id, 'width': self.width, 'height': self.height,
                'x': self.x, 'y': self.y}

    def to_csv_string(self):
        """Convert object to csv string."""
        return f'{self.id},{self.width},{self.height},{self.x},{self.y}'

    @staticmethod
    def from_csv_to_obj(csv_string):
        """Convert csv string into dictionary."""
        attr_list = csv_string.split(',')
        return Rectangle(int(attr_list[1]), int(attr_list[2]),
                         int(attr_list[3]), int(attr_list[4]),
                         int(attr_list[0]))
