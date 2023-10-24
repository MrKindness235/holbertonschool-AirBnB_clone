#!/usr/bin/python3
"""A base model for the AirB&B console."""


import datetime

class BaseModel():
    def __init__(self, id="",):
        """Initializes the instance."""
        id = self.id
        
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id_setter(self):
        id = str(id.uuid4())


    def created_at():
        """Anotates when was the instance created."""

    def updated_at():
        """Updates the date note."""
    
    def save(self):
        """Updates."""

    def to_dict(self):
        """Returns keys/values of __dict__."""
