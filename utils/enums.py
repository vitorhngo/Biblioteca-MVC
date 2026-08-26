from enum import Enum

class DeleteResult(Enum):
    DELETED = "deletado"
    DEACTIVATED = "desativado"

class UserRole(Enum):
    ADMIN = "admin"
    OP = "operador"