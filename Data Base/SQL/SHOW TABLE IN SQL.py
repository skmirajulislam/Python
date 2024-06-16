import mysql.connector as mysql

mydb=mysql.connect(host="localhost",user="root",password="Root_password",database="database_name")
print(mydb,"connection Established...")

db=mydb.cursor()

db.execute("show tables")
for x in db:
    print(x)