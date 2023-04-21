import sqlite3
from sqlite3 import Error
from datetime import datetime as dt

from features import (Company,Currency,
                      BankAccount)


#region Kreiranje bankovnog racuna
account_number = f'BA-{dt.now().year}-{dt.now().month}-{"42".zfill(5)}'
account_owner = Company(1,
                        'Firma d.o.o',
                        '12345678987',
                        'Ulica i broj',
                        '10290',
                        'Zapresic',
                        'Hrvatska',
                        'Pero Peric')
currency = Currency(1, 'EUR', 'EURO')
bank_account = BankAccount(1,
                           account_number,
                           account_owner,
                           currency,
                           10_999.99)

print(bank_account)
print(bank_account.currency)

for transaction in bank_account.transactions:
    print(transaction)


opening_amount = bank_account.transactions[0].amount
print(opening_amount)
#endregion




try:
    # 1. Korak otvori konekciju prema bazi
    db_connection = sqlite3.connect('db_data/dbsql.db')
    # 2. korak kreiranje kursora za kretanje po bazi podataka
    cursor = db_connection.cursor()
    
    # 3. korak pokreni sql upit
    cursor.execute('SELECT sqlite_version() ')
    # 3.1. korak ako je upit za dohvat podataka (read_) onda pozovemo fetchall()
    record_set = cursor.fetchall()
    print(record_set)
    # 3.2  korak ako je upit za promjenu podataka (insert update i delete)
    #db_connection.commit()
    #4. korak zatvorimo cursor 
    cursor.close()
except sqlite3.Error as error:
        print (f'Dogodila se greska u vezi baze : {error}')
except Exception as ex:
    print(f'Dogodila se greska: {ex}')
finally:
    #Finalni korak zatvaranje konekcije prema bazi
    if db_connection:
        db_connection.close()