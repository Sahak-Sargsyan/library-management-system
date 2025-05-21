import domain.book
from infrastructure import models

class BookMapper:
    @staticmethod
    def from_orm_map_to_domain(orm_book: models.Book):
        domain_book = domain.book.Book(
            id=orm_book.id,
            title=orm_book.title,
            author=orm_book.author,
        )

        domain_book.is_borrowed = orm_book.is_borrowed
        domain_book.borrowed_by = orm_book.borrowed_by
        domain_book.borrowed_date = orm_book.borrowed_date

        return domain_book
    
    @staticmethod
    def from_domain_map_to_orm(domain_book: domain.book.Book):
        orm_book = models.Book(
            book_id=domain_book.book_id,
            title=domain_book.title,
            author=domain_book.author,
            is_borrowed=domain_book.is_borrowed,
            borrowed_date=domain_book.borrowed_date,
            borrowed_by=domain_book.borrowed_by
        )

        return orm_book