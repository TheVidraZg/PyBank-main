from sqlalchemy import (create_engine,
    Column, Integer, String, ForeignKey)

from sqlalchemy.orm import (sessionmaker,
    declarative_base, relationship, backref)


Base = declarative_base()

class SaCompany(Base):
    __tablename__ = 'sa_companies'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(150), nullable=False)
    vat_id = Column(String(11), nullable=False)
    street_and_number = Column(String(500), nullable=True)
    postal_code = Column(String(20), nullable=True)
    city = Column(String(150), nullable=False)
    country = Column(String(150), nullable=False)
    email = Column(String(150), nullable=True)
    phone = Column(String(50), nullable=True)

    employees = relationship('SaEmployee',
                             backref=backref('company'))


class SaEmployee(Base):
    __tablename__ = 'sa_employees'
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(150), nullable=True)
    last_name = Column(String(150), nullable=False)
    email = Column(String(150), nullable=True)
    phone = Column(String(50), nullable=True)

    company_id = Column(Integer, ForeignKey('sa_companies.id'), nullable=False)



def main():
    db_path = 'sqlite:///db_data/py_bank.db'
    db_engine = create_engine(db_path)
    Base.metadata.create_all(db_engine)


    Session = sessionmaker()
    Session.configure(bind=db_engine)
    session = Session()

    employees = (
        session.query(SaEmployee)
        .join(SaCompany)
        .all()
    )
    for employee in employees:
        print(employee.company.name)

    company_01 = SaCompany(
        name = 'SA Firma 01',
        vat_id = '123',
        street_and_number = 'Ulica 01',
        postal_code = '12345',
        city = 'Grad 01',
        country = 'Drzava 01',
        email = 'firma01@firma01.com',
        phone = '123456'
    )
    company_02 = SaCompany(
        name = 'SA Firma 02',
        vat_id = '456',
        street_and_number = 'Ulica 02',
        postal_code = '12345',
        city = 'Grad 02',
        country = 'Drzava 02',
        email = 'firma02@firma02.com',
        phone = '654321'
    )

    employee_01 = SaEmployee(
        first_name = 'Pero',
        last_name = 'Peric',
        email = 'pero.peric@firma01.com',
        phone = '123456',
        company = company_01
    )
    employee_02 = SaEmployee(
        first_name = 'Ana',
        last_name = 'Anic',
        email = 'ana.anic@firma01.com',
        phone = '123456',
        company = company_01
    )
    employee_03 = SaEmployee(
        first_name = 'Marko',
        last_name = 'Maric',
        email = 'pero.peric@firma02.com',
        phone = '654321',
        company = company_02
    )

    session.add_all([company_01, company_02, employee_01, employee_02, employee_03])
    session.commit()

    for employee in company_01.employees:
        print(employee.first_name)

    print(f'Naziv: {employee_02.company.name} OIB: {employee_02.company.vat_id}')


if __name__ == '__main__':
    main()