import sqlite3
import csv

with open('D2R-Excel/inventory.txt', 'r', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter='\t')
    headers = next(reader)
    rows = list(reader)

conn = sqlite3.connect('D2RDB/d2r.db')
cursor = conn.cursor()

cursor.execute('DROP TABLE IF EXISTS inventory')

col_defs = ','.join([f'"{h}" TEXT' for h in headers])
cursor.execute(f'CREATE TABLE inventory ({col_defs})')

for row in rows:
    cursor.execute('INSERT INTO inventory VALUES (' + ','.join(['?']*len(headers)) + ')', row)

conn.commit()
conn.close()
print('inventory table imported')