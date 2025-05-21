from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from uuid import UUID

class BookCreate(BaseModel):
    title: str
    author: str

class BookUpdate(BookCreate):
    is_borowed: bool
    borrowed_date: Optional[datetime] = None
    borrowed_by: Optional[UUID] = None

class BookBase(BookUpdate):
    id: int

    model_config = {'from_attributes': True}

class MemberCreate(BaseModel):
    name: str
    email: str

class MemberUpdate(MemberCreate):
    pass

class MemberBase(MemberUpdate):
    member_id: UUID

    model_config = {'from_attributes': True}