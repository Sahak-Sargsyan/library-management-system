from sqlalchemy.orm import Session
from infrastructure.models import Book, Member
from uuid import UUID
from datetime import datetime, timezone
from shared.exceptions import NotFoundException, AlreadyBorrowedException, DuplicateEmailException

class LibraryRepository:
    db: Session

    def __init__(self, db: Session):
        self.db = db

    def create_book(self, new_book: Book):
        #TODO validation logic
        self.db.add(new_book)
        self.db.commit()
        self.db.refresh(new_book)
        return new_book
    
    def get_book_by_id(self, book_id: int):
        book = self.db.query(Book).filter(Book.book_id == book_id).first()
        if not Book:
            raise NotFoundException(f"Book with id: {book_id} is not found.")
        
        return book
    
    def get_all_books(self):
        return self.db.query(Book).all()
    
    def update_book(self, book_id: int, updated_book: Book):
        #TODO updated_book validation logic
        book_to_update = self.db.query(Book).filter(Book.book_id == book_id).first()

        if not book_to_update:
            raise NotFoundException(f"Book with id: {book_id} is not found.")

        self.db.merge(updated_book)
        self.db.commit()
        self.db.refresh(updated_book)
        return updated_book

    def delete_book_by_id(self, book_id: int):
        book_to_delete = self.db.query(Book).filter(Book.book_id == book_id).first()

        if not book_to_delete:
            raise NotFoundException(f"Book with id: {book_id} is not found.")

        self.db.delete(book_to_delete)
        self.db.commit()

    def borrow_book(self, book_id: int, member_id: UUID):
        book_to_borrow = self.db.query(Book).filter(Book.book_id == book_id).first()
        member_to_assign = self.db.query(Member).filter(Member.member_id == member_id).first()

        if not book_to_borrow:
            raise NotFoundException(f"Book with id: {book_id} is not found.")
        if not member_to_assign:
            raise NotFoundException(f"Member with id: {member_id} doesn't exist.")
        elif book_to_borrow.is_borrowed:
            raise AlreadyBorrowedException(f"Book with id: {book_id} is already borrowed.")

        book_to_borrow.is_borrowed = True
        book_to_borrow.borrowed_by = member_id
        book_to_borrow.borrowed_date = datetime.now(timezone.utc)

        self.db.merge(book_to_borrow)
        self.db.commit()

    def return_book(self, book_id: int):
        book_to_return = self.db.query(Book).filter(Book.book_id == book_id).first()

        #TODO check if is_borrowed

        book_to_return.is_borrowed = False
        book_to_return.borrowed_date = None
        book_to_return.borrowed_by = None
        self.db.merge(book_to_return)
        self.db.commit()

    #Members
    def create_member(self, new_member: Member):
        member = self.db.query(Member).filter(Member.email == new_member.email).first()

        if member is not None:
            raise DuplicateEmailException(f"Member with email: {new_member.email} exists.")
        
        self.db.add(new_member)
        self.db.commit()
        self.db.refresh(new_member)
        return new_member
    
    def get_member_by_id(self, member_id: int):
        member = self.db.query(Member).filter(Member.member_id == member_id).first()

        if not member:
            raise NotFoundException(f"Member with id: {member_id} is not found.")
        
        return member
    
    def get_all_members(self):
        return self.db.query(Member).all()
    
    def update_member(self, member_id: UUID, updated_member: Book):
        member_to_update = self.db.query(Member).filter(Member.member_id == member_id).first()

        if not member_to_update:
            raise NotFoundException(f"Member with id: {member_id} is not found.")
        
        self.db.merge(updated_member)
        self.db.commit()
        self.db.refresh(member_to_update)
        return member_to_update

    def delete_member_by_id(self, member_id: UUID):
        member_to_delete = self.db.query(Member).filter(Member.member_id == member_id).first()

        if not member_to_delete:
            raise NotFoundException(f"Member with id: {member_id} is not found.")

        self.db.delete(member_to_delete)
        self.db.commit()
