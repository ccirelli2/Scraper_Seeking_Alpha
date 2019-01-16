# SEEKING ALPH SCRAPER - SCRAPE EARNINGS CALLS
'''
header      Test which user agent that is being recognized when you make a url request
            url = 'https://httpbin.org/user-agent'
'''


### IMPORT LIBRARIES
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.request import Request
import urllib
import os
from datetime import datetime
import re
import sys
import mysql.connector

### IMPORT MODULES
import Module1_get_data_points as m1
import Module3_sql_insert_statement as m3
import Module4_utility_functions as m4

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

# URL OBJECTS
url_root_transcript_index = 'https://seekingalpha.com/earnings/earnings-call-transcripts/'
url_root_seeking_alpha = 'https://seekingalpha.com'

# PAGE OBJECTS
beg_transcript_page = 5268
test_beg_transcript_page = 2

# TARGET DIRECTORY OBJECTS
target_dir_transcripts = '/home/ccirelli2/Desktop/Programming/Scraper_Seeking_Alpha/output_transcripts'


# SCRAPER DRIVER FUNCTION-------------------------------------------------------------------------

def scraper_driver_function(run_type, url_root_transcript, page_start_num, 
                            url_root_article):
    '''
    INPUTS:
        run_type:                   either 'restart' or 'start_from_last_page'
        url_root_transcript_index:  root page for index_page containing links to indv transcript
                                    pages. 
        url_root_seeking_alpha:     root page for seeking alpha itself to which each article page
                                    to get a complete article url. 
        transcript_index_page_num:  the first index_page to start iteration. 

    '''

    if run_type == 'restart':
        m3.clear_table(mydb)
    elif run_type == 'start_from_last_page':
        pass
        # We need to capture the page number in our db

    Count = 0

    # Generate Loop over range of pages containing transcript links
    for num in range(0, page_start_num):
        
        # Progress Report
        Count +=1
        m4.progress_recorder(Count, page_start_num)

        # Create page number object (count down)
        page_number = page_start_num - num

        # Create bsObj for each page containing list of transcript pages
        bsObj = m1.get_bsObj(url_root_transcript + str(page_number))
        
        # Find All 'h3' Tags that contain links to transcript pages
        h3_tags = bsObj.findAll('h3')
        
        # Iterate h3 tags to get links
        '''
        format of return 
        value = /article/2159-sohu-managements-prepared-remarks-from-q1-2005-conference-call
        '''
        for tag in h3_tags:
            link = tag.a['href']
        
            # Single Transcript Page
            transcript_page = url_root_article + link

            # Create a bsObj of the transcript page
            bsObj_transcript_page = m1.get_bsObj(transcript_page)

            # Scrape Attributes
            page_url = transcript_page
            publication_date = m1.get_date_published(bsObj_transcript_page)
            ticker = m1.get_ticker(bsObj_transcript_page) 
            title = m1.get_title(bsObj_transcript_page)        
            dirty_text = m1.get_ecall_text(bsObj_transcript_page, 'dirty')
            clean_text = m1.get_ecall_text(bsObj_transcript_page, 'clean')

            # Write Transcript to File

            create_e_call_text = m4.create_txt_file(

            # Insert Into MySQL Table
            m3.insert_function_2(
                    mydb        = mydb, 
                    url         = page_url, 
                    pub_date    = publication_date, 
                    ticker      = ticker, 
                    title       = title,
                    text        = clean_text)
            print('Page Scraped => {}'.format(tag))             




#-------------------------------------------------------------------------------------

scraper_driver_function('restart', 
                        url_root_transcript_index, 
                        beg_transcript_page,
                        url_root_seeking_alpha
                        )

























