# SEEKING ALPH SCRAPER - SCRAPE EARNINGS CALLS



### IMPORT LIBRARIES
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.request import Request
import os
from datetime import datetime
import re


### IMPORT MODULES
import Module1_get_data_points as m1


# URL OBJECTS
url = 'https://seekingalpha.com/article/4232488-kb-homes-kbh-ceo-jeff-mezger-q4-2018-results-earnings-call-transcript'




### ARTICLE ATTRIBUTES------------------------------------------------------------

## Generate bsObj
bsObj = m1.get_bsObj(url)

## Get Article Title
#title = m1.get_title(bsObj)

## Get Article Text
#ecall_text = m1.get_ecall_text(bsObj)

## Get Publication Date
#publication_date = m1.get_date_published(bsObj)


