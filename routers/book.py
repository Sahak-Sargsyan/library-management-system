from fastapi import APIRouter, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
from shared.schemas import BookBase, BookCreate, BookUpdate, BorrowedData
from infrastructure.database import get_db
from application.book_service import BookService
from infrastructure.library_repository import LibraryRepository
from uuid import UUID
from shared.exceptions import NotFoundException
from fastapi_pagination import Page, paginate, add_pagination

router = APIRouter(
    prefix="/books",
    tags=["Books"]
)

@router.get("/", response_model=Page[BookBase])
def get_books(db: Session = Depends(get_db)):
    service = BookService(LibraryRepository(db))
    books = service.get_all_books()
    return paginate(books)

@router.get("/{book_id}", response_model=BookBase)
def get_book_by_id(book_id: int, db: Session = Depends(get_db)):
    try:
        service = BookService(LibraryRepository(db))
        book = service.get_book_by_id(book_id)
        return book
    except NotFoundException as ex:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(ex))

@router.post("/", response_model=BookBase)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    service = BookService(LibraryRepository(db))
    return service.create_book(book)

@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book_by_id(book_id: int, db: Session = Depends(get_db)):
    try:
        service = BookService(LibraryRepository(db))
        service.delete_book_by_id(book_id)
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    except NotFoundException as ex:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(ex))

@router.put("/{book_id}", response_model=BookBase)
def update_book(book_id: int, updated_book: BookUpdate, db: Session = Depends(get_db)):
    try:
        service = BookService(LibraryRepository(db))
        return service.update_book(book_id, updated_book)
    except NotFoundException as ex:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(ex))

@router.post("/borrow/{book_id}/{member_id}", response_model=BorrowedData)
def borrow_book(book_id: int, member_id: UUID, db: Session = Depends(get_db)):
    try:
        service = BookService(LibraryRepository(db))
        data = service.borrow_book(book_id, member_id)
        return data
    except NotFoundException as ex:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(ex))

@router.post("/return/{book_id}", response_model=BorrowedData)
def return_book(book_id: int, db: Session = Depends(get_db)):
    service = BookService(LibraryRepository(db))
    data = service.return_book(book_id)
    return data