# services/auth_service.py
import bcrypt

import utils.exceptions as exc
from models.user import User
from repositories.user_repository import UserRepository

class AuthService:
    @staticmethod
    def hash_password(password_plain: str) -> str:
        """Usado ao cadastrar/trocar senha de um usuário."""
        hashed = bcrypt.hashpw(password_plain.encode("utf-8"), bcrypt.gensalt())
        return hashed.decode("utf-8")

    @staticmethod
    def login(username: str, password_plain: str) -> User:
        data = UserRepository.find_by_username(username)
        if data is None:
            raise exc.InvalidCredentialsError()

        user = User(**data)

        if not user.active:
            raise exc.UserInactiveError()

        correct_password = bcrypt.checkpw(
            password_plain.encode("utf-8"),
            user.password_hash.encode("utf-8"),
        )
        print(username, password_plain, correct_password, user)
        if not correct_password:
            raise exc.InvalidCredentialsError()

        return user