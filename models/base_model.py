#!/usr/bin/python3
"""A base model for the AirB&B console."""


from datetime import datetime
from uuid import uuid4

class BaseModel():
    def __init__(self, *args, **kwargs):
        """Initializes the instance."""
        if kwargs:
            
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def save(self):
        """Updates the updated."""

        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns keys/values of __dict__."""
        new_dict = self.__dict__.copy()
        new_dict.update({"created_at": self.created_at.isoformat()})
        new_dict.update({"updated_at": self.updated_at.isoformat()})
        new_dict.update({"__class__": self.__class__.__name__})
        return new_dict

        

    def __str__(self):
        """Must print: [<class name>] (<self.id>) <self.__dict__>"""

        return (f"[{self.__class__.__name__}] ({self.id}) {self.to_dict()}")
