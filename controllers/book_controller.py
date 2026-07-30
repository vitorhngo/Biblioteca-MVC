'''Nunca retorna dados, somente relatórios: Deu certo? O que deu certo?'''

from models.book import Book
from models.user import User

import datamodels.exceptions as exc

class BookController:

    # ── Criação ───────────────────────────────────────────────────
    def create(
        self,
        title: str, 
        author: str, 
        year: int,
        image: str,
        amount: int
    ) -> dict:
        try:
            book = Book(
                title=title.strip(), 
                author=author.strip(), 
                year=year,
                image=image,
                amount=amount
            ).save()
            return {"success": True, "data": book}
        except ValueError as exc:
            return {"success": False, "error": str(exc)}
        
    # ── Remoção ───────────────────────────────────────────────────
    def delete(self, book_id: int) -> dict:
        book = Book.find_by_id(book_id)
        if book is None:
            return {"success": False, "error": f"Livro #{book_id} não encontrado."}
        result = book.delete()
        return {"success": True, "data": f"Livro #{book_id} {result.value} com sucesso."}
        