import sqlite3
import csv

with open('D2R-Excel/monlvl.txt', 'r', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter='\t')
    headers = next(reader)
    rows = list(reader)

conn = sqlite3.connect('D2RDB/d2r.db')
cursor = conn.cursor()

cursor.execute('DROP TABLE IF EXISTS monlvl')

col_defs = ','.join([f'"{h}" TEXT' for h in headers])
cursor.execute(f'CREATE TABLE monlvl ({col_defs})')

for row in rows:
    cursor.execute('INSERT INTO monlvl VALUES (' + ','.join(['?']*len(headers)) + ')', row)

conn.commit()
conn.close()
print('monlvl table imported')