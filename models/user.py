"""
MODEL: User
Responsável pela lógica regras de negócio do usuário.
"""
from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from utils.exceptions import DomainError
from utils.constants import DB_DATE_FORMAT
from utils.enums import UserRole

@dataclass
class User:
    username: str
    password_hash: str
    name: str
    role: str
    active: bool = True
    id: Optional[int] = None
    created_at: Optional[str] = datetime.now().strftime(DB_DATE_FORMAT)
    updated_at: Optional[str] = None

    # ── Validação ────────────────────────────────────────────────
    def validate(self) -> None:
        if self.name.isdigit():
            raise DomainError("Nome não pode ser numérico.")
        if not self.name.strip():
            raise DomainError("Nome não pode ser vazio.")

        if self.username.isdigit():
            raise DomainError("Nome de usuário não pode ser numérico.")
        if not self.username.strip():
            raise DomainError("Nome de usuário não pode ser vazio.")
        
        if not self.password_hash.strip():
            raise DomainError("Senha não pode ser vazio.")

        if not self.role in UserRole:
            raise DomainError("Cargo de usuário inválido")

    def format_data(self) -> "User":
        self.name = self.name.strip().upper()
        self.username = self.username.strip().upper()
        self.password_hash = self.password_hash.strip()
        return self