from sqlalchemy import (Column,
                        Integer,
                        String,
                        ForeignKey)
from sqlalchemy.orm import (declarative_base,
                            relationship,
                            backref)


Base = declarative_base()
class SaCompany(Base):
    __tablename__= 'sa_companies'
    id = Column(Integer(),
                primary_key=True,
                autoincrement=True)
    name = Column(String(150),
                  nullable=False)
    vat_id = Column(String(11),
                  nullable=False)
    street_and_number = Column(String(500),
                  nullable=False)
    postal_code = Column(String(20),
                  nullable=False)
    city = Column(String(150),
                  nullable=False)
    country = Column(String(150),
                  nullable=False)
    contact_person = Column(Integer(),
                ForeignKey('Sa_employes.id'),
                nullable=False)
    
    employees = relationship('SaEmployee',
                            backref=backref('company'))
class SaEmployee(Base):
    id = Column(Integer(),
                primary_key=True
                autoincrement=True)
    first_name = Column(String(150),
                  nullable=False)
    last_name = Column(String(150),
                  nullable=False)
    e_mail = Column(String(150),
                  nullable=False)
    phone_num = Column(String(50),
                  nullable=False)
    
    company_id = Column(Integer(),
                ForeignKey('sa_employes.id'),
                nullable=False)
    

firma = SaCompany()

firma.employees

employees = SaEmployee
employees.company