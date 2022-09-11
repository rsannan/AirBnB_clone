#!/usr/bin/python3
"""Contains the BaseModel class
"""


import models
import uuid
from datetime import datetime


formated_time = "%Y-%m-%dT%H:%M:%S.%f"
now = datetime.now()


class BaseModel:
    """Defines all common attributes/methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """BaseModel Class Constructor
        """
        if kwargs:
            for k, v in kwargs.items():
                if v is not self.__class__.__name__:
                    self.__dict__[k] = v
            if hasattr(self, "created_at") and type(self.created_at) is str:
                self.created_at = datetime.strptime(
                    kwargs["created_at"], formated_time
                )

            if hasattr(self, "updated_at") and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(
                    kwargs["updated_at"], formated_time
                )

        else:
            id = uuid.uuid4()
            self.id = str(id)
            self.created_at = now
            self.updated_at = self.created_at
            models.storage.new(self)
            models.storage.save()

    def __str__(self):
        """Returns a neatly formated string representation
        """
        str_repr = "[{:s}] ({:s}) {}".format(
                                        self.__class__.__name__,
                                        self.id, self.__dict__)
        return str_repr

    def save(self):
        """Updates the public instance attribute updated_at\
            with the current datetime
        """
        self.updated_at = now
        models.storage.save()

    def to_dict(self):
        """ returns a dictionary containing all keys/values\
            of __dict__ of the instance
        """
        my_dict = self.__dict__.copy()
        if "created_at" in my_dict:
            my_dict["created_at"] = my_dict["created_at"].strftime(
                formated_time
            )

        if "updated_at" in my_dict:
            my_dict["updated_at"] = my_dict["updated_at"].strftime(
                formated_time
            )

        my_dict["__class__"] = self.__class__.__name__
        return (my_dict)
