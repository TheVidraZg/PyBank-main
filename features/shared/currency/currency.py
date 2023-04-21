


class Currency:
    def __init__(self,
                 id: int,
                 symbol: str,
                 name: str) -> None:
        self.id: int = id
        self.symbol: str = symbol
        self.name: str = name
        
    def __str__(self) -> str:
        return f'{self.symbol}'

