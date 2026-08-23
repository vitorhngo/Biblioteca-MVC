"""
MODEL: User
Responsável pela lógica regras de negócio do usuário.
"""
from dataclasses import dataclass
from datetime import datetime
from typing import Optional
import re

from utils.exceptions import DomainError
from utils.constants import DB_DATE_FORMAT

@dataclass
class User:
    name: str
    email: str
    active: bool = True
    id: Optional[int] = None
    created_at: Optional[str] = datetime.now().strftime(DB_DATE_FORMAT)
    updated_at: Optional[str] = None

    # ── Validação ────────────────────────────────────────────────
    def validate(self) -> None:
        if not self.name.strip():
            raise DomainError("Nome não pode ser vazio.")
        if not re.match(r"[^@]+@[^@]+\.[^@]+", self.email):
            raise DomainError(f"E-mail inválido: {self.email!r}")

    def format_data(self) -> User:
        self.name = self.name.strip()
        self.email = self.email.strip().lower()
        return self