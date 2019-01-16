### CONFIG FILE
'''

Passwords:
        1.) MySQL:              Need to amend the sys.path name to the dir where the password
                                file is located.  Then import that file. 

Target Directories:
        1.) Transcripts:        Location for output of transcript text files. 





'''






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

