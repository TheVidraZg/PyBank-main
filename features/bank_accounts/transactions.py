from datetime import datetime as dt


class Transaction:
    def __init__(self,
                 id: int,
                 create_at: dt,
                 transaction_type: str,
                 amount: float,
                 author: str) -> None:
        self.id: int = id
        self.create_at: dt = create_at
        self.transaction_type: str = transaction_type
        self.amount: float = amount
        self.author: str = author

    def __str__(self) -> str:
        return f'{self.create_at} {self.transaction_type} {self.amount}'