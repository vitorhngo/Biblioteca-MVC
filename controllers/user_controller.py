'''Nunca retorna dados, somente relatórios: Deu certo? O que deu certo?'''
from typing import Optional
from models.user import User

class UserController:
    # ── Criação ───────────────────────────────────────────────────
    def create(
        self,
        name: str, 
        email: str,
    ) -> dict:
        if User.find_by_email(email):
            return {"success": False, "error": f"E-mail {email!r} já cadastrado."}
        try:
            user = User(name=name.strip(), email=email.strip().lower()).save()
            return {"success": True, "data": user}
        except ValueError as exc:
            return {"success": False, "error": str(exc)}

    # ── Leitura ───────────────────────────────────────────────────
    def get_by_id(self, user_id: int) -> dict:
        user = User.find_by_id(user_id)
        if user is None:
            return {"success": False, "error": f"Usuário #{user_id} não encontrado."}
        return {"success": True, "data": user}

    def list_all(self) -> dict:
        users = User.all()
        return {"success": True, "data": users}

    def update(self, user_id: int, name: Optional[str] = None, email: Optional[str] = None) -> dict:
        user = User.find_by_id(user_id)
        if user is None:
            return {"success": False, "error": f"Usuário #{user_id} não encontrado."}
        if name:
            user.name = name.strip()
        if email:
            user.email = email.strip()
        try:
            user.save()
            return {"success": True, "data": user}
        except ValueError as exc:
            return {"success": False, "error": str(exc)}
    
    # ── Remoção ───────────────────────────────────────────────────
    def delete(self, user_id: int) -> dict:
        user = User.find_by_id(user_id)
        if user is None:
            return {"success": False, "error": f"Usuário #{user_id} não encontrado."}
        result = user.delete()
        return {"success": True, "data": f"Usuário #{user_id} {result.value} com sucesso."}