import csv 
import time
from selenium import webdriver

def selenium_interpreter (browser, cmd, param_1):
    
    """ 
    selenium_interpreter ()
    
    This function executes the commands passed to it, using the appropriate
    selenium equivalent.
    
    """
    cmd_executed = False                # Set boolean to indicate a command has
                                        # not been executed.
    if (cmd == 'navigate_to'):
        browser.get(param_1)
        cmd_executed = True
        
    if (cmd == 'click'): 
        radio = browser.find_element_by_id(param_1).click() 
        cmd_executed = True 
     
    if (cmd_executed == False):         # If no command was executed, exit with
        return False                    # False, indicating an error condition.
    else:
        return True
    
def selenium_scraper (csv_file_name, chrome_driver):

    """ 
    selenium_scraper ()
    
    This function illustrates how to write a data-driven web scraper, using 
    Selenium.  Although the Selenium documentation indicates that Firefox is 
    supported, the webdriver.FireFox() method always passed control to the 
    browser, halting program execution in doing so.
    
    This function accepts two parameters, the name of the .csv file that 
    provides the data to drive program execution and the location of the 
    chromedriver.
    
    """
    
    # Validate that our two expected parameters have values.
    
    if (csv_file_name is None or len(csv_file_name) <= 0):
        print ('The csv_file_name parameter is empty in selenium_scraper()...')
        return False
    
    if (chrome_driver is None or len(chrome_driver) <= 0):
        print ('The chrome_driver parameters is empty in selenium_scraper().')
        return False
        
    browser = webdriver.Chrome(chrome_driver)
    
    # Open and read the .csv file with header 'cmd, param_1, param_2, etc...'
    
    with open (csv_file_name) as csv_file_handle:   
        reader = csv.DictReader (csv_file_handle)
        
        for row in reader:
            status = selenium_interpreter (browser, row['cmd'], row['param_1'])
            
            if (status == False):
                print ('Command' + row['cmd'] + ' is invalid in selenium_interpreter()')
                break 

    browser.quit()

# Driver to test selenium_scraper ()

selenium_scraper ('c:\informatics\selenium.csv', 'c:\informatics\chromedriver')