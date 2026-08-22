from utils import enums
from utils.exceptions import DomainError, BookNotFoundError

from repositories.book_repository import BookRepository

from models.book import Book
from models.loan import Loan

class BookService:
    @staticmethod
    def create(
            title: str,
            author: str,
            year: int,
            amount: int = 1,
            image = None
        ) -> Book:
        book = Book(title=title, author=author, year=year, amount=amount, image=image)
        book.register()
        return book

    @staticmethod
    def remove(book_id: int) -> enums.DeleteResult:
        book_data = BookRepository.find_by_id(book_id)
        if book_data is None:
            raise BookNotFoundError()
        
        book = Book(**book_data)

        if Loan.all_active_for_book(book_id):
            book.deactivate()
            return enums.DeleteResult.DEACTIVATED

        book.delete()
        return enums.DeleteResult.DELETED