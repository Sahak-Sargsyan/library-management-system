from infrastructure.library_repository import LibraryRepository
import schemas
from infrastructure import models
from infrastructure.mappers import BookMapper

class BookService:
    repository: LibraryRepository

    def __init__(self, repository: LibraryRepository):
        self.repository = repository

    def get_all_books(self):
        return self.repository.get_all_books()
    
    def get_book_by_id(self, book_id: int):
        book = self.repository.get_book_by_id(book_id)
        return book
    
    def create_book(self, new_book: schemas.BookCreate):
        new_book_to_add=models.Book(title=new_book.title, author=new_book.author)
        return self.repository.create_book(new_book_to_add)
    
    def delete_book_by_id(self, book_id: int):
        self.repository.delete_book_by_id(book_id)
    
    def update_book(self, book_id: int, updated_book: schemas.BookUpdate):
        book_to_update=models.Book(updated_book.model_dump())
        self.repository.update_book(book_id, book_to_update)

    def borrow_book(self, book_id: int, member_id: int):
        book_to_borrow = self.repository.get_book_by_id(book_id)
        domain_book = BookMapper.from_orm_map_to_domain(book_to_borrow)
        domain_book.borrow_book(member_id)
        book_to_borrow = BookMapper.from_domain_map_to_orm(domain_book)
        self.repository.update_book(book_id, book_to_borrow)

    def return_book(self, book_id):
        book_to_return = self.repository.get_book_by_id(book_id)
        domain_book = BookMapper.from_orm_map_to_domain(book_to_return)
        domain_book.return_book()
        book_to_return = BookMapper.from_domain_map_to_orm(domain_book)
        self.repository.update_book(book_id, book_to_return)
        