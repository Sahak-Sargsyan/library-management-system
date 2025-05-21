from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
import uuid
from infrastructure.database import Base

class Book(Base):
    __tablename__ = "books"
    book_id: int = Column(Integer, primary_key=True, nullable=False)
    title: str = Column(String, nullable=False)
    author: str = Column(String, nullable=False)
    is_borrowed: bool = Column(Boolean, nullable=False, default=False)
    borrowed_date: datetime = Column(DateTime, nullable=True)
    borrowed_by: uuid.UUID = Column(UUID(as_uuid=True), nullable=True)

class Member(Base):
    __tablename__ = "members"
    member_id: uuid.UUID = Column(UUID(as_uuid=True), primary_key=True, nullable=False, default=uuid.uuid4())
    name: str = Column(String, nullable=False)
    email: str = Column(String, unique=True, nullable=False)
