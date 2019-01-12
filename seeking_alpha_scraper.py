# Scraper for Seeking Alpha

### IMPORT LIBRARIES
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.request import Request
import os

### WEB PAGE OBJECTS
'''
root_url_articles_all = https://seekingalpha.com/article/
start_page            = 1
structure:            Every article 
                      Takes you to an article which may have many pages. 
                      - page_tag = <span class='pages'>page 1 / 10</span>
                      - timestamp_tag = time content='2006-11-07T06:20:44Z'
                      - date = <time itemprop='datePublished"</time>
                      - title = <span title="NetEase, Inc (NTES)'
                      - ticker = <a symbol='NTES'
                      - link = <div id ='content-rail'
                               <meta content='https://seekingalpha...

Note:                All basic content appears to be included in 
                     <div id='content-rail' 
                     <article>
                     <header>
                     use to get the first time datetime, meta content="" for the link

Title                <div class='a-themes'>
                     <h1 itemprop='headline'>


root_url_articles_transcripts = https://seekingalpha.com/earnings/earnings-call-transcripts

Using headers:
                    Updated the creation of the Beautiful soup object to add a 
                    header to see if we can trick 
                    the web page administrator.
                    Taken from "Clandestine scraping techniques web page
'''

url = 'https://seekingalpha.com/article/4232488-kb-homes-kbh-ceo-jeff-mezger-q4-2018-results-earnings-call-transcript'



def get_bsObj(url):
    # Create bs4 Object
    request = Request(url, headers={'User-Agent':'Mozilla/5.0'})
    html    = urlopen(request)
    bsObj   = BeautifulSoup(html.read(), 'lxml')
    return bsObj

def get_date_published(bsObj):
    # Get date puslished
    search = bsObj.findAll('time',{'datetime':''})
    date   = search[0].text
    return date

def get_article_body(bsObj):
    # Get article body
    search = bsObj.findAll('div', {'itemprop':'articleBody'})
    body   = search[0]
    return body

# Generate bsObj
bsObj = get_bsObj(url)

# Get Article Text
'''body = get_article_body(bsObj)'''

# Get article date pusblished
'''date_pubished = get_date_published(bsObj)'''


print(bsObj.time('datetime'))






