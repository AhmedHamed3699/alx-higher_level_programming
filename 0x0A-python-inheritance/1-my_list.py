#!/usr/bin/python3
"""A module for a class printing list in order."""


class MyList(list):
    """Class MyList, derived from list."""

    def print_sorted(self):
        """Print array sorted."""
        tmp_list = self.copy()
        tmp_list.sort()
        print(tmp_list)
