

# INSERT FUNCTION

def insert_function_basic_transcript_info_table(mydb, url, pub_date, ticker, title, text):
    mycursor = mydb.cursor()

    sql_command = '''
                  INSERT INTO BASIC_TRANSCRIPT_INFO
                  (URL, PUBLICATION_DATE, TICKER, TITLE, TEXT)
                  VALUES
                  ('{}', '{}', '{}', {}, {})
                  '''.format(url, pub_date, ticker, title, text)
    
    mycursor.execute(sql_command)
    mydb.commit()

    return None



