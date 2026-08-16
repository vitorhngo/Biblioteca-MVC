from dataclasses import dataclass
from typing import Optional

import database.db as db
import datamodels.exceptions as exc
import datamodels.enums as Enum

from models.loan import Loan

@dataclass
class Book:
    '''Representação abstrata de um livro'''
    title: str
    author: str
    year: int
    image: str
    amount: int
    active: bool = True
    id: Optional[int] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

    # ── Validação ────────────────────────────────────────────────
    def validate(self):
        if not self.title.strip():
            raise ValueError("Título não pode ser vazio.")
        if not len(str(self.year)) == 4 :
            raise ValueError("Ano inválido.")

    # ── Persistência ─────────────────────────────────────────────
    def save(self) -> "Book":
        self.validate()
        if self.id is None:
            self.id = db.write("books", {
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "image": self.image,
            "amount": self.amount,
            "active": self.active
            }
        )
        else:
            db.update("books", self.id, {
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "image": self.image,
            "amount": self.amount,
            "active": self.active,
            }
        )
        return self

    def delete(self):# -> Enum.DeleteResult:
        if self.id is None:
            raise RuntimeError("Livro não foi salvo ainda.")
        #if Loan.all_active_for_book(self.id):
        #    self.deactivate()
        #    return Enum.DeleteResult.DEACTIVATED
        db.delete("books", self.id)
        self.id = None
        #return Enum.DeleteResult.DELETED

    def deactivate(self) -> None:
        if self.id is None:
            raise RuntimeError("Livro não foi salvo ainda.")
        if self.active == False: return
        self.active = False
        self.save()

    def decrease_amount(self):
        if self is None:
            raise ValueError("O livro não foi encontrado")
        if self.amount < 1: return
        self.amount -= 1
        
    # ── Consultas ─────────────────────────────────────────────────
    @classmethod
    def is_available(cls, book_id: int) -> bool:
        """Verifica se o livro especificado tem quantidade suficiente ou está ativo"""
        book = cls.find_by_id(book_id)
        if book is None:
            raise ValueError("O livro não foi encontrado")
        return book.amount > 0 or book.active

    #@classmethod
    #def decrease_amount(cls, book_id: int) -> None:
    #    book = cls.find_by_id(book_id)
    #    if book is None:
    #        raise ValueError("O livro não foi encontrado")
    #    if book.amount < 1: return
    #    book.amount -= 1

    @classmethod
    def find_by_id(cls, book_id: int) -> Optional["Book"]:
        data = db.get("books", book_id)
        return cls._from_data(data) if data else None

    # ── Auxiliar ──────────────────────────────────────────────────
    @classmethod
    def _from_data(cls, data) -> "Book":
        '''Reconstrói o objeto com dados vindos do banco'''
        return cls(
            id=data["id"],
            title=data["title"],
            author=data["author"],
            year=data["year"],
            image=data["image"],
            amount=data["amount"],
            active=data["active"]
        )