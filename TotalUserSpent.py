
import psycopg2

conn = psycopg2.connect("postgres://decor_manager:testing@localhost:5432/wallartdecor")
cur = conn.cursor()

while True:
  print("Please enter Username")
  username = str(input())
 
 
  cur.execute("SELECT SUM(Price) FROM TRANSACTIONS WHERE Username = '%s'");
  TotalPrice = cur.fetchall()
  print(username, " has spent a total of: $", TotalPrice)
  conn.commit()
  
cur.close()
conn.close()
