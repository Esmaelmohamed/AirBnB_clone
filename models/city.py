from models.base_model import BaseModel

class City(BaseModel):
    """City class inherits from BaseModel."""
    
    def __init__(self):
        """Initialize City instance."""
        super().__init__()
        self.state_id = ""
        self.name = ""
