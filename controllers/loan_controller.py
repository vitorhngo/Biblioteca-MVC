from datetime import date
from typing import Optional
from models.loan import Loan
from models.user import User
from models.book import Book

MAX_LOAN_PER_USER = 5

class LoanController:
    '''Representação abstrata de um empréstimo'''
    def create(
        self,
        user_id: int, 
        book_id: int,
        due_date: Optional[date]
    ) -> dict:
        if User.find_by_id(user_id) is None:
            return {"success": False, "error": f"Usuário #{user_id} não encontrado."}
        if Book.find_by_id(book_id) is None:
            return {"success": False, "error": f"Livro #{user_id} não encontrado."}
        if not Book.is_available(book_id):
            return {"success": False, "error": f"Não há livros suficientes para emprestar."}
        if len(Loan.all_for_user(user_id)) >= MAX_LOAN_PER_USER:
            return {"success": False, "error": f"O usuário chegou no limite de empréstimos: {MAX_LOAN_PER_USER}"}
        try:
            loan = Loan(
                user_id=user_id,
                book_id=book_id,
                due_date=due_date
            ).save()
            return {"success": True, "data": loan}
        except ValueError as exc:
            return {"success": False, "error": str(exc)}

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
            return {"success": False, "error": f"Tarefa #{loan_id} não encontrada."}
        loan.delete()
        return {"success": True, "data": f"Tarefa #{loan_id} removida com sucesso."}