from models.user import User

class AppSession:
    """Guarda o usuário atualmente autenticado durante a execução do programa."""
    _current_user: User | None = None

    @classmethod
    def login(cls, user: User) -> None:
        cls._current_user = user

    @classmethod
    def logout(cls) -> None:
        cls._current_user = None

    @classmethod
    def current_user(cls) -> User | None:
        return cls._current_user

    @classmethod
    def non_none_current_user(cls) -> User | str:
        return "Usuário" if cls._current_user is None else cls._current_user 

    @classmethod
    def is_authenticated(cls) -> bool:
        return cls._current_user is not None