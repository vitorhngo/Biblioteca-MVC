'''Nunca retorna dados, somente relatórios: Deu certo? O que deu certo?'''
from typing import Optional

from utils.exceptions import DomainError

from services.user_service import UserService

class UserController:
    # ── Criação ───────────────────────────────────────────────────
    @staticmethod
    def create(
        name: str, 
        email: str,
    ) -> dict:
        try:
            result = UserService.create(name=name, email=email)
            return {"success": True, "data": result}
        except DomainError as e:
            return {"success": False, "error": str(e)}

    # ── Leitura ───────────────────────────────────────────────────
    @staticmethod
    def list_all() -> dict:
        result = UserService.list_all()
        return {"success": True, "data": result}

    @staticmethod
    def update(user_id: int, name: Optional[str], email: Optional[str]) -> dict:
        try:
            result = UserService.update(user_id, name, email)
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