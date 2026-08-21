'''Nunca retorna dados, somente relatórios: Deu certo? O que deu certo?'''

from models.book import Book

from services.book_service import BookService

import utils.exceptions as exc

class BookController:

    # ── Criação ───────────────────────────────────────────────────
    def create(
        self,
        title: str, 
        author: str, 
        year: int,
        image = None,
        amount: int = 1
    ) -> dict:
        try:
            book = Book(
                title=title.strip(), 
                author=author.strip(), 
                year=year,
                amount=amount
            ).save()
            return {"success": True, "data": book}
        except exc.DomainError as e:
            return {"success": False, "error": str(e)}
        
    # ── Remoção ───────────────────────────────────────────────────
    def delete(self, book_id: int) -> dict:
        try:
            result = BookService().remove(book_id)
            return {"success": True, "data": f"Livro #{book_id} {result.value} com sucesso."}
        except exc.BookNotFoundError:
            return {"success": False, "error": f"Livro #{book_id} não encontrado."}