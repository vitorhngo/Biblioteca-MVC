"""
CONTROLLER: BookController
Responsável por lidar com as requisições relacionadas aos livros.
"""
from typing import Optional

from utils.exceptions import DomainError, BookNotFoundError

from services.book_service import BookService

class BookController:
    # ── Criação ───────────────────────────────────────────────────
    @staticmethod
    def create(
        title: str, 
        author: str, 
        year: int,
        image: Optional[str] = None,
        amount: int = 1
    ) -> dict:
        try:
            result = BookService().create(title=title, author=author, year=year, image=image, amount=amount)
            return {"success": True, "data": result}
        except DomainError as e:
            return {"success": False, "error": str(e)}
        
    @staticmethod
    def update(book_id: int, info_update: dict[str, any]) -> dict: # type: ignore
        try:
            result = BookService().update(book_id, info_update)
            return {"success": True, "data": result}
        except DomainError as e:
            return {"success": False, "error": str(e)}
        
    # ── Remoção ───────────────────────────────────────────────────
    @staticmethod
    def delete(book_id: int) -> dict:
        try:
            result = BookService().remove(book_id)
            return {"success": True, "data": f"Livro #{book_id} {result.value} com sucesso."}
        except BookNotFoundError:
            return {"success": False, "error": f"Livro #{book_id} não encontrado."}