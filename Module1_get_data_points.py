### IMPORT LIBRARIES
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.request import Request
import os


# FUNCTIONS GET VALUES FROM WEB PAGE


def get_bsObj(url):
    # Create bs4 Object
    request = Request(url, headers={'User-Agent':'Mozilla/5.0'})
    html    = urlopen(request)
    bsObj   = BeautifulSoup(html.read(), 'lxml')
    return bsObj

def get_date_published(bsObj):
    # Get date puslished
    search = bsObj.findAll('time',{'itemprop':'datePublished'})
    date = search[0].text
    return search 

def get_ecall_text(bsObj):
    # Get article body
    search = bsObj.findAll('div', {'itemprop':'articleBody'})
    body   = search[0]
    return body



















