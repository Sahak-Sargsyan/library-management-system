from datetime import datetime, timezone
from typing import Optional
import uuid
from __future__ import annotations

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

    def borrow_book(self, member: uuid.UUID):
        self.is_borrowed = True
        self.borrowed_date = datetime.now(timezone.utc)
        self.borrowed_by = member

    def return_book(self):
        self.is_borrowed = False
        self.borrowed_date = None
        self.borrowed_by = None