"""
MODEL: User
Responsável pela lógica de dados e regras de negócio do usuário.
"""
from dataclasses import dataclass
from typing import Optional
import re

from utils.exceptions import DomainError

from repositories.user_repository import UserRepository

@dataclass
class User:
    name: str
    email: str
    active: bool = True
    id: Optional[int] = None
    created_at: Optional[str] = None

    # ── Validação ────────────────────────────────────────────────
    def validate(self) -> None:
        if not self.name.strip():
            raise DomainError("Nome não pode ser vazio.")
        if not re.match(r"[^@]+@[^@]+\.[^@]+", self.email):
            raise DomainError(f"E-mail inválido: {self.email!r}")

    def register(self):
        self.validate()
        UserRepository.save(self)
        return self

    def delete(self):
        if self.id is None:
            raise RuntimeError("Usuário não foi salvo ainda.")
        UserRepository.delete(self)
        self.id = None

    def deactivate(self) -> None:
        if self.id is None:
            raise RuntimeError("Usuário não foi salvo ainda.")
        if self.active == False: return
        self.active = False
        UserRepository.save(self)

    # ── Consultas ─────────────────────────────────────────────────
    @classmethod
    def find_by_id(cls, user_id: int) -> Optional["User"]:
        """Busca um usuário pelo seu ID. Retorna None se não encontrado."""
        user_data = UserRepository.find_by_id(user_id)
        return cls(**user_data) if user_data else None

    @classmethod
    def find_by_email(cls, email: str) -> Optional["User"]:
        """Busca um usuário pelo seu e-mail. Retorna None se não encontrado."""
        user_data = UserRepository.find_by_email(email)
        return cls(**user_data) if user_data else None

    @classmethod
    def all(cls) -> list["User"]:
        """Retorna todos os usuários cadastrados."""
        users_data = UserRepository.all()
        return [cls(**user) for user in users_data]