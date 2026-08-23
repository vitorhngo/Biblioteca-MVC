"""
SERVICE: BookService
Responsável por coordenar a lógica de negócio do livro, interagindo com o repositório e o modelo.
"""
from typing import Optional

from utils import enums
from utils.exceptions import BookNotFoundError

from repositories.book_repository import BookRepository
from repositories.loan_repository import LoanRepository

from models.book import Book

class BookService:
    @staticmethod
    def create(
            title: str,
            author: str,
            year: int,
            amount: int = 1,
            image = None
        ) -> Book:
        """Cria um novo livro coordenando o fluxo de persistência."""
        book = Book(
            title=title,
            author=author,
            year=year,
            amount=amount,
            image=image
        )
        book.validate()
        book.format_data()
        BookRepository.save(book)
        return book

    @staticmethod
    def update(book_id: int, info_update: dict[str, any]) -> Book: # type: ignore
        """Muda informações de um livro dinamicamente. Se o livro não existir, lança BookNotFoundError."""
        data = BookRepository.find_by_id(book_id)
        if data is None:
            raise BookNotFoundError()

        for key, value in data.items():
            new_value = info_update.get(key)
            if new_value is not None and new_value != value:
                    data[key] = new_value

        book = Book(**data)
        book.validate()
        book.format_data()
        BookRepository.save(book)
        return book

    @staticmethod
    def remove(book_id: int) -> enums.DeleteResult:
        """Remove um livro do repositório. Se o livro não existir, lança BookNotFoundError."""
        data = BookRepository.find_by_id(book_id)
        if data is None:
            raise BookNotFoundError()
        
        book = Book(**data)

        if LoanRepository.all_active_for_book(book_id):
            book.active = False
            BookRepository.save(book)
            return enums.DeleteResult.DEACTIVATED
        
        BookRepository.delete(book)
        return enums.DeleteResult.DELETED