from datetime import date

from datamodels.exceptions import DomainError

from models.loan import Loan, DUE_DATE_LIMIT
from models.user import User
from models.book import Book
from services.loan_service import LoanService

class LoanController:
    '''Representação abstrata de um empréstimo'''
    def create(
        self,
        user_id: int, 
        book_id: int,
        due_date: date
    ) -> dict:
        try:
            loan = LoanService().create_loan(book_id, user_id, due_date)
            return {"success": True, "data": loan}
        except DomainError as e:
            return {"success": False, "error": e}

    def update(self, loan_id: int, due_date: date) -> dict:
        loan = Loan.find_by_id(loan_id)
        if loan is None:
            return {"success": False, "error": f"Empréstimo #{loan_id} não encontrado."}
        loan.due_date = due_date
        try:
            loan.save()
            return {"success": True, "data": loan}
        except DomainError as e:
            return {"success": False, "error": e}

    # ── Leitura ───────────────────────────────────────────────────
    def get_by_id(self, loan_id: int) -> dict:
        loan = Loan.find_by_id(loan_id)
        if loan is None:
            return {"success": False, "error": f"Empréstimo #{loan_id} não encontrado."}
        return {"success": True, "data": loan}

    def list_for_user(
        self,
        user_id: int,
    ) -> dict:
        if User.find_by_id(user_id) is None:
            return {"success": False, "error": f"Usuário #{user_id} não encontrado."}
        loan = Loan.all_for_user(user_id)
        return {"success": True, "data": loan}

    # ── Remoção ───────────────────────────────────────────────────
    def delete(self, loan_id: int) -> dict:
        loan = Loan.find_by_id(loan_id)
        if loan is None:
            return {"success": False, "error": f"Empréstimo #{loan_id} não encontrado."}
        loan.delete()
        return {"success": True, "data": f"Empréstimo #{loan_id} removido com sucesso."}