import mysql.connector as mysql

mydb=mysql.connect(host="localhost",user="root",password="Root_password",database="database_name")
print(mydb,"connection Established...")

db=mydb.cursor()

#table creating
db.execute("create table employe(id int,name varchar(20))")
print("table creted")
