from infrastructure.library_repository import LibraryRepository
from shared.schemas import BookCreate, BookUpdate, BorrowedData
from infrastructure import models
from infrastructure.mappers import BookMapper
from uuid import UUID
from shared.exceptions import NotFoundException, AlreadyBorrowedException

class BookService:
    repository: LibraryRepository

    def __init__(self, repository: LibraryRepository):
        self.repository = repository

    def get_all_books(self):
        return self.repository.get_all_books()
    
    def get_book_by_id(self, book_id: int):
        try:
            book = self.repository.get_book_by_id(book_id)
            return book
        except NotFoundException:
            raise
    
    def create_book(self, new_book: BookCreate):
        new_book_to_add=models.Book(title=new_book.title, author=new_book.author)
        return self.repository.create_book(new_book_to_add)
    
    def delete_book_by_id(self, book_id: int):
        try:
            self.repository.delete_book_by_id(book_id)
        except NotFoundException:
            raise
    
    def update_book(self, book_id: int, updated_book: BookUpdate):
        try:
            book_to_update=models.Book(
                book_id = book_id,
                title = updated_book.title,
                author = updated_book.title,
                is_borrowed = updated_book.is_borrowed,
                borrowed_date = updated_book.borrowed_date,
                borrowed_by = updated_book.borrowed_by
            )
            return self.repository.update_book(book_id, book_to_update)
        except NotFoundException:
            raise

    def borrow_book(self, book_id: int, member_id: UUID):
        try:
            book_to_borrow = self.repository.get_book_by_id(book_id)
            domain_book = BookMapper.from_orm_map_to_domain(book_to_borrow)
            domain_book.borrow_book(member_id)
            book_to_borrow = BookMapper.from_domain_map_to_orm(domain_book)
            borrowed_book = self.repository.update_book(book_id, book_to_borrow)
            borrowed_data = BorrowedData(
                book_id=borrowed_book.book_id,
                borrowed_date=borrowed_book.borrowed_date,
                borrowed_by=borrowed_book.borrowed_by
                )
            return borrowed_data
        except NotFoundException as ex:
            raise
        except AlreadyBorrowedException:
            borrowed_data = BorrowedData(
                book_id=book_to_borrow.book_id,
                borrowed_date=book_to_borrow.borrowed_date,
                borrowed_by=book_to_borrow.borrowed_by
                )
            return borrowed_data

    def return_book(self, book_id):
        book_to_return = self.repository.get_book_by_id(book_id)
        domain_book = BookMapper.from_orm_map_to_domain(book_to_return)
        domain_book.return_book()
        book_to_return = BookMapper.from_domain_map_to_orm(domain_book)
        returned_book = self.repository.update_book(book_id, book_to_return)
        borrowed_data = BorrowedData(
            book_id=returned_book.book_id,
            borrowed_date=returned_book.borrowed_date,
            borrowed_by=returned_book.borrowed_by
            )
        return borrowed_data
        