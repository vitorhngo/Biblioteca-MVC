from dataclasses import dataclass
from typing import Optional
from datetime import date

import database.db as db
from utils.exceptions import DomainError

DUE_DATE_LIMIT = 31 # Em dias

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
            days = (self.due_date - date.strptime(self.created_at, db.DATE_FORMAT)).days
            if days > DUE_DATE_LIMIT:
                raise DomainError(f"A data de vencimento ultrapassa o limite de {DUE_DATE_LIMIT} dias")
            if self.due_date < date.strptime(self.created_at, db.DATE_FORMAT):
                raise DomainError(f"A data de vencimento não pode ser menor que a data de criação do empréstimo")
        
    # ── Persistência ─────────────────────────────────────────────
    def save(self) -> "Loan":
        self.validate()
        due = self.due_date.strftime("%d/%m/%Y, 23:59:59") if self.due_date else None
        if self.id is None:
            self.id = db.write("loans", {
                "user_id": self.user_id,
                "book_id": self.book_id,
                "status": self.status,
                "due_date": due
            }
        )
        else:
            db.update("loans", self.id, {
                "user_id": self.user_id,
                "book_id": self.book_id,
                "status": self.status,
                "due_date": due
            }
        )
        return self
    
    def delete(self) -> None:
        if self.id is None:
            raise RuntimeError("Empréstimo não foi salvo ainda.")
        db.delete("loans", self.id)
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
        data = db.get("loans", loan_id)
        return cls._from_data(data) if data else None

    @classmethod
    def has_occurrence(cls, user_id: int, book_id: int) -> bool:
        '''Checa se há empréstimos associados ao usuário e livro especificados'''
        loans = cls.all()
        for loan in loans:
            if user_id == loan.user_id and book_id == loan.book_id:
                return True
        return False
    
    @classmethod
    def all(cls) -> list[Loan]:
        '''Retorna uma lista de empréstimos'''
        loans = []
        for k, v in db.read().items():
            if not type(v).__name__ == "dict": continue
            if not k == "loans": continue
            for _, loan in v.items():
                if loan is None: continue
                loans.append(loan)
        return [cls._from_data(l) for l in loans]

    @classmethod
    def all_for_user(cls, user_id: int) -> list[Loan]:
        '''Retorna uma lista de empréstimos do usuário especificado'''
        loans = []
        for k, v in db.read().items():
            if not type(v).__name__ == "dict": continue
            if not k == "loans": continue
            for _, loan in v.items():
                if loan is None: continue
                if loan["user_id"] != user_id: continue
                loans.append(loan)
        return [cls._from_data(l) for l in loans]

    @classmethod
    def all_active_for_user(cls, user_id: int) -> list[Loan]:
        '''Retorna uma lista de empréstimos ativos do usuário especificado'''
        loans = []
        for k, v in db.read().items():
            if not type(v).__name__ == "dict": continue
            if not k == "loans": continue
            for _, loan in v.items():
                if loan is None: continue
                if loan["user_id"] != user_id: continue
                if loan["status"] != "active": continue
                loans.append(loan)
        return [cls._from_data(l) for l in loans]
    
    @classmethod
    def all_active_for_book(cls, book_id: int) -> list[Loan]:
        '''Retorna uma lista de empréstimos ativos do livro especificado'''
        loans = []
        for k, v in db.read().items():
            if not type(v).__name__ == "dict": continue
            if not k == "loans": continue
            for _, loan in v.items():
                if loan is None: continue
                if loan["book_id"] != book_id: continue
                if loan["status"] != "active": continue
                loans.append(loan)
        return [cls._from_data(l) for l in loans]
    
    # ── Auxiliar ──────────────────────────────────────────────────
    @classmethod
    def _from_data(cls, data) -> "Loan":
        '''Reconstrói o objeto com dados vindos do banco'''
        return cls(
            id=data["id"],
            user_id=data["user_id"],
            book_id=data["book_id"],
            status=data["status"],
            due_date=data["due_date"],
            created_at=data["created_at"]
        )