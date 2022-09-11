#!/usr/bin/python3
"""Contains the Amenity class
"""


from models.base_model import BaseModel


class Amenity(BaseModel):
    """Inherits from BaseModel
    """
    name = str()

    def __init__(self, *args, **kwargs):
        """Amenity class Constructor
        """
        super().__init__(*args, **kwargs)
