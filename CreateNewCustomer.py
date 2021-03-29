import psycopg2

conn = psycopg2.connect("postgres://decor_manager:testing@localhost:5432/wallartdecor")
cur = conn.cursor()

while True:
  print("Please enter Username")
  username = str(input())
  print("Please enter Password")
  passw = str(input())
  print("Please enter CardName")
  cname = str(input())
  print("Please enter Billing Address")
  billadd = str(input())
  print("Please enter Mailing Address")
  mailadd = str(input())
  print("Please enter City")
  city = str(input())
  print("Please enter State")
  state = str(input())
  print("Please enter Zipcode")
  zipcode = int(input())
 
  cur.execute("""
    INSERT INTO CUSTOMER (Username, Password, CName, BillingAddress, Str1, City, State, Zip)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
  """, (username, passw, cname, billadd, mailadd, city, state, zipcode));
  conn.commit()
  print("record inserted")
cur.close()
conn.close()
