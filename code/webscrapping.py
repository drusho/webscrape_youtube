# pip install selenium

#import libraries
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC #specify driver path
import time
DRIVER_PATH = '/opt/homebrew/bin/chromedriver'
driver = webdriver.Chrome(executable_path = DRIVER_PATH)


action = ActionChains(driver)

#Open chrome browser to url
driver.get('https://indeed.com')
driver.implicitly_wait(30)
driver.set_page_load_timeout(50)

#Enter Job and Location Search Terms
job_search_term = 'data analyst'
job_search_location = 'new york'
display_limit_num = '30'


def general_search(job, location):

    #select job input 'What'
    job_selection = driver.find_element_by_xpath('//*[@id="text-input-what"]')
    job_selection.send_keys([job_search_term])

    #select job input 'Where'
    location_selection = driver.find_element_by_xpath('//*[@id="text-input-where"]')
    time.sleep(1)
    location_selection.send_keys(Keys.COMMAND+"a")
    time.sleep(1)
    location_selection.send_keys([job_search_location])

    #initiate search by clicking 'find_jobs' buttom
    find_jobs_button = driver.find_element_by_xpath('//*[@id="whatWhereFormId"]/div[3]/button')
    find_jobs_button.click()

    return print(f"General Search for {job_search_term} in {job_search_location} completed")


# Close Pop-Up
# close_popup = driver.find_element_by_id("popover-close-link")
# close_popup.click()

def advanced_job_search(job,limit):
    #From main site, find and click advanced search buttom
    advanced_search = driver.find_element_by_xpath("//a[contains(text(),'Advanced Job Search')]")
    advanced_search.click()

    #set job search term
    search_job = driver.find_element_by_xpath('//input[@id="as_and"]')
    search_job.send_keys([job_search_term])

    #set display limit results per page
    display_limit = driver.find_element_by_xpath(f'//select[@id="limit"]//option[@value={display_limit_num}]')
    display_limit.click()

    #sort results by date
    sort_option = driver.find_element_by_xpath('//select[@id="sort"]//option[@value="date"]')
    sort_option.click()

    #initiate advanced search
    search_button = driver.find_element_by_xpath('//*[@id="fj"]')
    search_button.click()


general_search(job_search_term,job_search_location)

# advanced_job_search(job_search_term, display_limit)