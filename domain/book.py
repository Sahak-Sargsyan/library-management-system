from datetime import datetime
from member import Member
from typing import Union, Optional
import uuid

class Book:
    book_id: Optional[int] = None
    title: str
    author: str
    is_borrowed: bool
    borrowed_date: Optional[datetime] = None
    borrowed_by: Optional[uuid.UUID] = None

    def __init__(self, title, author, id: Optional[int] = None):
        self.book_id = id
        self.title = title
        self.author = author
        self.is_borrowed = False
        self.borrowed_date = None
        self.borrowed_by = None
