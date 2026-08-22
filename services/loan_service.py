from datetime import date

import utils.exceptions as exc
from utils.constants import MAX_LOAN_PER_USER

from models.user import User
from models.book import Book
from models.loan import Loan

from repositories.loan_repository import LoanRepository
from repositories.book_repository import BookRepository

class LoanService:
    @staticmethod
    def create(book_id: int, user_id: int, due_date: date) -> Loan:
        user, book = LoanService._validate_loan_request(book_id, user_id, due_date)

        #XXX: FALTA ATOMICIDADE: Se o save do loan falhar, o amount do livro não deve ser decrementado.
        loan = Loan(
            book_id=book_id, 
            user_id=user_id, 
            due_date=due_date
        )
        loan.register()
        
        book.amount -= 1
        BookRepository.save(book)

        return loan

    @staticmethod
    def update(loan_id: int, due_date: date) -> Loan:
        loan = Loan.find_by_id(loan_id)
        if loan is None:
            raise exc.LoanNotFoundError()
        loan.due_date = due_date
        loan.register()
        return loan

    @staticmethod
    def list_for_user(user_id: int) -> list[Loan]:
        if User.find_by_id(user_id) is None:
            raise exc.UserNotFoundError()
        return Loan.all_for_user(user_id)

    @staticmethod
    def delete(loan_id: int):
        loan = Loan.find_by_id(loan_id)
        if loan is None:
            raise exc.LoanNotFoundError()
        loan.delete()

    @staticmethod
    def _validate_loan_request(book_id: int, user_id: int, due_date: date) -> tuple[User, Book]:
        user = User.find_by_id(user_id)
        if user is None or not user.active:
            raise exc.UserNotFoundError()

        book_data = BookRepository.find_by_id(book_id)
        if book_data is None:
            raise exc.BookNotFoundError()
        
        book = Book(**book_data)

        if book_data is None or book.amount <= 0 or not book.active:
            raise exc.BookUnavailableError()

        if len(Loan.all_for_user(user_id)) >= MAX_LOAN_PER_USER:
            raise exc.UserMaxLoansReachedError()

        if Loan.has_occurrence(user_id, book_id):
            raise exc.LoanAlreadyExistsError()

        return user, book