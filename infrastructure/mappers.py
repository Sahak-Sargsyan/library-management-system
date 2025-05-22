import domain.book
from infrastructure import models

class BookMapper:
    @staticmethod
    def from_orm_map_to_domain(orm_book: models.Book):
        domain_book = domain.book.Book(
            book_id=orm_book.book_id,
            title=orm_book.title,
            author=orm_book.author,
        )

        domain_book.is_borrowed = orm_book.is_borrowed
        domain_book.borrowed_by = orm_book.borrowed_by
        domain_book.borrowed_date = orm_book.borrowed_date

        return domain_book
    
    @staticmethod
    def from_domain_map_to_orm(domain_book: domain.book.Book):
        orm_book = models.Book()
        orm_book.book_id=domain_book.book_id
        orm_book.title=domain_book.title
        orm_book.author=domain_book.author
        orm_book.is_borrowed=domain_book.is_borrowed
        orm_book.borrowed_date=domain_book.borrowed_date
        orm_book.borrowed_by=domain_book.borrowed_by
        return orm_book