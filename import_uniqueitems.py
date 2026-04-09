import sqlite3
import csv

with open('D2R-Excel/uniqueitems.txt', 'r', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter='\t')
    headers = next(reader)
    rows = list(reader)

conn = sqlite3.connect('D2RDB/d2r.db')
cursor = conn.cursor()

cursor.execute('DROP TABLE IF EXISTS uniqueitems')

col_defs = ','.join([f'"{h}" TEXT' for h in headers])
cursor.execute(f'CREATE TABLE uniqueitems ({col_defs})')

for row in rows:
    cursor.execute('INSERT INTO uniqueitems VALUES (' + ','.join(['?']*len(headers)) + ')', row)

conn.commit()
conn.close()
print('uniqueitems table imported')