"""
REPOSITORY: LoanRepository
Responsável por interagir com o banco de dados para operações relacionadas ao empréstimo.
"""
import database.db as db

from utils.constants import DB_DATE_FORMAT

class LoanRepository:
    @staticmethod
    def save(loan):
        """Salva um empréstimo no banco de dados. Se o empréstimo já existir, atualiza seus dados."""
        if hasattr(loan, 'due_date') and loan.due_date:
            loan.due_date = loan.due_date.strftime(DB_DATE_FORMAT)

        if loan.id is None:
            loan.id = db.write("loans", loan.__dict__)
        else:
            db.update("loans", loan.id, loan.__dict__)
        return loan

    @staticmethod
    def delete(loan):
        """Deleta um empréstimo do banco de dados."""
        if loan.id is None:
            raise RuntimeError("Empréstimo não foi salvo ainda.")
        db.delete("loans", loan.id)
        loan.id = None

    @staticmethod
    def find_by_id(loan_id: int):
        """Busca um empréstimo pelo seu ID. Retorna None se não encontrado."""
        loan_data = db.get("loans", loan_id)
        return loan_data

    @staticmethod
    def all(filter_expression=lambda loan: True):
        """De acordo com o filtro especificado, retorna empréstimos cadastrados."""
        loans = []
        for k, v in db.read().items():
            if not type(v).__name__ == "dict": continue
            if not k == "loans": continue
            for _, loan in v.items():
                if loan is None: continue
                if not filter_expression(loan): continue
                loans.append(loan)
        return loans

    @staticmethod
    def all_for_user(user_id: int) -> list[dict]:
        """Retorna uma lista de empréstimos do usuário especificado"""
        return LoanRepository.all(
            filter_expression=lambda loan: loan["user_id"] == user_id
        )

    @staticmethod
    def all_active_for_user(user_id: int) -> list[dict]:
        '''Retorna uma lista de empréstimos ativos do usuário especificado'''
        return LoanRepository.all(
            filter_expression=lambda loan: loan["user_id"] == user_id and loan["status"] == "active"
        )

    @staticmethod
    def all_for_book(book_id: int) -> list[dict]:
        """Retorna uma lista de empréstimos do livro especificado"""
        return LoanRepository.all(
            filter_expression=lambda loan: loan["book_id"] == book_id
        )

    @staticmethod
    def all_active_for_book(book_id: int) -> list[dict]:
        '''Retorna uma lista de empréstimos ativos do livro especificado'''
        return LoanRepository.all(
            filter_expression=lambda loan: loan["book_id"] == book_id and loan["status"] == "active"
        )