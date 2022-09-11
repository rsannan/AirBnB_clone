#!/usr/bin/python3
"""Contains the Review class
"""


from models.base_model import BaseModel


class Review(BaseModel):
    """Inherits from BaseModel
    """
    place_id = str()
    user_id = str()
    text = str()

    def __init__(self, *args, **kwargs):
        """Review class constructor
        """
        super().__init__(*args, **kwargs)
