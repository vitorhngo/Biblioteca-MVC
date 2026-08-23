"""
SERVICE: BookService
Responsável por coordenar a lógica de negócio do livro, interagindo com o repositório e o modelo.
"""
from utils import enums
from utils.exceptions import BookNotFoundError

from repositories.book_repository import BookRepository
from repositories.loan_repository import LoanRepository

from models.book import Book

class BookService:
    @staticmethod
    def create(
            title: str,
            author: str,
            year: int,
            amount: int = 1,
            image = None
        ) -> Book:
        book = Book(
            title=title,
            author=author,
            year=year,
            amount=amount,
            image=image
        )
        book.validate()
        BookRepository.save(book)
        return book

    @staticmethod
    def remove(book_id: int) -> enums.DeleteResult:
        data = BookRepository.find_by_id(book_id)
        if data is None:
            raise BookNotFoundError()
        
        book = Book(**data)

        if LoanRepository.all_active_for_book(book_id):
            book.active = False
            BookRepository.save(book)
            return enums.DeleteResult.DEACTIVATED
        
        BookRepository.delete(book)
        return enums.DeleteResult.DELETED