import sqlite3
from py_bank_config import DB_PATH
def insert_in_table():
    
    db_path = DB_PATH
    insert_in_table_sql_query = """
INSERT INTO companies (name, vat_id, street_and_number, postal_code, city, country, contact_person)
VALUES(?, ?, ?, ?, ?, ?, ?);
 """
    name = input('Upisite ime firme: ')
    vat_id = input('Upisite OiB: ')
    street_and_number = input('Upisite ulicu i broj:')
    postal_code = input('Upisite postanski broj:')
    city = input('Upisite grad firme:')
    country = input('Upisite ime drzave: ')
    contact_person = input('Upisite ime osobe za kontakt:')

    sql_params = (name, vat_id, street_and_number, postal_code, city, country, contact_person)
    try:
        db_connection = sqlite3.connect(db_path)
        cursor = db_connection.cursor()
    
        cursor.execute(insert_in_table_sql_query, sql_params)
        db_connection.commit()
        
        cursor.close()
    except sqlite3.Error as error:
        print (f'Dogodila se greska u vezi baze : {error}')
    except Exception as ex:
        print(f'Dogodila se greska: {ex}')
    finally:
    #Finalni korak zatvaranje konekcije prema bazi
        if db_connection:
            db_connection.close()
            
if __name__ == '__main__':
    insert_in_table()