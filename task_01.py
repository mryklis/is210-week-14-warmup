#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""import and call pet module"""


from pet import Pet


class Dog(Pet):
    """child to pet"""

    def __init__(self, has_shots=False, **kargs):
        """subclass constructor

        Args:
            has_shots (bool): false
            **kargs: arbitrary argument dictionary
        Attributes:
            has_shots (bool): set to false
        """

        self.has_shots = has_shots
        Pet.__init__(self, **kargs)
