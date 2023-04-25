import sqlite3
from py_bank_config import DB_PATH
def create_company_table():
    
    db_path = DB_PATH
    crate_table_sql_query = """
    CREATE TABLE IF NOT EXISTS companies(
	id INTEGER PRIMARY KEY,
	name TEXT NOT NULL,
	vat_id TEXT NOT NULL,
	street_and_number Text NULL,
	postal_code TEXT NULL,
	city TEXT NOT NULL,
	country TEXT not null,
	contact_person TEXT not NULL
	);
 """


    try:
        db_connection = sqlite3.connect(db_path)
        cursor = db_connection.cursor()
    
        cursor.execute(crate_table_sql_query)
        record_set = cursor.fetchall()
        print(record_set)
        #db_connection.commit()
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
    create_company_table()