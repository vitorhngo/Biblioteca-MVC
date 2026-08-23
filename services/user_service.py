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

class UserService:
    @staticmethod
    def create(
            name: str,
            email: str
        ) -> User:
        if UserRepository.find_by_email(email):
            raise DomainError(f"E-mail {email!r} já cadastrado.")
        user = User(name=name, email=email)
        user.validate()
        user.format_data()
        UserRepository.save(user)
        return user

    @staticmethod
    def update(user_id: int, info_update: dict[str, any]) -> User: # type: ignore
        data = UserRepository.find_by_id(user_id)
        if data is None:
            raise UserNotFoundError()

        for key, value in data.items():
            new_value = info_update.get(key)
            if new_value is not None and new_value != value:
                    data[key] = new_value
        
        user = User(**data)
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