import psycopg2

conn = psycopg2.connect("postgres://decor_manager:testing@localhost:5432/wallartdecor")
cur = conn.cursor()

while True:
    print("Please enter Username")
    Username = str(input())
    query = "SELECT * FROM transactions WHERE Username = %s"
    cur.execute(query)
    result = cur.fetchall()
    conn.commit()

cur.close()
conn.close()
