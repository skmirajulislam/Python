import mysql.connector as mysql

mydb=mysql.connect(host="localhost",user="root",password="Root_password")
print(mydb,"connection Established...")

db=mydb.cursor()

#database creating
db.execute("create database miraj")
print("database created")
