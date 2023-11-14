#!/usr/bin/python3
"""Square module."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class, that inherits from Rectangle."""

    def __init__(self, size, x=0, y=0, id_num=None):
        """Construct Square object."""
        super().__init__(size, size, x, y, id_num)

    def __str__(self):
        """Convert object to string."""
        return f'[Square] ({self.id}) {self.x}/{self.y} - {self.width}'

    @property
    def size(self):
        """Get size."""
        return self.width

    @size.setter
    def size(self, val):
        """Set size."""
        self.width = val
        self.height = val

    def update(self, *args, **kwargs):
        """Update Square."""
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
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]

    def to_dictionary(self):
        """Convert object to dictionary."""
        new_dict = super().to_dictionary()
        new_dict.pop('height')
        new_dict['size'] = new_dict.pop('width')
        return new_dict

    def to_csv_string(self):
        """Convert object to csv string."""
        return f'{self.id},{self.size},{self.x},{self.y}'

    @staticmethod
    def from_csv_to_obj(csv_string):
        """Convert csv string into dictionary."""
        attr_list = csv_string.split(',')
        return Square(int(attr_list[1]), int(attr_list[2]),
                      int(attr_list[3]), int(attr_list[0]))
