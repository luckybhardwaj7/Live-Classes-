import mysql.connector 
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
mycursor = mydb.cursor()
mycursor.execute("insert into test2.test_table values( 123 , 'Lucky' , 123.0 , 'Bhardwaj')")
mydb.commit() #to insert the data into the table 
mydb.close()