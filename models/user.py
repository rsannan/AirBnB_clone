#!/usr/bin/python3
"""Contains User class
"""


from models.base_model import BaseModel


class User(BaseModel):
    """Inherits from BaseModel
    """
    email = str()
    password = str()
    first_name = str()
    last_name = str()

    def __init__(self, *args, **kwargs):
        """User class constructor
        """
        super().__init__(*args, **kwargs)
