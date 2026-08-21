from utils import enums
import utils.exceptions as exc

from models.book import Book
from models.loan import Loan

class BookService:
    def remove(self, book_id: int) -> enums.DeleteResult:
        book = Book.find_by_id(book_id)
        if book is None:
            raise exc.BookNotFoundError()

        if Loan.all_active_for_book(book_id):
            book.deactivate()
            return enums.DeleteResult.DEACTIVATED

        book.delete()
        return enums.DeleteResult.DELETED