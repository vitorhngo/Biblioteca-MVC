from dataclasses import dataclass
from typing import Optional
from datetime import date

from utils.exceptions import DomainError
from utils.constants import DUE_DATE_LIMIT, DB_DATE_FORMAT

from repositories.loan_repository import LoanRepository

VALID_STATUSES  = ("active", "expired")
STATUS_LABELS = {
    "active":      "Ativo",
    "expired":     "Vencido",
}

@dataclass
class Loan:
    user_id: int
    book_id: int
    status: str = "active"
    id: Optional[int] = None
    due_date: Optional[date] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

    # ── Validação ────────────────────────────────────────────────
    def validate(self) -> None:
        if self.status not in VALID_STATUSES:
            raise DomainError(f"Status inválido: {self.status!r}. Use: {VALID_STATUSES}")
        if self.due_date and self.created_at:
            days = (self.due_date - date.strptime(self.created_at, DB_DATE_FORMAT)).days
            if days > DUE_DATE_LIMIT:
                raise DomainError(f"A data de vencimento ultrapassa o limite de {DUE_DATE_LIMIT} dias")
            if self.due_date < date.strptime(self.created_at, DB_DATE_FORMAT):
                raise DomainError(f"A data de vencimento não pode ser menor que a data de criação do empréstimo")
        
    def register(self):
        self.validate()
        LoanRepository.save(self)
        return self
    
    def delete(self) -> None:
        if self.id is None:
            raise RuntimeError("Empréstimo não foi salvo ainda.")
        LoanRepository.delete(self)
        self.id = None

    # ── Propriedades de conveniência ──────────────────────────────
    @property
    def status_label(self) -> str:
        return STATUS_LABELS.get(self.status, self.status)

    @property
    def is_overdue(self) -> bool:
        return (
            self.due_date is not None
            and self.status != "active"
            and self.due_date < date.today()
        )

    # ── Consultas ─────────────────────────────────────────────────
    @classmethod
    def find_by_id(cls, loan_id: int) -> Optional["Loan"]:
        """Busca um empréstimo pelo seu ID. Retorna None se não encontrado."""
        data = LoanRepository.find_by_id(loan_id)
        return cls(**data) if data else None

    @classmethod
    def has_occurrence(cls, user_id: int, book_id: int) -> bool:
        """Checa se há empréstimos associados ao usuário e livro especificados"""
        data = LoanRepository.all(
            filter_expression=lambda loan: loan["user_id"] == user_id and loan["book_id"] == book_id
        )
        return len(data) > 0
    
    @classmethod
    def all(cls) -> list[Loan]:
        """Retorna uma lista de empréstimos"""
        data = LoanRepository.all()
        return [cls(**loan) for loan in data]

    @classmethod
    def all_for_user(cls, user_id: int) -> list[Loan]:
        """Retorna uma lista de empréstimos do usuário especificado"""
        data = LoanRepository.all(
            filter_expression=lambda loan: loan["user_id"] == user_id
        )
        return [cls(**loan) for loan in data]

    @classmethod
    def all_active_for_user(cls, user_id: int) -> list[Loan]:
        '''Retorna uma lista de empréstimos ativos do usuário especificado'''
        data = LoanRepository.all(
            filter_expression=lambda loan: loan["user_id"] == user_id and loan["status"] == "active"
        )
        return [cls(**loan) for loan in data]

    @classmethod
    def all_for_book(cls, book_id: int) -> list[Loan]:
        """Retorna uma lista de empréstimos do livro especificado"""
        data = LoanRepository.all(
            filter_expression=lambda loan: loan["book_id"] == book_id
        )
        return [cls(**loan) for loan in data]

    @classmethod
    def all_active_for_book(cls, book_id: int) -> list[Loan]:
        '''Retorna uma lista de empréstimos ativos do livro especificado'''
        data = LoanRepository.all(
            filter_expression=lambda loan: loan["book_id"] == book_id and loan["status"] == "active"
        )
        return [cls(**loan) for loan in data]