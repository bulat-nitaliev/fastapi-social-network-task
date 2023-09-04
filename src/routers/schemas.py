from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class PostCreate(BaseModel):
    title: str
    content: str
    date_creation: Optional[datetime] 


