import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database="sflow",
  password=""
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM messages")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)