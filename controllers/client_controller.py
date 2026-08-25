"""
CONTROLLER: ClientController
Responsável por lidar com as requisições relacionadas aos usuários.
"""
from typing import Optional

from utils.exceptions import DomainError

from services.client_service import ClientService

class ClientController:
    # ── Criação ───────────────────────────────────────────────────
    @staticmethod
    def create(
        name: str, 
        email: str,
        registered_by: int
    ) -> dict:
        try:
            result = ClientService.create(name=name, email=email, registered_by=registered_by)
            return {"success": True, "data": result}
        except DomainError as e:
            return {"success": False, "error": str(e)}

    # ── Leitura ───────────────────────────────────────────────────
    @staticmethod
    def list_all() -> dict:
        result = ClientService.list_all()
        return {"success": True, "data": result}

    @staticmethod
    def update(user_id: int, info_update: dict[str, any]) -> dict: #type: ignore
        try:
            result = ClientService.update(user_id, info_update)
            return {"success": True, "data": result}
        except DomainError as e:
            return {"success": False, "error": str(e)}
    
    # ── Remoção ───────────────────────────────────────────────────
    @staticmethod
    def delete(user_id: int) -> dict:
        try:
            result = ClientService.remove(user_id)
            return {"success": True, "data": f"Usuário #{user_id} {result.value} com sucesso."}
        except DomainError as e:
            return {"success": False, "error": str(e)}