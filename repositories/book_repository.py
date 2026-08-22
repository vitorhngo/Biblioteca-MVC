import database.db as db

class BookRepository:
    @staticmethod
    def save(book):
        """Salva um livro no banco de dados. Se o livro já existir, atualiza seus dados."""
        if book.id is None:
            book.id = db.write("books", book.__dict__)
        else:
            db.update("books", book.id, book.__dict__)
        return book

    @staticmethod
    def delete(book):
        """Deleta um livro do banco de dados."""
        if book.id is None:
            raise RuntimeError("Livro não foi salvo ainda.")
        db.delete("books", book.id)
        book.id = None

    @staticmethod
    def find_by_id(book_id: int):
        """Busca um livro pelo seu ID. Retorna None se não encontrado."""
        book_data = db.get("books", book_id)
        return book_data