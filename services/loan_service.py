from datetime import date

import utils.exceptions as exc

from models.user import User
from models.book import Book
from models.loan import Loan

MAX_LOAN_PER_USER = 5

class LoanService:
    def create_loan(self, book_id: int, user_id: int, due_date: date) -> Loan:
        user, book = self._validate_loan_request(book_id, user_id, due_date)

        #XXX: FALTA ATOMICIDADE: Se o save do loan falhar, o amount do livro não deve ser decrementado.
        loan = Loan(book_id=book_id, user_id=user_id, due_date=due_date)
        loan.save()

        book.amount -= 1
        book.save()

        return loan

    def _validate_loan_request(self, book_id: int, user_id: int, due_date: date) -> tuple[User, Book]:
        user = User.find_by_id(user_id)
        if user is None or not user.active:
            raise exc.UserNotFoundError()

        book = Book.find_by_id(book_id)
        if book is None or book.amount <= 0 or not book.active:
            raise exc.BookUnavailableError()

        if len(Loan.all_for_user(user_id)) >= MAX_LOAN_PER_USER:
            raise exc.UserMaxLoansReachedError()

        if Loan.has_occurrence(user_id, book_id):
            raise exc.LoanAlreadyExistsError()

        return user, book