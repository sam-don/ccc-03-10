import psycopg2
import os

connection = psycopg2.connect(
    database="library_api",
    user="postgres",
    password="aTXy87PdpjiR9eNciaFZ",
    host="54.91.110.61",
    port="5432"
)

cursor = connection.cursor()

cursor.execute("create table if not exists books (id serial PRIMARY KEY, title varchar);")
connection.commit()
