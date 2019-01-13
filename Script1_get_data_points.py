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


### IMPORT MODULES
import Module1_get_data_points as m1


# URL OBJECTS
url_root_transcript_index = 'https://seekingalpha.com/earnings/earnings-call-transcripts/'
url_root_seeking_alpha = 'https://seekingalpha.com'


# PAGE OBJECTS
beg_transcript_page = 5268





# FUNCTION TO GET TRANSCRIPT LINKS FROM TRANSCRIPT PAGE

def scraper_driver_function(url_root_transcript_index_page, transcript_index_page_num, 
        url_root_seeking_alpha):
    '''
    INPUTS:
        url_root_transcript_index:  root page for index_page containing links to indv transcript
                                    pages. 
        url_root_seeking_alpha:     root page for seeking alpha itself to which each article page
                                    to get a complete article url. 
        transcript_index_page_num:  the first index_page to start iteration. 

    '''



    # Generate Loop over range of pages containing transcript links
    for num in range(0, transcript_index_page_num):
        
        # Create page number object (count down)
        page_number = transcript_index_page_num - num

        # Create bsObj for each page containing list of transcript pages
        bsObj = m1.get_bsObj(url_root_transcript_index_page + str(page_number))
        
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
            transcript_page = url_root_seeking_alpha + link

            # Create a bsObj of the transcript page
            bsObj_transcript_page = m1.bsObj(transcript_page)

            # Scrape Attributes
            publication_date = m1.get_date_published(bsObj_transcript_page)
            ticker = m1.get_ticker(bsObj_transcript_page) 
            title = m1.get_title(bsObj_transcript_page)        
            text = m1.get_ecall_text(bsObj_transcript_page)



            # Insert Into MySQL Table












































