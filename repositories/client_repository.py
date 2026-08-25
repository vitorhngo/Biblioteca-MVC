"""
REPOSITORY: ClientRepository
Responsável por interagir com o banco de dados para operações relacionadas ao cliente.
"""
import database.db as db

class ClientRepository:
    @staticmethod
    def save(client):
        """Salva um cliente no banco de dados. Se o cliente já existir, atualiza seus dados."""
        if client.id is None:
            client.id = db.write("clients", client.__dict__)
        else:
            db.update("clients", client.id, client.__dict__)
        return client

    @staticmethod
    def delete(client):
        """Deleta um cliente do banco de dados."""
        if client.id is None:
            raise RuntimeError("Usuário não foi salvo ainda.")
        db.delete("clients", client.id)
        client.id = None

    @staticmethod
    def find_by_id(user_id: int):
        """Busca um cliente pelo seu ID. Retorna None se não encontrado."""
        user_data = db.get("clients", user_id)
        return user_data

    @staticmethod
    def find_by_email(email: str):
        """Busca um cliente pelo seu e-mail. Retorna None se não encontrado."""
        for k, v in db.read().items():
            if not type(v).__name__ == "dict": continue
            if not k == "clients": continue
            for _, client in v.items():
                if client is None: continue
                if client["email"] != email.lower(): continue
                return client
        return None
        
    @staticmethod
    def all(filter_by=lambda client: True):
        """De acordo com o filtro especificado, retorna clientes cadastrados."""
        clients = []
        for k, v in db.read().items():
            if not type(v).__name__ == "dict": continue
            if not k == "clients": continue
            for _, client in v.items():
                if client is None: continue
                if filter_by(client):
                    clients.append(client)
        return clients

    @staticmethod
    def find_by_username(username: str) -> dict | None:
        matches = ClientRepository.all(
            filter_by=lambda client: client["username"] == username
        )
        return matches[0] if matches else None