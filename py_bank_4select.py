import sqlite3
from py_bank_config import DB_PATH
def select_from_table():
    db_path = DB_PATH
#     select_from_table_sql_query = """
# SELECT name, vat_id, city, contact_person FROM companies
#  """
    select_from_table_sql_query = """
SELECT * FROM companies
WHERE id= ?
 """
    company_id = int(input('Upisite ID firme koju zelite dohvatiti: '))
    try:
        db_connection = sqlite3.connect(db_path)
        cursor = db_connection.cursor()
    
        cursor.execute(select_from_table_sql_query, (company_id,))
        companies = cursor.fetchall()
        if len(companies) < 1 :
            print('Ne postoji taj podatak u bazi!')
        else:
            for company in companies:
                print(company)
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
    select_from_table()