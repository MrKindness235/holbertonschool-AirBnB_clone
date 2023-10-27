#!/usr/bin/python3
"""A file storage engine."""

import json

class FileStorage():
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns all objects."""
        return self.__objects
    
    def new(self, obj):
        """Defines a new object."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        jsonDict = {}
        for key, value in self.__objects.items():
            jsonDict[key] = value.to_dict()
        with open(self.__file_path, mode="w", encoding="utf-8") as file:
            json.dump(jsonDict, file)

    def reload(self):
        """Deserializes the JSON file to __objects (only if it already exists)"""

        from models.base_model import BaseModel

        with open(self.__file_path, mode="r") as file:
            data = json.load(file)
            for key, value in data.items():
                self.__objects[key] = BaseModel(**value)
