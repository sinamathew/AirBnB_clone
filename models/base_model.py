#!/usr/bin/env python3
import uuid
from datetime import datetime

"""A BaseModel module."""

class BaseModel:
    """Defines common attributes/methods for other classes.
    """

    def __init__(self):
        """Initialize.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.update_at = datetime.now()

    def __str__(self):
        """Return the string representation.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update time and date."""
        self.update_at = datetime.now()

    def to_dict(self):
        """save result to dictionary."""
        result = self.__dict__.copy()
        result["__class__"] = self.__class__.__name__
        result["created_at"] = self.created_at.isoformat()
        result["updated_at"] = self.updated_at.isoformat()
        return result
