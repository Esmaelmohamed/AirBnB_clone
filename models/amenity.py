from models.base_model import BaseModel

class Amenity(BaseModel):
    """Amenity class inherits from BaseModel."""
    
    def __init__(self):
        """Initialize Amenity instance."""
        super().__init__()
        self.name = ""