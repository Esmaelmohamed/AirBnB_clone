#!/usr/bin/python3
"""FileStorage module - defines the FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Storage engine abstraction handling serialization and deserialization of objects."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Retrieve all objects."""
        return self.__objects

    def new(self, obj):
        """Add a new object to the storage dictionary."""
        obj_key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[obj_key] = obj

    def save(self):
        """Serialize objects to JSON file."""
        serialized_objects = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, "w") as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """Deserialize JSON file to objects."""
        try:
            with open(self.__file_path, "r") as file:
                deserialized_objects = json.load(file)
                for key, obj_data in deserialized_objects.items():
                    class_name, obj_id = key.split('.')
                    class_ref = eval(class_name)
                    del obj_data['__class__']
                    self.__objects[key] = class_ref(**obj_data)
        except FileNotFoundError:
            pass
