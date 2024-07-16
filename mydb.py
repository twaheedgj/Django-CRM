import mysql.connector


dataBase=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Next.crm1",
    port="3307"
)

cursor=dataBase.cursor()

cursor.execute("CREATE DATABASE DCRM")

print('All Done')
   