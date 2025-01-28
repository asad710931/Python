import sqlite3
import datetime


date = datetime.datetime.now()
print(date)

db_conn=sqlite3.connect('mydata.db')
print("Database Created")


def printDB():
    try:
        result=db_conn.execute("SELECT id,name,age,address,height,date FROM users")
        for row in result:
            print(f'ID : {row[0]}\nNAME : {row[1]}\nDate : {row[5]}')
    except sqlite3.OperationalError:
        print('Failed to view data')

def deleteRow():
    try:
        db_conn.execute("DELETE FROM users WHERE Id=3")
        db_conn.commit()
        print('row deleted')
        
    except sqlite3.OperationalError:
        print('row Not deleted')



def create_table():
    try:
        db_conn.execute("CREATE TABLE users (Id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,name TEXT NOT NULL,age INT NOT NULL,address TEXT,height REAL NOT NULL,date TEXT);")
        db_conn.commit()
        print('Table Created')
    except sqlite3.OperationalError:
        print('Table Not Created')

data_list=[('Asad',25,'CTG-BD',5.10,date),('Sabed',14,'DK-BD',5.11,date),('Shireen',24,'CO-BD',5.23,date)]


def insertData():
    try:
        db_conn.execute("INSERT INTO users (name,age,address,height,date) VALUES(data_list);")
        db_conn.commit()
        print("Data inserted")
    except sqlite3.OperationalError:
        print("data inserting failed")

#create_table()
insertData()
#deleteRow()
printDB()

db_conn.close()