from utils.exceptions import DomainError, InvalidCredentialsError
from services.auth_service import AuthService

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