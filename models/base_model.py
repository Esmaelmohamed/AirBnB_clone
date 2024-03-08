from models import storage
import uuid 
from datetime import datetime  


class BaseModel:
    """BaseModel class for defining common attributes/methods for other classes."""
    
    def __init__(self, *args, **kwargs):
        """Initialize BaseModel instance."""
        if kwargs:
            # Initialize attributes from dictionary representation
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        setattr(self, key, datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)  # Add new instance to storage

    def save(self):
        """Update the 'updated_at' attribute with the current datetime."""
        self.updated_at = datetime.now()
        storage.save()
        

    def to_dict(self):
        """Return a dictionary representation of the BaseModel instance."""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
    
