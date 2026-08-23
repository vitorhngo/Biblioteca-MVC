"""
MODEL: Loan
Responsável pela lógica de dados e regras de negócio do empréstimo.
"""
from dataclasses import dataclass
from typing import Optional
from datetime import date, datetime

from utils.exceptions import DomainError
from utils.constants import DUE_DATE_LIMIT, DB_DATE_FORMAT

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
    created_at: Optional[str] = datetime.now().strftime(DB_DATE_FORMAT)
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

    def format_data(self) -> Loan:
        if self.due_date and isinstance(self.due_date, str):
            self.due_date = date.strptime(self.due_date, DB_DATE_FORMAT)
        return self

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