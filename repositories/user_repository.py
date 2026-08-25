"""
REPOSITORY: UserRepository
Responsável por interagir com o banco de dados para operações relacionadas ao usuário.
"""
import database.db as db

class UserRepository:
    @staticmethod
    def save(user):
        """Salva um usuário no banco de dados. Se o usuário já existir, atualiza seus dados."""
        if user.id is None:
            user.id = db.write("users", user.__dict__)
        else:
            db.update("users", user.id, user.__dict__)
        return user

    @staticmethod
    def delete(user):
        """Deleta um usuário do banco de dados."""
        if user.id is None:
            raise RuntimeError("Usuário não foi salvo ainda.")
        db.delete("users", user.id)
        user.id = None

    @staticmethod
    def find_by_id(user_id: int):
        """Busca um usuário pelo seu ID. Retorna None se não encontrado."""
        user_data = db.get("users", user_id)
        return user_data

    @staticmethod
    def all(filter_by=lambda user: True):
        """De acordo com o filtro especificado, retorna usuários cadastrados. Se tiver no filtro retorna o usuário."""
        users = []
        for k, v in db.read().items():
            if not type(v).__name__ == "dict": continue
            if not k == "users": continue
            for _, user in v.items():
                if user is None: continue
                if filter_by(user):
                    users.append(user)
        return users

    @staticmethod
    def find_by_username(username: str) -> dict | None:
        matches = UserRepository.all(
            filter_by=lambda user: user["username"] == username
        )
        return matches[0] if matches else None