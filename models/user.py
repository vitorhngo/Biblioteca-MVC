"""
MODEL: User
Responsável pela lógica de dados e regras de negócio do usuário.
"""
from dataclasses import dataclass
from typing import Optional
import re

import database.db as db

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
            raise ValueError("Nome não pode ser vazio.")
        if not re.match(r"[^@]+@[^@]+\.[^@]+", self.email):
            raise ValueError(f"E-mail inválido: {self.email!r}")

    # ── Persistência ─────────────────────────────────────────────
    def save(self) -> "User":
        """Insere ou atualiza o usuário no banco."""
        self.validate()
        if self.id is None:
            self.id = db.write("users", {
            "name": self.name,
            "email": self.email,
            "active": self.active
            }
        )
        else:
            db.update("users", self.id, {
            "name": self.name,
            "email": self.email,
            "active": self.active
            }
        )
        return self

    def delete(self):
        if self.id is None:
            raise RuntimeError("Usuário não foi salvo ainda.")
        db.delete("users", self.id)
        self.id = None

    def deactivate(self) -> None:
        if self.id is None:
            raise RuntimeError("Usuário não foi salvo ainda.")
        if self.active == False: return
        self.active = False
        self.save()

    # ── Consultas ─────────────────────────────────────────────────
    @classmethod
    def find_by_id(cls, user_id: int) -> Optional["User"]:
        data = db.get("users", user_id)
        return cls._from_data(data) if data else None

    @classmethod
    def find_by_email(cls, email: str) -> Optional["User"]:
        for k, v in db.read().items():
            if not type(v).__name__ == "dict": continue
            if not k == "users": continue
            for _, user in v.items():
                if user is None: continue
                if user["email"] != email.lower(): continue
                return cls._from_data(user) if user else None

    @classmethod
    def all(cls) -> list["User"]:
        users = []
        for k, v in db.read().items():
            if not type(v).__name__ == "dict": continue
            if not k == "users": continue
            for _, user in v.items():
                if user is None: continue
                users.append(user)
        return [cls._from_data(u) for u in users]

    # ── Auxiliar ──────────────────────────────────────────────────
    @classmethod
    def _from_data(cls, data) -> "User":
        '''Reconstrói o objeto com dados vindos do banco'''
        return cls(
            id=data["id"],
            name=data["name"],
            email=data["email"],
            active=data["active"]
        )

    def __str__(self) -> str:
        return f"User(id={self.id}, name={self.name!r}, email={self.email!r})"