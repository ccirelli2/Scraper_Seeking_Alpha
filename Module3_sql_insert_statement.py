# NOTE: CREATE INSERT STATEMENTS FOR THE LOGGING DATA





# INSERT FUNCTION

def insert_function_basic_transcript_info_table(mydb, url, pub_date, ticker, title, text):

    mycursor = mydb.cursor()

    sql_command = '''INSERT INTO BASIC_TRANSCRIPT_INFO 
                     (URL, PUBLICATION_DATE, TICKER, TITLE, TEXT)
                     VALUES ('{}', '{}', '{}', '{}', '{}')
                     '''.format(url, pub_date, ticker, title, text)
    
    
    mycursor.execute(sql_command)
    mydb.commit()

    return None



def insert_function_2(mydb, url, pub_date, ticker, title, text):

    mycursor = mydb.cursor()

    sql_command = '''INSERT INTO BASIC_TRANSCRIPT_INFO 
                     (URL, PUBLICATION_DATE, TICKER, TITLE, TEXT)
                     VALUES (%s, %s, %s, %s, %s)'''

    mycursor.execute(sql_command, (url, pub_date, ticker, title, text))
    mydb.commit()

    return None




def clear_transcript_table(mydb):
    mycursor = mydb.cursor()

    sql_command = '''
                  DELETE FROM BASIC_TRANSCRIPT_INFO
                  WHERE URL != ''
                  '''

    mycursor.execute(sql_command)
    mydb.commit()

    return None


def insert_url(mydb, url):
    mycursor = mydb.cursor()
    sql_command = '''INSERT INTO URL_LINKS
                     (URL)
                     VALUE ('{}')'''.format(url)
    mycursor.execute(sql_command)
    mydb.commit()


def clear_url_table(mydb):
    mycursor = mydb.cursor()

    sql_command = '''
                  DELETE FROM URL_LINKS
                  WHERE URL != ''
                  '''
    mycursor.execute(sql_command)
    mydb.commit()



