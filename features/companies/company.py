

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