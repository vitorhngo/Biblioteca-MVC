from typing import Optional

from utils import enums
from utils.exceptions import DomainError, UserNotFoundError

from models.loan import Loan
from models.user import User

class UserService:
    @staticmethod
    def create(
            name: str,
            email: str
        ) -> User:
        if User.find_by_email(email):
            raise DomainError(f"E-mail {email!r} já cadastrado.")
        user = User(name=name, email=email)
        user.register()
        return user

    @staticmethod
    def update(user_id: int, name: Optional[str], email: Optional[str]) -> User:
        user = User.find_by_id(user_id)
        if user is None:
            raise UserNotFoundError()
        if name:
            user.name = name.strip()
        if email:
            user.email = email.strip().lower()
        user.register()
        return user

    @staticmethod
    def remove(user_id: int) -> enums.DeleteResult:
        user = User.find_by_id(user_id)
        if user is None:
            raise UserNotFoundError()

        if Loan.all_active_for_user(user_id):
            user.deactivate()
            return enums.DeleteResult.DEACTIVATED

        user.delete()
        return enums.DeleteResult.DELETED

    @staticmethod
    def list_all() -> list[User]:
        return User.all()