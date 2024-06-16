import mysql.connector as mysql

mydb=mysql.connect(host="localhost",user="root",password="Root_password",database="database_name")
print(mydb,"connection Established...")
db=mydb.cursor()

db.execute("select * from miraj.employe")
db_show=db.fetchall()

for x in db_show:
    print (x)