"""
MODEL: Book
Responsável pela lógica de dados e regras de negócio do livro.
"""
from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from utils.exceptions import DomainError, BookNotFoundError
from utils.constants import DB_DATE_FORMAT

from repositories.book_repository import BookRepository

@dataclass
class Book:
    title: str
    author: str
    year: int
    amount: int
    active: bool = True
    id: Optional[int] = None
    image: Optional[str] = None
    created_at: Optional[str] = datetime.now().strftime(DB_DATE_FORMAT)
    updated_at: Optional[str] = None

    # ── Úteis ────────────────────────────────────────────────
    def validate(self):
        if not self.title.strip():
            raise DomainError("Título não pode ser vazio.")
        if not len(str(self.year)) == 4 :
            raise DomainError("Ano inválido.")

    def decrease_amount(self):
        if self.amount < 1: return
        self.amount -= 1

    def format_data(self) -> Book:
        self.title = self.title.strip()
        self.author = self.author.strip()
        return self

    # ── Consultas ─────────────────────────────────────────────────
    @classmethod
    def is_available(cls, book_id: int) -> bool:
        """Verifica se o livro especificado tem quantidade suficiente ou está ativo"""
        book_data = BookRepository.find_by_id(book_id)
        if book_data is None:
            raise BookNotFoundError()
        book = cls(**book_data)
        if book is None:
            raise BookNotFoundError()
        return book.amount > 0 or book.active