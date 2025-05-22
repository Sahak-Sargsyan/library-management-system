from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime
from uuid import UUID

class BookCreate(BaseModel):
    title: str
    author: str

class BookUpdate(BookCreate):
    is_borrowed: bool
    borrowed_date: Optional[datetime] = None
    borrowed_by: Optional[UUID] = None

class BookBase(BookUpdate):
    book_id: int

    model_config = {'from_attributes': True}

class MemberCreate(BaseModel):
    name: str
    email: EmailStr

class MemberUpdate(MemberCreate):
    pass

class MemberBase(MemberUpdate):
    member_id: UUID

    model_config = {'from_attributes': True}

class BorrowedData(BaseModel):
    book_id: int
    borrowed_date: Optional[datetime] = None
    borrowed_by: Optional[UUID] = None