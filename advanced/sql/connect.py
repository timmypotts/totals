import psycopg2

# db = sqlalchemy.create_engine('postgresql://postgres:a0E24me@localhost:5432/mlb')

conn = psycopg2.connect(dbname="mlb", user="postgres", password="a0E24me", host="localhost")

cur = conn.cursor()

cur.execute("SELECT * FROM field")

records = cur.fetchall()

print(records)