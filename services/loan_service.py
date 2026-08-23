"""
SERVICE: LoanService
Responsável por coordenar a lógica de negócio do empréstimo, interagindo com o repositório e o modelo.
"""
from datetime import date

import utils.exceptions as exc
from utils.constants import MAX_LOAN_PER_USER

from repositories.loan_repository import LoanRepository
from repositories.book_repository import BookRepository
from repositories.user_repository import UserRepository

from models.user import User
from models.book import Book
from models.loan import Loan

class LoanService:
    @staticmethod
    def create(book_id: int, user_id: int, due_date: date) -> Loan:
        book = LoanService._validate_loan_request(book_id, user_id, due_date)

        #XXX: FALTA ATOMICIDADE: Se o save do loan falhar, o amount do livro não deve ser decrementado.
        loan = Loan(
            book_id=book_id, 
            user_id=user_id, 
            due_date=due_date
        )
        loan.validate()
        loan.format_data()
        LoanRepository.save(loan)
        
        book.amount -= 1
        BookRepository.save(book)

        return loan

    @staticmethod
    def update(loan_id: int, due_date: date) -> Loan:
        data = LoanRepository.find_by_id(loan_id)
        if data is None:
            raise exc.LoanNotFoundError()
        loan = Loan(**data)
        loan.due_date = due_date
        loan.validate()
        loan.format_data()
        LoanRepository.save(loan)
        return loan

    @staticmethod
    def list_for_user(user_id: int) -> list[Loan]:
        if UserRepository.find_by_id(user_id) is None:
            raise exc.UserNotFoundError()
        return [Loan(**data) for data in LoanRepository.all_for_user(user_id)]

    @staticmethod
    def delete(loan_id: int):
        data = LoanRepository.find_by_id(loan_id)
        if data is None:
            raise exc.LoanNotFoundError()
        loan = Loan(**data)
        LoanRepository.delete(loan)

    @staticmethod
    def has_occurrence(user_id: int, book_id: int) -> bool:
        """Checa se há empréstimos associados ao usuário e livro especificados"""
        data = LoanRepository.all(
                filter_expression=lambda loan: loan["user_id"] == user_id and loan["book_id"] == book_id
            )
        return len(data) > 0

    @staticmethod
    def _validate_loan_request(book_id: int, user_id: int, due_date: date) -> Book:
        user_data = UserRepository.find_by_id(user_id)
        if user_data is None:
            raise exc.UserNotFoundError()
        if not user_data.get("active", True):
            raise exc.UserDeactiveError()

        book_data = BookRepository.find_by_id(book_id)
        if book_data is None:
            raise exc.BookNotFoundError()
        if not book_data.get("active", True):
            raise exc.BookDeactiveError()
        
        book = Book(**book_data)

        if book.amount <= 0:
            raise exc.BookUnavailableError()

        if len(LoanRepository.all_for_user(user_id)) >= MAX_LOAN_PER_USER:
            raise exc.UserMaxLoansReachedError()

        if LoanService.has_occurrence(user_id, book_id):
            raise exc.LoanAlreadyExistsError()

        return book