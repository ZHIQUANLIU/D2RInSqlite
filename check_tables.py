import sqlite3
conn = sqlite3.connect('D2RDB/d2r.db')
cursor = conn.cursor()
cursor.execute('SELECT name FROM sqlite_master WHERE type="table"')
tables = cursor.fetchall()
print(f'Total tables: {len(tables)}')
for t in sorted(tables):
    print(t[0])