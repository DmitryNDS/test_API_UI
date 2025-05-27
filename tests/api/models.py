from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

class User(BaseModel):
    id: Optional[int] = None
    name: str
    email: str
    status: str = "active"
    created_at: Optional[datetime] = None

class Post(BaseModel):
    id: Optional[int] = None
    title: str
    content: str
    user_id: int
    created_at: Optional[datetime] = None

class Comment(BaseModel):
    id: Optional[int] = None
    post_id: int
    user_id: int
    content: str
    created_at: Optional[datetime] = None

class ErrorResponse(BaseModel):
    error: str
    message: str
    status_code: int 