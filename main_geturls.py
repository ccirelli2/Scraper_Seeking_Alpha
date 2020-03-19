# SEEKING ALPH SCRAPER - SCRAPE EARNINGS CALLS
'''
header      Test which user agent that is being recognized when you make a url request
            url = 'https://httpbin.org/user-agent'
'''


### IMPORT LIBRARIES
from bs4 import BeautifulSoup
import requests
import urllib
import os
from datetime import datetime
import re
import sys
import mysql.connector
from time import sleep 
import pandas as pd

### EXTEND PATH NAME
sys.path.append('/home/ccirelli2/Desktop/Passwords')

### IMPORT MODULES
import Module1_get_data_points as m1
import Module3_sql_insert_statement as m3
import Module4_utility_functions as m4
import passwords as ps


# APPEND PATH & IMPORT MYSQL LOGIN INFO
# print(sys.path, '\n')
#sys.path.append('/home/ccirelli2/Desktop/Programming/Passwords')
#import mysql_login_info

# CREATE CONNECTION TO MYSQL
mydb = mysql.connector.connect(
        host    ='localhost',
        user    = ps.get_mysql_user_info('user_name'),
        passwd  = ps.get_mysql_user_info('password'),
        database= 'SEEKING_ALPHA_SCRAPER'
        )

# CREATE CURSOR
mycursor = mydb.cursor()

# URL OBJECTS
url_root_transcript_index = 'https://seekingalpha.com/earnings/earnings-call-transcripts/'
url_root_seeking_alpha = 'https://seekingalpha.com'

# PAGE OBJECTS
page_start_num = 5268 

# TARGET DIRECTORY OBJECTS
target_dir_transcripts = '/home/ccirelli2/Desktop/Programming/Scraper_Seeking_Alpha/output_transcripts'
transcript_data_file = 'Seeking_Alpha_URLs.csv'




# SCRAPER DRIVER FUNCTION-------------------------------------------------------------------------

def scraper_driver_function(run_type, url_root_transcript, page_start_num, 
                            url_root_article, target_dir_transcripts, transcript_data_file):
    '''
    INPUTS--------------------------------------------------------------------------------
    run_type:                   'restart' = clear table; 'start_from_last_page' = start from 
                                last page scraped
    url_root_transcript:        Root part of url that contains the list of transcript links
                                We add a number to each of these pages to move through the
                                web page and collect all of the links.        
    url_root_seeking_alpha:     Root page for seeking alpha itself to which each article page
                                to get a complete article url. 
    page_start_num:             The transcript index pages run from 1 to 5268, the latter 
                                being the page with the oldest trasnscripts.
                                Therefore, we start the scraper at 5268 and subtract 1 
                                from it on each iteration. 
                                 
    '''

    # SELECT RUN TYPE------------------------------------------------------------------
    '''Note we need to capture the count object in our db'''
    if run_type == 'restart':
        m3.clear_transcript_table(mydb)
    
    elif run_type == 'start_from_last_page':
        pass
        

    # CREATE COUNT OBJECT FOR PROGRESS RECORDING---------------------------------------
    Count = 0

    
    transcript_data_file = 'Seeking_Alpha_URLs.csv'
    df = pd.read_csv(transcript_data_file)

    for url in df.iloc[:,0]:

        content = Request(url, headers={
                                        'authority': 'seekingalpha.com',
                                        'method': 'GET',
                                        'path': '/earnings/earnings-call-transcripts',
                                        'scheme': 'https',
                                        '''user-agent': 
                                        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) 
                                        AppleWebKit/537.36 (KHTML, like Gecko) 
                                        Chrome/61.0.3163.100 Safari/537.36'''})
        html = urlopen(content)
        bsObj = BeautifulSoup(html.read(), 'lxml')

        # Generate Values from bsObj
        publication_date = m1.get_date_published(bsObj)
        ticker = m1.get_ticker(bsObj)
        title = m1.get_title(bsObj)
        dirty_text = m1.get_ecall_text(bsObj, 'dirty')
        clean_text = m1.get_ecall_text(bsObj, 'clean')

        # Insert Values Into DB
        m3.insert_function_2(mydb, url, publication_date, ticker, title, clean_text)

        # Create Files
        m4.create_txt_file(target_dir_transcripts, url.split('article/')[1], clean_text)
        m4.progress_recorder(Count, 150000)
        Count += 1
        sleep(10)







#-------------------------------------------------------------------------------------
                                               

'''
import requests
from bs4 import BeautifulSoup
target_dir_transcripts='/home/ccirelli2/Desktop/Repositories/Scraper_Seeking_Alpha/output_transcripts'
target_file = 'Seeking_Alpha_URLs.csv'
df = pd.read_csv(target_file)
Count = 0
m3.clear_transcript_table(mydb)

for url in df.iloc[:,0]:

    content = Request(url, headers={
	'authority': 'seekingalpha.com',
	'method': 'GET',
	'path': '/earnings/earnings-call-transcripts',
	'scheme': 'https',
	'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
})
    html = urlopen(content)
    bsObj = BeautifulSoup(html.read(), 'lxml')

    # Generate Values from bsObj
    publication_date = m1.get_date_published(bsObj)
    ticker = m1.get_ticker(bsObj)
    title = m1.get_title(bsObj)
    dirty_text = m1.get_ecall_text(bsObj, 'dirty')
    clean_text = m1.get_ecall_text(bsObj, 'clean')

    # Insert Values Into DB
    m3.insert_function_2(mydb, url, publication_date, ticker, title, clean_text)
    
    # Create Files
    m4.create_txt_file(target_dir_transcripts, url.split('article/')[1], clean_text)
    m4.progress_recorder(Count, 150000)
    Count += 1
    sleep(10)


'''











