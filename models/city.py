#!/usr/bin/python3
"""Contains the City class
"""


from models.base_model import BaseModel


class City(BaseModel):
    """Inherits from BaseModel
    """
    state_id = str()
    name = str()

    def __init__(self, *args, **kwargs):
        """City class constructor
        """
        super().__init__(*args, **kwargs)
