#!/usr/bin/python3
class LockedClass:
    """prevents the user from dynamically creating instance attributes."""

    __slots__ = ["first_name"]

    def __init__(self):
        """Initialize an instance of LockedClass."""
        pass
