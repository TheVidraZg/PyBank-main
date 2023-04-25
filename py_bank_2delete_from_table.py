import sqlite3

from py_bank_config import DB_PATH



def delete_table():
    db_path = DB_PATH

    delete_table_sql_query = '''
        DELETE FROM companies
        WHERE id = ?
    '''

    company_id = int(input('Upisite ID firme koju zelite izbrisati: '))


    try:
        db_connection = sqlite3.connect(db_path)
        cursor = db_connection.cursor()

        cursor.execute(delete_table_sql_query,(company_id,))
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
    delete_table()
