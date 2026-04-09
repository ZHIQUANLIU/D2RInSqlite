import sqlite3
import csv

with open('D2R-Excel/levelgroups.txt', 'r', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter='\t')
    headers = next(reader)
    rows = list(reader)

conn = sqlite3.connect('D2RDB/d2r.db')
cursor = conn.cursor()

cursor.execute('DROP TABLE IF EXISTS levelgroups')

col_defs = ','.join([f'"{h}" TEXT' for h in headers])
cursor.execute(f'CREATE TABLE levelgroups ({col_defs})')

for row in rows:
    cursor.execute('INSERT INTO levelgroups VALUES (' + ','.join(['?']*len(headers)) + ')', row)

conn.commit()
conn.close()
print('levelgroups table imported')