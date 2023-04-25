import sqlite3

from py_bank_config import DB_PATH



def update_table():
    db_path = DB_PATH

    update_table_sql_query = '''
        UPDATE companies
        SET name = ?,
            vat_id = ?,
            street_and_number = ?,
            postal_code = ?,
            city = ?,
            country = ?,
            contact_person = ?
        WHERE id = ?
    '''

    company_id = int(input('Upisite ID firme koju zelite dohvatiti: '))

    #Poziv funkcije za dohvat podataka iz baze na osnovu upisanog ID broja
    # Unos dobivenih podatka u varijable
    # prolazak kroz svaku varijablu i nuditi korisniku azuriranje
    # Tek nakon toga ide SQL update u bazu
    
    name = input('Upisite naziv firme: ')
    vat_id = input('Upisite OIB firme: ')
    street_and_number = input('Upisite ulicu i broj firme: ')
    postal_code = input('Upisite postanski broj firme: ')
    city = input('Upisite grad firme: ')
    country = input('Upisite drzavu firme: ')
    contact_person = input('Upisite ime i prezime kontakt osobe firme: ')

    sql_params = (name, vat_id,
                  street_and_number,
                  postal_code,
                  city,
                  country,
                  contact_person,
                  company_id)


    try:
        db_connection = sqlite3.connect(db_path)
        cursor = db_connection.cursor()

        cursor.execute(update_table_sql_query, sql_params)
        db_connection.commit()

        cursor.close()

    except sqlite3.Error as error:
        print(f'Dogodila se greska u vezi baze: {error}')
    except Exception as ex:
        print(f'Dogodila se greska: {ex}')

    finally:
        if db_connection:
            db_connection.close()


if __name__ == '__main__':
    update_table()
