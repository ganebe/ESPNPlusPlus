import mysql.connector

db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_root_password",
        #uncomment the next line of code after you have created your own database
        #  database="nba_database",
)

mycursor = db.cursor()
#delete the following line of code when you have created your database
mycursor.execute("CREATE DATABASE nba_database")