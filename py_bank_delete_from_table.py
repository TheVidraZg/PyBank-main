import sqlite3
from py_bank_config import DB_PATH

db_path = DB_PATH

def delete_from_table():
    create_backup_table_sql_query = """
        CREATE TABLE companies_backup(
	    id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT
        ); """

    insert_in_backup_table_sql_query = """
        INSERT INTO companies_backup
        SELECT name, vat_id, city
        FROM companies ;

         """

    try:
        db_connection = sqlite3.connect(db_path)
        cursor = db_connection.cursor()

        cursor.execute(create_backup_table_sql_query)
        previev = cursor.fetchall()
        print(previev)
        cursor.execute(insert_in_backup_table_sql_query)
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
    delete_from_table()