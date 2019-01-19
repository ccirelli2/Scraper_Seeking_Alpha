### SCRIPT TO CREATE MYSQL TABLE


# IMPORT MODULESmport Modules
import mysql.connector
import os
import sys

'''NOTE:  CREATE TABLES FOR LOGGING DATA'''




# APPEND PATH & IMPORT MYSQL LOGIN INFO
# print(sys.path, '\n')
sys.path.append('/home/ccirelli2/Desktop/Programming/Passwords')
import mysql_login_info

 
# CREATE CONNECTION TO MYSQL
mydb = mysql.connector.connect(
        host    ='localhost', 
        user    = mysql_login_info.user, 
        passwd  = mysql_login_info.password,
        database= 'SEEKING_ALPHA_SCRAPER'
        )


# CREATE CURSOR
mycursor = mydb.cursor()


# CREATE TABLE

def create_table(mydb, mycursor):

    sql_command = '''
                    CREATE TABLE BASIC_TRANSCRIPT_INFO (

                    URL                 VARCHAR(1000) NOT NULL    
                    PUBLICATION_DATE    DATE
                    TICKER              VARCHAR(255)
                    TITLE               VARCHAR(1000)
                    TEXT                LONGTEXT

                    PRIMARY KEY (URL)

                    )'''
    mycursor.execute(sql_command)
    mydb.commit()

    return None





def create_table_links(mydb, mycursor):
    sql_command = '''

    CREATE TABLE URL_LINKS (

    URL VARCHAR(1000) NOT NULL
    PRIMARY KEY (URL)

    )'''

    mycursor.execute(sql_command)

    return None












