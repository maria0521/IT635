import psycopg2

conn = psycopg2.connect("postgres://decor_manager:testing@localhost:5432/wallartdecor")
cur = conn.cursor()

print("Please enter Username")
Username = str(input())
cur.execute("SELECT * FROM transactions WHERE Username = '%s'");
result = cur.fetchall()
for row in result:
    print(row[0])
conn.commit()

cur.close()
conn.close()
