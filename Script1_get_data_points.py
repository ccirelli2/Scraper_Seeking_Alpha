# SEEKING ALPH SCRAPER - SCRAPE EARNINGS CALLS



### IMPORT LIBRARIES
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.request import Request
import os

### IMPORT MODULES
import Module1_get_data_points as m1


# URL OBJECTS
url = 'https://seekingalpha.com/article/4232488-kb-homes-kbh-ceo-jeff-mezger-q4-2018-results-earnings-call-transcript'




# SCRAPER

# Generate bsObj
bsObj = m1.get_bsObj(url)

# Get Article Title


# Get Article Text
ecall_text = m1.get_ecall_text(bsObj)

# Get Publication Date
publication_date = m1.get_date_published(bsObj)

print(publication_date)


# Get article date pusblished
'''date_pubished = get_date_published(bsObj)'''








