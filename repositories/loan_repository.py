import database.db as db

class LoanRepository:
    @staticmethod
    def save(loan):
        """Salva um empréstimo no banco de dados. Se o empréstimo já existir, atualiza seus dados."""
        if loan.id is None:
            loan.id = db.write("loans", loan.__dict__)
        else:
            db.update("loans", loan.id, loan.__dict__)
        return loan

    @staticmethod
    def delete(loan):
        """Deleta um empréstimo do banco de dados."""
        if loan.id is None:
            raise RuntimeError("Empréstimo não foi salvo ainda.")
        db.delete("loans", loan.id)
        loan.id = None

    @staticmethod
    def find_by_id(loan_id: int):
        """Busca um empréstimo pelo seu ID. Retorna None se não encontrado."""
        loan_data = db.get("loans", loan_id)
        return loan_data

    @staticmethod
    def all(filter_expression=lambda loan: True):
        """De acordo com o filtro especificado, retorna empréstimos cadastrados."""
        loans = []
        for k, v in db.read().items():
            if not type(v).__name__ == "dict": continue
            if not k == "loans": continue
            for _, loan in v.items():
                if loan is None: continue
                if not filter_expression(loan): continue
                loans.append(loan)
        return loans