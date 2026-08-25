"""
SERVICE: ClientService
Responsável por coordenar a lógica de negócio do cliente, interagindo com o repositório e o modelo.
"""
from typing import Optional

from utils import enums
from utils.exceptions import DomainError, ClientNotFoundError, UserNotFoundError

from models.loan import Loan
from models.client import Client

from repositories.user_repository import UserRepository
from repositories.client_repository import ClientRepository
from repositories.loan_repository import LoanRepository

class ClientService:
    @staticmethod
    def create(
            name: str,
            email: str,
            registered_by: int
        ) -> Client:
        client = Client(name=name, email=email, registered_by=registered_by)
        client.validate()
        client.format_data()

        if not UserRepository.find_by_id(client.registered_by):
            raise UserNotFoundError()
        if ClientRepository.find_by_email(client.email):
            raise DomainError(f"E-mail {client.email!r} já cadastrado.")

        ClientRepository.save(client)
        return client

    @staticmethod
    def update(user_id: int, info_update: dict[str, any]) -> Client: # type: ignore
        data = ClientRepository.find_by_id(user_id)
        if data is None:
            raise ClientNotFoundError()

        for key, value in data.items():
            new_value = info_update.get(key)
            if new_value is not None and new_value != value:
                    data[key] = new_value
        
        client = Client(**data)
        client.validate()
        client.format_data()
        ClientRepository.save(client)
        return client

    @staticmethod
    def remove(user_id: int) -> enums.DeleteResult:
        data = ClientRepository.find_by_id(user_id)
        if data is None:
            raise ClientNotFoundError()
        
        client = Client(**data)
        if LoanRepository.all_active_for_user(user_id):
            client.active = False
            ClientRepository.save(client)
            return enums.DeleteResult.DEACTIVATED

        ClientRepository.delete(client)
        return enums.DeleteResult.DELETED

    @staticmethod
    def list_all() -> list[Client]:
        return ClientRepository.all()