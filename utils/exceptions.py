class DomainError(Exception):
    """Classe-base para erros de regra de negócio do domínio."""
    pass

class LoanNotFoundError(DomainError):
    def __init__(self, *args: object):
        super().__init__('Empréstimo não encontrado', *args)

class LoanAlreadyExistsError(DomainError):
    def __init__(self, *args: object):
        super().__init__('Empréstimo já existe', *args)

class BookUnavailableError(DomainError):
    def __init__(self, *args: object):
        super().__init__('Livro indisponível', *args)

class BookNotFoundError(DomainError):
    def __init__(self, *args: object):
        super().__init__('Livro não encontrado', *args)

class BookDeactiveError(DomainError):
    def __init__(self, *args: object):
        super().__init__('Livro está desativado', *args)

class UserNotFoundError(DomainError):
    def __init__(self, *args: object):
        super().__init__('Usuário não encontrado', *args)

class UserMaxLoansReachedError(DomainError):
    def __init__(self, *args: object):
        super().__init__('Usuário chegou no limite máximo de empréstimos permitido', *args)

class UserDeactiveError(DomainError):
    def __init__(self, *args: object):
        super().__init__('Usuário está desativado', *args)