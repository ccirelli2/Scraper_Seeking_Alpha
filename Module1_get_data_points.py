### IMPORT LIBRARIES
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.request import Request
import os
import re
import string


# FUNCTIONS GET VALUES FROM WEB PAGE

'''headers ={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.149 Safari/537.36'}


'''



def get_bsObj(url):
    # Create bs4 Object
    request = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    html    = urlopen(request)
    bsObj   = BeautifulSoup(html.read(), 'lxml')
    return bsObj

def get_date_published(bsObj):
    # Get date puslished
    '''Returns a string like: 2019-01-09 21:09:07 -0500'''
    date_time_stamp = bsObj.article.header.time['datetime']
    # Utilize Regex To Obtain Only the Date
    format_target = '2019-01-09'
    regex = re.compile('[0-9]+-[0-9]+-[0-9]+')
    try:
        search = re.search(regex, date_time_stamp)
        result = search.group()
        return result
    except AttributeError:
        return None

def get_title(bsObj):
    title = bsObj.h1.text
    return title


def get_clean_text(dirty_text):
    punct = string.punctuation + "’" + "'" + "-" 
    clean_text = ('').join(list(filter(lambda x: (x not in punct), dirty_text)))   
    return clean_text

def insert_backslash_comments(dirty_text):
    # code should backslash all quotes in our insert text
    backslash_single_quotes = dirty_text.replace("'", "\\'")
    backslash_double_quotes = backslash_single_quotes.replace("\"", "\\\"") 
    return backslash_double_quotes


def get_ecall_text(bsObj, type):
    '''type:  dirty or clean'''
    # Get article body
    search = bsObj.findAll('div', {'itemprop':'articleBody'})
    body   = search[0]
    
    if type == 'dirty':
        return body.text

    else:
        dirty_text = body.text
        clean_text = insert_backslash_comments(dirty_text) 
        return clean_text




def get_ticker(bsObj):
    try:
        tag = bsObj.find('span', {'id':'about_primary_stocks'})
        ticker = tag.a['href'].split('/')[-1]
        return ticker
    
    except AttributeError:
        print('No ticker')
        return None
    

# Need to set up logging. 
















