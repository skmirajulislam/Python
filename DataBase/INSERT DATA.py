import mysql.connector as mysql

mydb=mysql.connect(host="localhost",user="root",password="Root_password",database="database_name")
print(mydb,"connection Established...")

db=mydb.cursor()

db_insert="insert into employe(id,name) values(%s,%s)"
db_list=[(6,"abhranil"),(7,"debjit"),(8,"rupam"),(30,"arnab")]

db.executemany(db_insert,db_list)
mydb.commit()


print("record inserted")
