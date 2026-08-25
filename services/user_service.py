"""
SERVICE: UserService
Responsável por coordenar a lógica de negócio do usuário, interagindo com o repositório e o modelo.
"""
from typing import Optional

from utils import enums
from utils.exceptions import DomainError, UserNotFoundError

from models.loan import Loan
from models.user import User

from repositories.user_repository import UserRepository
from repositories.loan_repository import LoanRepository

from services.auth_service import AuthService

class UserService:
    @staticmethod
    def create(
            name: str,
            username: str,
            password_plain: str
        ) -> User:
        user = User(
            name=name,
            username=username,
            password_hash=AuthService.hash_password(password_plain)
        )
        user.validate()
        user.format_data()

        if UserRepository.find_by_username(user.username):
            raise DomainError(f"Nome de usuário {user.username!r} já cadastrado.")
        
        UserRepository.save(user)
        return user

    @staticmethod
    def update(user_id: int, name: str, password_plain: str) -> User: #type: ignore
        data = UserRepository.find_by_id(user_id)
        if data is None:
            raise UserNotFoundError()

        user = User(**data)
        user.name = name
        user.password_hash = AuthService.hash_password(password_plain)
        user.validate()
        user.format_data()
        UserRepository.save(user)
        return user

    @staticmethod
    def remove(user_id: int) -> enums.DeleteResult:
        data = UserRepository.find_by_id(user_id)
        if data is None:
            raise UserNotFoundError()
        
        user = User(**data)
        if LoanRepository.all_active_for_user(user_id):
            user.active = False
            UserRepository.save(user)
            return enums.DeleteResult.DEACTIVATED

        UserRepository.delete(user)
        return enums.DeleteResult.DELETED

    @staticmethod
    def list_all() -> list[User]:
        return UserRepository.all()