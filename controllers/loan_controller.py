"""
CONTROLLER: LoanController
Responsável por lidar com as requisições relacionadas aos empréstimos.
"""
from datetime import date

from utils.exceptions import DomainError

from services.loan_service import LoanService

class LoanController:
    '''Representação abstrata de um empréstimo'''
    @staticmethod
    def create(
        user_id: int, 
        book_id: int,
        due_date: date
    ) -> dict:
        try:
            result = LoanService.create(book_id, user_id, due_date)
            return {"success": True, "data": result}
        except DomainError as e:
            return {"success": False, "error": str(e)}

    @staticmethod
    def update(loan_id: int, due_date: date) -> dict:
        try:
            result = LoanService.update(loan_id, due_date)
            return {"success": True, "data": result}
        except DomainError as e:
            return {"success": False, "error": str(e)}

    @staticmethod
    def list_for_user(
        user_id: int,
    ) -> dict:
        """Lista todos os empréstimos de um usuário"""
        try:
            result = LoanService.list_for_user(user_id)
            return {"success": True, "data": result}
        except DomainError as e:
            return {"success": False, "error": str(e)}

    # ── Remoção ───────────────────────────────────────────────────
    @staticmethod
    def delete(loan_id: int) -> dict:
        """Deleta um empréstimo"""
        try:
            LoanService.delete(loan_id)
            return {"success": True, "data": f"Empréstimo #{loan_id} deletado com sucesso."}
        except DomainError as e:
            return {"success": False, "error": str(e)}