# SCRIPT TO CREATE MYSQL TABLE



# Import Modules
import mysql.connector
import os

os.chdir('/home/ccirelli2/Desktop/Programming/Passwords')
print(os.listdir())

import mysql_login_info 




'''


def get_mysql_login(data, mysql_login_info):   
    if data == 'password':
        return mysql_login_info.password
    elif data == 'user':
        return mysql_login_info.user

# Create Connection to MySQL
mydb = mysql.connector.connect(
        host='localhost', 
        user='ccirelli2', 
        passwd= get_mysql_login('password'),
        database= get_mysql_login('user')
        )



# Create mycursor
mycursor = mydb.cursor()

'''





