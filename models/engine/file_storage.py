import json
import sys 
sys.path.insert(0,"/home/esmael/Desktop/AirBnB_clone/models/user.py")

from user import User
class FileStorage:
    """Class for serializing instances to a JSON file and deserializing JSON file to instances."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file."""
        obj_dict = {}
        for key, obj in self.__objects.items():
            obj_dict[key] = obj.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        try:
            with open(self.__file_path, 'r') as f:
                obj_dict = json.load(f)
                for key, val in obj_dict.items():
                    class_name, obj_id = key.split('.')
                    self.__objects[key] = globals()[class_name](**val)
        except FileNotFoundError:
            pass
