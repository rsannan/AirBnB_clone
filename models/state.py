#!/usr/bin/python3
"""Contains the State class
"""


from models.base_model import BaseModel


class State(BaseModel):
    """Inherits from BaseModel
    """
    name = str()

    def __init__(self, *args, **kwargs):
        """State Class Constructor
        """
        super().__init__(*args, **kwargs)
