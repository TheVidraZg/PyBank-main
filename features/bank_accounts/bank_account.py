from datetime import datetime as dt

from ..companies import Company
from .transactions import Transaction
from ..shared import Currency


class BankAccount:
    def __init__(self,
                 id: int,
                 account_number: str, # BA-2023-04-00042
                 account_owner: Company,
                 currency: Currency,
                 opening_amount: float) -> None:
        self.id: int = id
        self.account_number: str = account_number
        self.account_owner: Company = account_owner
        self.currency: Currency = currency
        self.transactions: list[Transaction] = []
        self.add_opening_transaction(opening_amount)

    def __str__(self) -> str:
        return f'{self.account_number} - {self.currency}'

    def add_opening_transaction(self, opening_amount):
        transaction = Transaction(
            1,
            dt.now(),
            'Otvaranje racuna',
            opening_amount,
            self.account_owner.contact_person
        )
        self.add_transaction(transaction)


    def add_transaction(self, transaction: Transaction):
        self.transactions.append(transaction)