class DomainError(Exception):
    """Classe-base para erros de regra de negócio do domínio."""
    pass

class InvalidCredentialsError(DomainError):
    def __init__(self, *args):
        super().__init__("Usuário ou senha inválidos", *args)



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

class BookInactiveError(DomainError):
    def __init__(self, *args: object):
        super().__init__('Livro está desativado', *args)



class UserNotFoundError(DomainError):
    def __init__(self, *args: object):
        super().__init__('Usuário não encontrado', *args)

class UserInactiveError(DomainError):
    def __init__(self, *args):
        super().__init__("Usuário desativado. Contate o administrador.", *args)




class ClientNotFoundError(DomainError):
    def __init__(self, *args: object):
        super().__init__('Cliente não encontrado', *args)

class ClientMaxLoansReachedError(DomainError):
    def __init__(self, *args: object):
        super().__init__('Cliente chegou no limite máximo de empréstimos permitido', *args)

class ClientInactiveError(DomainError):
    def __init__(self, *args):
        super().__init__("Cliente desativado. Contate o administrador.", *args)