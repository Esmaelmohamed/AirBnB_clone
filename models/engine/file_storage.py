#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel


class FileStorage:
    """A class for handling abstracted storage."""

    def __init__(self):
        """Initialize FileStorage class."""
        self._file_path = "file.json"
        self._objects = {}

    def all(self):
        """Retrieve all stored objects."""
        return self._objects

    def new(self, obj):
        """Add a new object to the storage."""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self._objects[key] = obj

    def save(self):
        """Serialize objects to JSON and save to file."""
        serialized = {key: obj.to_dict() for key, obj in self._objects.items()}
        with open(self._file_path, "w") as f:
            json.dump(serialized, f)

    def reload(self):
        """Deserialize JSON file and reload objects."""
        try:
            with open(self._file_path) as f:
                data = json.load(f)
                for key, val in data.items():
                    cls_name = val['__class__']
                    del val['__class__']
                    obj = eval(cls_name)(**val)
                    self.new(obj)
        except FileNotFoundError:
            pass

