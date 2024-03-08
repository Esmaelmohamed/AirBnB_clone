from models.base_model import BaseModel

class Review(BaseModel):
    """Review class inherits from BaseModel."""
    
    def __init__(self):
        """Initialize Review instance."""
        super().__init__()
        self.place_id = ""
        self.user_id = ""
        self.text = ""
