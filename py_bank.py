from datetime import datetime as dt


class Company:
    def __init__(self,
                 id: int,
                 name: str,
                 vat_id: str,
                 street_and_number: str,
                 postal_code: str,
                 city: str,
                 country:str,
                 contact_person:str) -> None:
        self.id: int = id
        self.name: str = name
        self.vat_id: str = vat_id
        self.street_and_number: str = street_and_number
        self.postal_code: str = postal_code
        self.city: str = city
        self.country:str = country
        self.contact_person: str = contact_person


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

class Transaction:
    def __init__(self,
                 id: int,
                 created_at: dt,
                 transaction_type: str,
                 amount: float,
                 author:str) -> None:
        self.id: int = id
        self.created_at: dt = created_at
        self.transaction_type: str = transaction_type
        self.amount: float = amount
        self.author:str = author
                 

class BankAccount:
    def __init__(self,
                 id: int,
                 account_number: str, # BA2023-04-00042
                 account_owner: Company,
                 currency: Currency,
                 opening_amount: float,
                 ) -> None:
        
         self.id:int = id
         self.account_number:str = account_number
         self.account_owner: Company = account_owner
         self.currency: Currency = currency
         self.opening_amount: float = opening_amount
         self.transactions: list[Transaction] = []
         self.add_transaction(opening_amount)

    
    def __str__(self) -> str:
        return f'{self.account_number}- {self.opening_amount}  {self.currency}'
    
    def add_transaction(self, opening_amount):
        transaction = Transaction( 1,
                                  dt.now(),
                                  'Otvaranje racuna',
                                  )
        self.transactions.append()
        
        
account_number = f'BA-{dt.now().year} - {dt.now().month}-{"42".zfill(5)}'      
account_owner = Company(1,
                        'Firma',
                        '123456879985',
                        'Ulica i broj',
                        '10090',
                        'Zagreb',
                        'Hrvatska',
                        'Ana Anic')  
currency = Currency(1, 'EUR', 'EURO')      
bank_account =  BankAccount(1,
                            account_number,
                            account_owner,
                            currency,
                            10_999.99,) 


print(bank_account)
print(bank_account.currency)