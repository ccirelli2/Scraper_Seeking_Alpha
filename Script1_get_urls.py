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
from time import sleep 


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
page_start_num = 5268 



# TARGET DIRECTORY OBJECTS
target_dir_transcripts = '/home/ccirelli2/Desktop/Programming/Scraper_Seeking_Alpha/output_transcripts'


# SCRAPER DRIVER FUNCTION-------------------------------------------------------------------------

def scraper_driver_function(run_type, url_root_transcript, page_start_num, 
                            url_root_article):
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
        m3.clear_url_table(mydb)
    
    elif run_type == 'start_from_last_page':
        pass
        

    # CREATE COUNT OBJECT FOR PROGRESS RECORDING---------------------------------------
    Count = 0


    # Generate Loop over range of pages containing transcript links
    for num in range(0, page_start_num):
        
        # Progress Report
        Count +=1
        m4.progress_recorder(Count, page_start_num)

        # Create page number object (count down)
        '''On the first iteration this would be 5268 - 1'''
        page_number = page_start_num - num
        
        # Create bsObj for each page containing list of transcript pages
        bsObj = m1.get_bsObj(url_root_transcript + str(page_number))
        
        # Find All 'h3' Tags that contain links to transcript pages
        h3_tags = bsObj.findAll('h3')
        
        # Iterate over h3_tag and insert into table
        for tag in h3_tags:
            url = str(url_root_article + tag.a['href']) 
            m3.insert_url(mydb, url, page_number)

        # Add Sleep Delay of 5 Seconds   
        sleep(10)


    # Return None



#-------------------------------------------------------------------------------------
'''
scraper_driver_function('restart', 
                        url_root_transcript_index, 
                        page_start_num,
                        url_root_seeking_alpha
                        )


'''

import csv
total_url_count = 158040
count_transcript_function = 0

def get_transcripts(count_transcript_function, total_url_count):
    # Open CSV File
    with open('Seeking_Alpha_URLs.csv', 'r') as csvfile:
        
        # Read CSV File
        csv_reader = csv.reader(csvfile, delimiter=',')
        
        # Iterate Each Row
        for row in csv_reader:
            
            if row[0] != 'URL':
                
                # Progress Report
                m4.progress_recorder(count_transcript_function, total_url_count)
                count_transcript_function += 1
            
                # Obtain String of Url
                url = row[0]
                print(url)
                # Generate bs4 object 
                request = Request(url, headers={'User-Agent': '''Mozilla/5.0 (Windows NT 6.1) 
                AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'''})
                print('request created')
                html = urlopen(request)
                print('html created')
                bsObj = BeautifulSoup(html.read(), 'lxml')
                print('bs4 object created') 
                # Generate Values & Insert them into our DB
                publication_date = m1.get_date_published(bsObj)
                ticker = m1.get_ticker(bsObj)
                title = m1.get_title(bsObj)
                dirty_text = m1.get_ecall_text(bsObj, 'dirty')
                clean_text = m1.get_ecall_text(bsObj, 'clean')
   
                # Create Text File of Transcript with Tags
                create_e_call_text = m4.create_txt_file(
                    target_dir ='''
                    /home/ccirelli2/Desktop/Programming/Scraper_Seeking_Alpha/output_transcripts''',
                    file_name =                url,
                    text =                     str(dirty_text)
                                                )
                sleep(10)


get_transcripts(count_transcript_function, total_url_count)




