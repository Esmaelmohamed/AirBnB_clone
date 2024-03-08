from models.base_model import BaseModel

class State(BaseModel):
    """State class inherits from BaseModel."""
    
    def __init__(self):
        """Initialize State instance."""
        super().__init__()
        self.name = ""
