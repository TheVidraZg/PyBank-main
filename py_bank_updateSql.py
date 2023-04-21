import sqlite3
from py_bank_config import DB_PATH
def update_table():
    db_path = DB_PATH
#     select_from_table_sql_query = """
# SELECT name, vat_id, city, contact_person FROM companies
#  """
    update_table_sql_query = """
UPDATE companies
SET vat_id = 4422688859631
WHERE id= 2
 """
    try:
        db_connection = sqlite3.connect(db_path)
        cursor = db_connection.cursor()
    
        cursor.execute(update_table_sql_query)
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
    update_table()