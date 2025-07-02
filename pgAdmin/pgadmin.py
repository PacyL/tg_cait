import psycopg2

conn = psycopg2.connect(
    dbname="Rus1",
    user="postgres",
    password="Rus371m",
    host="localhost",
    port="4999"
)

cursor = conn.cursor()
cursor.execute("SELECT * FROM item")
a = cursor.fetchall()
print(a)

conn.commit()
cursor.close()
conn.close()