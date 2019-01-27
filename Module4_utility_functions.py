# UTILITY FUNCTIONS USED THROUGHOUT THE PROGRAM
'''INCLUDED IN THIS MODULE
1.) progress_recorder:
2.) create_txt_file:        Create text file of transcript document. 
'''

# IMPORT LIBRARIES
import os


def progress_recorder(Count_obj, range_value_obj):
    '''
    Inputs      
        Count_obj:  This is the current count of the for loop, i.e. 
        the current count of the number of pages scraped.  
        range_value_obj: This represents the integer value of the last 
        page of the web page minus the first, so the total number of pages to scrape.       
    '''
    if Count_obj == 1:
        print('Scraping started')
    elif Count_obj == round(range_value_obj * 0.01, 0):
        print('1% Complete')
    elif Count_obj == round(range_value_obj * 0.05, 0):
        print('5% Complete')
    elif Count_obj == round(range_value_obj * 0.1,0):
        print('10% Complete')
    elif Count_obj == round(range_value_obj * 0.15,0):
        print('15% Completed')
    elif Count_obj == round(range_value_obj * 0.20,0):
        print('20% Complete')
    elif Count_obj == round(range_value_obj * 0.25,0):
        print('25% Completed')
    elif Count_obj == round(range_value_obj * 0.3,0):
        print('30% Completed')
    elif Count_obj == round(range_value_obj * 0.35,0):
        print('35% Completed')
    elif Count_obj == round(range_value_obj * 0.4,0):
        print('40% Completed')
    elif Count_obj == round(range_value_obj * 0.5,0):
        print('50% Completed')
    elif Count_obj == round(range_value_obj * 0.6,0):
        print('60% Completed')
    elif Count_obj == round(range_value_obj * 0.7,0):
        print('70% Completed')
    elif Count_obj == round(range_value_obj * 0.8,0):
        print('80% Completed')
    elif Count_obj == round(range_value_obj * 0.9,0):
        print('90% Completed')
    elif Count_obj == round(range_value_obj * 1.0,0):
        print('RRRRRR!!!!!!.......Scraping 100% Complete!!')
        print('Ok to proceed to the next job!\n')
    return None


def create_txt_file(target_dir, file_name, text):
    os.chdir(target_dir)
    f = open(file_name + '.txt', 'w+')
    f.write(text)
    f.close()

    return None










