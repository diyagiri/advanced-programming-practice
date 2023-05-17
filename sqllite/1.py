import sqlite3
conn=sqlite3.connect('employee.db')

c=conn.cursor()

c.execute("INSERT INTO employees VALUES ('Corey','Schafer',5000)")

conn.commit()

conn.close()