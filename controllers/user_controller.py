"""
CONTROLLER: UserController
Responsável por lidar com as requisições relacionadas aos usuários.
"""
from typing import Optional

from utils.exceptions import DomainError
from utils.enums import UserRole

from services.user_service import UserService

class UserController:
    # ── Criação ───────────────────────────────────────────────────
    @staticmethod
    def create(
        name: str, 
        username: str,
        password_plain: str,
        role: str = UserRole.OP.value
    ) -> dict:
        try:
            result = UserService.create(name=name, username=username, password_plain=password_plain, role=role)
            return {"success": True, "data": result}
        except DomainError as e:
            return {"success": False, "error": str(e)}

    # ── Leitura ───────────────────────────────────────────────────
    @staticmethod
    def list_all() -> dict:
        result = UserService.list_all()
        return {"success": True, "data": result}

    @staticmethod
    def update(user_id: int, name: str, password_plain: str) -> dict:
        try:
            result = UserService.update(user_id, name, password_plain)
            return {"success": True, "data": result}
        except DomainError as e:
            return {"success": False, "error": str(e)}
    
    # ── Remoção ───────────────────────────────────────────────────
    @staticmethod
    def delete(user_id: int) -> dict:
        try:
            result = UserService.remove(user_id)
            return {"success": True, "data": f"Usuário #{user_id} {result.value} com sucesso."}
        except DomainError as e:
            return {"success": False, "error": str(e)}