import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'admin1990',
    port = '3307',

)


cursorObject = dataBase.cursor()


cursorObject.execute('CREATE DATABASE crm')

print("All Done!")