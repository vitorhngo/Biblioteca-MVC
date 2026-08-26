from utils.exceptions import DomainError, InvalidCredentialsError
from services.auth_service import AuthService
from services.user_service import UserService

from utils.enums import UserRole

class AuthController:
    @staticmethod
    def login(username: str, password: str) -> dict:
        try:
            user = AuthService.login(username, password)
            return {"success": True, "data": user}
        except DomainError as e:
            return {"success": False, "error": str(e)}
        except ValueError as e:
            return {"success": False, "error": str(InvalidCredentialsError())}

    @staticmethod
    def create_adm_user() -> dict:
        try:
            result = UserService.create(name="admin", username="admin", password_plain="123", role=UserRole.ADMIN.value)
            return {"success": True, "data": result}
        except DomainError as e:
            return {"success": False, "error": str(e)}